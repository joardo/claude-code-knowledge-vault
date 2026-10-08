#!/usr/bin/env python3
"""
Claude Code Official Documentation Ingestion & Transformation Engine.
Crawls all 221 pages from https://code.claude.com/docs/llms.txt,
transforms them into Obsidian Open Knowledge atomic notes with YAML frontmatter,
converts links to bidirectional [[wikilinks]], and generates the scrape manifest.
"""

import os
import re
import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VAULT_DIR = "/home/joaquin/Documents/Official Claude Code Docs"
META_DIR = os.path.join(VAULT_DIR, "00_Meta")

def clean_name(s):
    s = re.sub(r'[^\w\s\-]', '', s).strip()
    return re.sub(r'\s+', '_', s)

def load_pages():
    with open(os.path.join(META_DIR, "parsed_pages.json")) as f:
        return json.load(f)

def determine_target_dir(p):
    slug = p['slug']
    h2 = p['h2']
    h3 = p['h3']
    
    # Release notes
    if slug.startswith('whats-new') or h2 == "What's New":
        return "90_Release_Notes", "release-notes"
    
    # Agent SDK
    if slug.startswith('agent-sdk') or h2 == "Agent SDK":
        return "45_Agent_SDK", "agent-sdk"
    
    # Extensibility, MCP, Plugins, Mods
    if (h2 == "Plugins" or 
        slug.startswith("plugins/") or 
        h3 in ["MCP", "Skills", "Artifacts"] or
        slug in ["mcp", "mcp-quickstart", "skills", "artifacts"]):
        return "40_Extensibility_and_MCP", "extensibility"
        
    # Hooks and Events, Channels, Scheduling
    if (h3 == "Automation" and slug in ["hooks-guide", "channels", "scheduled-tasks"]) or \
       slug in ["hooks", "channels-reference"]:
        return "50_Hooks_and_Events", "hooks-events"
        
    # Administration and Security / Gateways
    if h2 == "Administration" or slug in ["admin-setup", "managed-settings", "server-managed-settings", "managed-mcp"]:
        return "35_Administration_and_Security", "admin-security"
        
    # Memory and Config
    if (h3 in ["Settings", "Environments"] and not slug.startswith("self-hosted")) or \
       slug in ["memory", "claude-directory", "settings", "settings-reference", "settings-example", "output-styles"]:
        return "30_Memory_and_Config", "memory-config"
        
    # Core Architecture
    if (h3 in ["Core concepts", "Model and responses", "Permissions and sandboxing"] and 
        slug not in ["claude-directory", "output-styles"]) or \
       slug in ["checkpointing", "tools-reference"]:
        return "10_Core_Architecture", "architecture"
        
    # CLI and Commands
    if slug in ["cli-reference", "commands", "env-vars", "interactive-mode", "overview", "quickstart", "changelog", 
                "sessions", "common-workflows", "prompt-library", "best-practices", "terminal-config", 
                "fullscreen", "accessibility", "voice-dictation", "statusline", "keybindings", "fast-mode"]:
        return "20_CLI_and_Commands", "cli-runtime"
        
    # Workflows and Patterns
    return "60_Workflows_and_Patterns", "workflows"

def build_manifest_and_mappings(pages):
    slug_map = {}
    used_names = set()
    mappings = []
    
    for p in pages:
        slug = p['slug']
        title = p['title'].strip()
        target_dir, cat_tag = determine_target_dir(p)
        
        if slug.startswith('agent-sdk/') and not title.lower().startswith('agent sdk'):
            base = f"Agent_SDK_{clean_name(title)}"
        elif slug.startswith('plugins/mods/') and not title.lower().startswith('mod'):
            base = f"Mod_{clean_name(title)}"
        elif slug.startswith('whats-new/'):
            week_match = re.search(r'(\d{4}-w\d+)', slug)
            if week_match:
                base = f"Release_{week_match.group(1)}"
            else:
                base = f"Release_{clean_name(title)}"
        else:
            base = clean_name(title)
            
        if base in used_names:
            slug_suffix = slug.replace('/', '_').replace('-', '_')
            base = f"{base}_{slug_suffix}"
            
        used_names.add(base)
        slug_map[slug] = base
        
        mappings.append({
            "page": p,
            "target_dir": target_dir,
            "filename": f"{base}.md",
            "base": base,
            "cat_tag": cat_tag
        })
        
    return slug_map, mappings

def fetch_url(url, retries=3):
    headers = {"User-Agent": "Claude-Code-Doc-Archiver/1.0"}
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read().decode('utf-8')
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(1 + attempt)

def transform_to_open_knowledge(raw_content, item, slug_map):
    p = item['page']
    title = p['title'].strip()
    slug = p['slug']
    target_dir = item['target_dir']
    base = item['base']
    cat_tag = item['cat_tag']
    desc = p['desc'].strip()
    
    # 1. Strip crawler header
    content = re.sub(r'^>\s*##\s*Documentation Index.*?(?=# )', '', raw_content, flags=re.DOTALL).strip()
    if not content:
        content = raw_content.strip()
        
    # Remove leading '# Title' if present so we control the title rendering
    content = re.sub(r'^#\s+.*?\n+', '', content, flags=re.DOTALL)
    
    # Extract leading blockquote if present as summary
    extracted_summary = ""
    summary_match = re.match(r'^>\s*(.*?)\n\n', content, flags=re.DOTALL)
    if summary_match:
        extracted_summary = summary_match.group(1).replace('\n> ', ' ').strip()
        content = content[summary_match.end():].strip()
        
    final_summary = extracted_summary if extracted_summary else desc
    
    # 2. Transform links to [[wikilinks]]
    # Match [label](/docs/en/slug.md#anchor) or [label](/docs/en/slug) or full URL https://code.claude.com/docs/en/slug
    link_pattern = r'\[([^\]]+)\]\((?:https://code\.claude\.com)?/docs/en/([a-zA-Z0-9_\-\./]+?)(?:\.md)?(?:#([a-zA-Z0-9_\-\.]+))?\)'
    def repl(m):
        label = m.group(1).strip()
        link_slug = m.group(2).rstrip('/')
        if link_slug in slug_map:
            target_base = slug_map[link_slug]
            if label == target_base:
                return f"[[{target_base}]]"
            else:
                return f"[[{target_base}|{label}]]"
        return m.group(0)
    
    content = re.sub(link_pattern, repl, content)
    
    # 3. Build related concepts links based on target_dir
    moc_map = {
        "10_Core_Architecture": "[[MOC_Core_Architecture|Core Architecture MOC]]",
        "20_CLI_and_Commands": "[[MOC_CLI_and_Runtime|CLI & Runtime MOC]]",
        "30_Memory_and_Config": "[[MOC_Memory_and_Context|Memory & Context MOC]]",
        "35_Administration_and_Security": "[[MOC_Administration_and_Security|Administration & Security MOC]]",
        "40_Extensibility_and_MCP": "[[MOC_Extensibility_and_MCP|Extensibility & MCP MOC]]",
        "45_Agent_SDK": "[[MOC_Agent_SDK|Agent SDK MOC]]",
        "50_Hooks_and_Events": "[[MOC_Hooks_and_Automation|Hooks & Automation MOC]]",
        "60_Workflows_and_Patterns": "[[MOC_Workflows_and_Patterns|Workflows & Patterns MOC]]",
        "90_Release_Notes": "[[MOC_Release_Notes|Release Notes MOC]]"
    }
    
    category_moc = moc_map.get(target_dir, "[[MOC_Claude_Code|Claude Code MOC]]")
    
    # 4. Generate YAML Frontmatter
    safe_title = title.replace('"', '\\"')
    frontmatter = f"""---
title: "{safe_title}"
aliases:
  - "{slug}"
  - "{safe_title}"
tags:
  - "claude-code"
  - "{cat_tag}"
source_url: "https://code.claude.com/docs/en/{slug}"
status: "verified"
last_updated: "2026-10"
---

# {title}

## Executive Summary
> {final_summary}

## Technical Mechanics & Documentation

{content}

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- {category_moc}
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]
"""
    return frontmatter

def main():
    pages = load_pages()
    slug_map, mappings = build_manifest_and_mappings(pages)
    
    # Ensure all directories exist
    dirs_to_create = set(m['target_dir'] for m in mappings)
    dirs_to_create.add("00_MOC")
    dirs_to_create.add("70_Tool_Selection_Matrix")
    dirs_to_create.add("80_Agent_Skills/claude-platform-master/references")
    for d in dirs_to_create:
        os.makedirs(os.path.join(VAULT_DIR, d), exist_ok=True)
        
    print(f"Starting crawl and processing of {len(mappings)} documents...")
    
    manifest = []
    
    def process_item(item):
        p = item['page']
        url = f"https://code.claude.com/docs/en/{p['slug']}.md"
        t0 = time.time()
        try:
            raw = fetch_url(url)
            transformed = transform_to_open_knowledge(raw, item, slug_map)
            out_path = os.path.join(VAULT_DIR, item['target_dir'], item['filename'])
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(transformed)
            duration = round(time.time() - t0, 2)
            return {
                "url": url,
                "title": p['title'],
                "slug": p['slug'],
                "target_dir": item['target_dir'],
                "filename": item['filename'],
                "path": os.path.relpath(out_path, VAULT_DIR),
                "bytes": len(transformed),
                "status": "success",
                "duration_seconds": duration,
                "fetched_at": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "url": url,
                "title": p['title'],
                "slug": p['slug'],
                "target_dir": item['target_dir'],
                "filename": item['filename'],
                "path": os.path.join(item['target_dir'], item['filename']),
                "status": "error",
                "error": str(e),
                "fetched_at": datetime.now().isoformat()
            }

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_item, it): it for it in mappings}
        completed = 0
        for f in as_completed(futures):
            res = f.result()
            manifest.append(res)
            completed += 1
            if completed % 25 == 0 or completed == len(mappings):
                print(f"Progress: {completed}/{len(mappings)} completed. Latest: {res['slug']} ({res['status']})")

    # Save manifest
    manifest_path = os.path.join(META_DIR, "scrape_manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
        
    # Also save slug_map for auditing and matrix generation
    slug_map_path = os.path.join(META_DIR, "slug_map.json")
    with open(slug_map_path, 'w', encoding='utf-8') as f:
        json.dump(slug_map, f, indent=2)
        
    errors = [m for m in manifest if m['status'] != 'success']
    print(f"\nFinished! Total successfully processed: {len(manifest) - len(errors)} / {len(manifest)}")
    if errors:
        print(f"Encountered {len(errors)} errors:")
        for err in errors:
            print(f"  - {err['slug']}: {err['error']}")

if __name__ == "__main__":
    main()

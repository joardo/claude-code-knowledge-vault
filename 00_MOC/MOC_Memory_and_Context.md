---
title: "MOC: Memory, Context & Configuration"
aliases:
  - "MOC_Memory_and_Context"
tags:
  - "claude-code"
  - "moc"
  - "memory"
status: "verified"
last_updated: "2026-10"
---

# MOC: Memory, Context & Configuration

> How Claude Code accumulates persistent project knowledge, reads multi-tier configuration, and controls behavioral persona.

## 1. Project Memory & Conventions
- [[How_Claude_remembers_your_project|How Claude Remembers Your Project]]: The authoritative guide to `CLAUDE.md`, `AGENTS.md`, and auto-memory (`MEMORY.md`).
- [[Explore_the_claude_directory|Explore the .claude Directory]]: Architectural layout of project-local `.claude/` vs global `~/.claude/` directories.
- [[Output_styles|Output Styles]]: Customizing personality, brevity, and tone (Concise, Explanatory, Custom).

## 2. Settings & Precedence Architecture
- [[Settings_files_and_precedence|Settings Files & Precedence]]: 5-tier settings hierarchy (Enterprise Managed -> Project `.claude/settings.json` -> User `~/.claude/settings.json` -> CLI Flags).
- [[All_settings|All Settings Reference]]: Complete schema reference of every key in `settings.json`.
- [[Example_settings_files|Example Settings Files]]: Production settings templates for solo developers, teams, and enterprise orgs.
- [[Configure_cloud_environments|Configure Cloud Environments]]: Cloud VM runner environments, secrets, and setup scripts.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Core_Architecture|Core Architecture]]
- [[Matrix_Memory_Architectures|Memory Hierarchy Matrix]]

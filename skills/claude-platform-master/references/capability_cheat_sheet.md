---
title: "Claude Code Platform Capabilities Cheat Sheet"
aliases:
  - "capability_cheat_sheet"
  - "Claude Capabilities Cheat Sheet"
tags:
  - "claude-code"
  - "reference"
  - "cheat-sheet"
status: "verified"
last_updated: "2026-10"
---

# Claude Code Platform Capabilities Cheat Sheet

> Fast lookup reference covering all CLI commands, flags, slash commands, environment variables, and configuration paths.

## 1. CLI Commands & Flags
- `claude`: Start interactive session.
- `claude "prompt"`: Start interactive session with initial prompt.
- `claude -p "query"`: Headless one-shot execution, print answer, exit.
- `claude -c`: Continue most recent conversation in current directory.
- `claude -c -p "query"`: Continue conversation non-interactively via SDK.
- `claude -r "<session_id>"`: Resume specific session by ID or name.
- `claude agents`: Open background Agent View dashboard.
- `claude attach <id>`: Attach to a running background session.
- `claude --worktree`: Spin up session inside an isolated Git worktree.
- `claude --permission-mode <mode>`: One of `default`, `autoMode`, `acceptEdits`, `restricted`.
- `claude --dangerously-skip-permissions`: Bypass all interactive approvals (disposable environments only).
- `claude --model <name>`: Model selection (`sonnet`, `opus`, `haiku`).
- `claude --effort <level>`: Effort level (`low`, `medium`, `high`, `xhigh`).
- `claude --style <style>`: Output style (`concise`, `explanatory`, custom).
- `claude doctor`: Run read-only setup and configuration diagnostics.
- `claude mcp login <name>`: OAuth login for remote MCP servers.

## 2. In-Session Slash Commands
- `/goal <condition>`: Autonomous persistent loop until condition is satisfied.
- `/loop <interval> <prompt>`: Schedule recurring check in session.
- `/compact`: Force-trigger context window compaction to free tokens.
- `/doctor`: Run setup diagnostic and auto-repair.
- `/cost` or `/usage`: Display session token breakdown and cost attribution.
- `/rewind`: Roll back conversation and file changes to a previous checkpoint.
- `/clear`: Clear conversation context (restarts prompt cache).
- `/config`: Inspect or modify live session configuration.
- `/model`: Switch models mid-session.
- `/code-review`: Trigger multi-agent diff review.
- `/ultrareview`: Deep cloud multi-agent vulnerability and bug analysis.

## 3. Configuration & Memory Paths
- Project Root Memory: `<repo>/CLAUDE.md` or `AGENTS.md`
- Subdirectory Memory: `<repo>/packages/<pkg>/CLAUDE.md`
- Project Settings: `<repo>/.claude/settings.json`
- User Global Memory: `~/.claude/CLAUDE.md`
- User Global Settings: `~/.claude/settings.json`
- Custom Skills: `.claude/skills/<name>/SKILL.md` or `~/.claude/skills/`
- Custom Slash Commands: `.claude/commands/<name>.md`
- Custom Mods: `.claude/mods/<name>/`
- Auto-Memory File: `~/.claude/projects/<project-hash>/MEMORY.md`
- Enterprise Managed Settings: `/etc/claude-code/settings.json` (Linux/macOS)

## 4. Lifecycle Hooks Matrix
- `PreToolUse`: Fires before tool executes. Can block execution (exit non-zero) or modify parameters.
- `PostToolUse`: Fires immediately after tool completes. Ideal for linters, formatters, test triggers.
- `Prompt`: Fires when user enters prompt before sending to LLM.
- `Stop`: Fires when Claude completes a turn or full goal.

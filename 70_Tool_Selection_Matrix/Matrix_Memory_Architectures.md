---
title: "Decision Matrix: Memory & Context Architectures"
aliases:
  - "Matrix_Memory_Architectures"
  - "Memory Hierarchy Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "memory"
  - "context"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Memory & Context Architectures

> Choosing where instructions, project conventions, and learnings should live across the Claude Code hierarchy.

## Comparative Matrix

| Layer | File / Location | Scope | Persistence | Token Cost Impact | Best Used For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Enterprise Managed Settings** | `/etc/claude-code/` or cloud server | Organization-wide | Immutable by developer | Injected into system config | Enforcing security policies, approved models, telemetry endpoints |
| **User Global Memory** | `~/.claude/CLAUDE.md` | All projects for this user | Permanent | Injected on every session startup | Personal coding preferences, preferred style, terminal preferences |
| **Project Root Memory** | `<repo>/CLAUDE.md` or `AGENTS.md` | Entire repository | Version-controlled with git | Cached via Prompt Caching (high hit rate) | Project build/test commands, architecture principles, code conventions |
| **Subdirectory Memory** | `<repo>/packages/<pkg>/CLAUDE.md` | Subtree / monorepo package | Activated when Claude operates in subtree | Injected on context entry | Package-specific build scripts, local architecture rules in monorepos |
| **Auto-Memory** | `~/.claude/projects/<proj>/MEMORY.md` | Project-specific (accumulated) | Automatically saved by Claude | First 200 lines / 25KB loaded on startup | Learnings Claude discovers over time (quirks, failed approaches) |
| **Ephemeral Session Context** | Live conversation history | Current session only | Discarded on session clear | Grows per turn; pruned by `/compact` | Active task progress, transient investigation logs, debug outputs |

---

## Memory Architecture Principles

1. **Keep `CLAUDE.md` Terse & High-Signal**:
   - Do NOT duplicate documentation that exists in README or code comments.
   - Store **build commands**, **test commands**, **lint commands**, and non-obvious project traps.
   - Format with bullet points; avoid verbose prose to maximize prompt cache efficiency.
2. **Leverage Prompt Caching**:
   - Editing `CLAUDE.md` in the middle of a session invalidates prompt caching for subsequent turns. Keep base memory stable.
3. **Monorepo Strategy**:
   - Root `CLAUDE.md`: High-level repo layout, overall build orchestration, global git guidelines.
   - Package `CLAUDE.md`: Local commands (e.g. `pnpm --filter @app/core test`).

---
## Related References
- [[How_Claude_remembers_your_project|How Claude Remembers Your Project]]
- [[Settings_files_and_precedence|Settings Files & Precedence]]
- [[Set_up_Claude_Code_in_a_monorepo_or_large_codebase|Monorepo Setup Guide]]

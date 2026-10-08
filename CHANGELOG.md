# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-08

### Added
- **Full Claude Code Official Documentation Vault**:
  - 221 official documentation pages crawled, transformed, and indexed into Open Knowledge atomic notes with YAML frontmatter.
  - 10 specialized Maps of Content (MOCs) serving as knowledge graph entrypoints.
  - 10,780+ verified bidirectional `[[wikilinks]]` with zero broken references.
- **Claude Platform Master Skill (`claude-platform-master`)**:
  - Progressive disclosure architecture (`SKILL.md` trimmed to 76 lines, saving ~73% recurring context tokens).
  - Standalone `references/capability_cheat_sheet.md` for instant lookup of CLI flags, slash commands, paths, and hook schemas.
  - Standalone `references/consultation_examples.md` containing 5 end-to-end real-world consultation case studies.
- **Comparative Decision Trees & Matrices**:
  - `Matrix_Execution_Modes.md` (Interactive REPL vs Headless vs Loop vs Multi-Agent).
  - `Matrix_Extensibility.md` (Skills vs Commands vs MCP vs Hooks vs Plugins vs Mods).
  - `Matrix_Memory_Architectures.md` (Managed Settings vs Root CLAUDE.md vs Subdir vs Auto-Memory).
  - `Matrix_Tool_Approval_and_Security.md` (Default vs Auto-Mode vs Sandboxed Bash vs Devcontainers).
  - `Matrix_Agentic_Coordination.md` (Inline vs Subagents vs Git Worktrees vs Agent Teams).
- **One-Command Distribution**:
  - `install.sh`: Universal POSIX shell installer with environment auto-detection (Claude Code & Antigravity).
  - `install.ps1`: Windows PowerShell installer.
  - `.claude-plugin/plugin.json`: Native Claude Code plugin manifest.
- **Automated Verification Pipeline**:
  - `00_Meta/ingest_docs.py`: Reproducible crawler & transformer engine.
  - `00_Meta/audit_vault.py`: Automated link integrity and placeholder auditor.
  - `.github/workflows/ci.yml`: Continuous integration quality gate.

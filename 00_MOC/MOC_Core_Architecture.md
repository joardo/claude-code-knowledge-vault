---
title: "MOC: Core Architecture & Foundations"
aliases:
  - "MOC_Core_Architecture"
tags:
  - "claude-code"
  - "moc"
  - "architecture"
status: "verified"
last_updated: "2026-10"
---

# MOC: Core Architecture & Foundations

> Architectural mechanics governing Claude Code's agentic loop, context window budgeting, prompt caching, model tiers, and tool execution engines.

## 1. The Agentic Loop & Reasoning
- [[How_Claude_Code_works|How Claude Code works]]: The fundamental three-phase cycle (Gather Context -> Take Action -> Verify Results), agentic harness structure, and user steering.
- [[Model_configuration|Model Configuration]]: Selecting Sonnet, Opus, and Haiku tiers, effort levels (`low`, `medium`, `high`, `xhigh`), and token parameters.
- [[Escalate_hard_decisions_with_the_advisor_tool|Advisor Tool]]: Autonomous escalation protocol pairing primary models with a secondary reasoning advisor.

## 2. Context Window & Memory Economics
- [[Explore_the_context_window|Explore the Context Window]]: Context budget dynamics, system prompt allocations, tool result overhead, and automatic context compacting.
- [[How_Claude_Code_uses_prompt_caching|Prompt Caching Mechanics]]: 5-minute caching TTL, breakpoint rules, cache write/read cost differences, and cache-friendly practices.

## 3. Sandboxing & Safety Architecture
- [[Configure_permissions|Configure Permissions]]: Fine-grained permission rules, tool allowlists, and execution boundaries.
- [[Choose_a_permission_mode|Choose a Permission Mode]]: Interactive mode, auto mode classifier, accept-edits mode, and bypass mode.
- [[Configure_the_sandboxed_Bash_tool|Sandboxed Bash Tool]]: Containerized command execution, network egress limits, and filesystem jails.
- [[Choose_a_sandbox_environment|Sandbox Environments]]: Comparative breakdown of local sandbox, devcontainers, Docker, and VM boundaries.
- [[Tools_reference|Tools Reference]]: Complete reference of built-in file operations, search regex, shell execution, and web tools.
- [[Checkpointing|Checkpointing & State Rewind]]: Snapshotting file modifications and rolling back conversation states.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_CLI_and_Runtime|CLI & Runtime]]
- [[Matrix_Tool_Approval_and_Security|Security & Approval Matrix]]

---
title: "Decision Matrix: Multi-Agent Coordination & Swarm Patterns"
aliases:
  - "Matrix_Agentic_Coordination"
  - "Multi-Agent Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "multi-agent"
  - "subagents"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Multi-Agent Coordination & Swarm Patterns

> When to keep execution inline vs dispatching subagents, worktrees, agent teams, or dynamic workflows.

## Comparative Matrix

| Pattern | Context Window Isolation | Filesystem Isolation | Concurrency | Communication Channel | Best Used For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Inline Agent** | Single shared context | Same workspace | 1 (Sequential) | Direct chat | Quick edits, linear tasks, targeted bug fixes |
| **Subagents (`sub-agents`)** | **Complete context isolation** | Same workspace | Multi (runs in background) | Task prompt in -> Summary report out | Deep codebase research, isolated refactor passes without context pollution |
| **Worktree Subagents** | Complete context isolation | **Isolated Git Worktree** | Multi (parallel branches) | Git branch merge / PR | Concurrent feature development where file writes would collide |
| **Agent View Dashboard** | Independent sessions | Independent directories / worktrees | High (monitor 10+ sessions) | Shell attach & dashboard | Engineering leads overseeing multiple background projects |
| **Agent Teams** | Multi-agent network | Shared or independent repos | Multi-agent collaboration | Inter-session peer messaging | Complex swarm tasks with dedicated specialized roles (Architect, Coder, Tester) |
| **Dynamic Workflows** | Scripted subagent DAG | Script-defined isolation | Controlled fan-out / fan-in | Script outputs / JSON artifacts | Large-scale repo migrations, exhaustive vulnerability scans across 100 packages |

---

## Architectural Rule of Thumb

- **Will reading 30 files blow up your primary context window?**
  - **Spawn a [[Create_custom_subagents|Subagent]]** for research. The subagent reads the 30 files, summarizes the findings in 500 tokens, and returns only the necessary insight to the orchestrator.
- **Will two agents edit the same codebase simultaneously?**
  - **Always use [[Run_parallel_sessions_with_worktrees|Git Worktrees]]** (`--worktree`). Parallel sessions in the same working directory will overwrite each other's edits and corrupt git staging.
- **Need a repeatable migration pipeline across hundreds of files?**
  - **Use [[Orchestrate_subagents_at_scale_with_dynamic_workflows|Dynamic Workflows]]**.

---
## Related References
- [[Run_agents_in_parallel|Run Agents in Parallel]]
- [[Create_custom_subagents|Create Custom Subagents]]
- [[Run_parallel_sessions_with_worktrees|Parallel Sessions with Worktrees]]

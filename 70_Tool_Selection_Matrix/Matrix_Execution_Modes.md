---
title: "Decision Matrix: Claude Code Execution Modes"
aliases:
  - "Matrix_Execution_Modes"
  - "Execution Modes Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "decision-tree"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Claude Code Execution Modes

> Comparative evaluation of operational modes: Interactive Terminal REPL, Headless Scripting (`-p`), Autonomous Loops (`/goal`), Background Daemons, and Agent Teams.

## Comparative Matrix

| Mode | Interactivity | Autonomy Level | State / Context | Best Used For | Key Commands / Flags |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Interactive REPL** | Full real-time steering | Semi-autonomous (turns pause for user feedback) | Continuous in-session context, resumable | Exploratory coding, pair programming, debugging, multi-file refactoring | `claude`, `claude "initial prompt"` |
| **Headless Script (`-p`)** | Zero (non-interactive) | One-shot execution until task completion or exit | Fresh session or continued with `-c` | CI/CD pipelines, shell scripting, piped input (`cat x \| claude -p`), pre-commit hooks | `claude -p "query"`, `claude -c -p "followup"` |
| **Autonomous Goal (`/goal`)** | Intermittent oversight | Persistent autonomy until explicit condition met | Auto-compacting long-context loop | Complex overnight refactors, test-suite fixing, exhaustive migrations | `/goal "condition"`, [[Keep_Claude_working_toward_a_goal]] |
| **Recurring Cron (`/loop`)** | Asynchronous | Periodic polling & execution | Retains handle or runs fresh | Long-running build monitoring, deployment polling, hourly security audits | `/loop 5m "check tests"`, [[Run_prompts_on_a_schedule]] |
| **Background Agent View** | Dashboard oversight | Full background parallel execution | Independent sessions, attached on demand | Running 5+ concurrent feature branches or audits | `claude agents`, `claude attach <id>`, [[Manage_multiple_agents_with_agent_view]] |
| **Claude Agent SDK** | Fully programmatic | Custom workflow logic | Programmatic session storage (S3/Redis/SQL) | Building custom AI applications, custom IDE integrations, SaaS agent workers | `ClaudeAgentOptions`, [[Agent_SDK_overview]] |

---

## Decision Flowchart

1. **Do you need human-in-the-loop steering while writing code?**
   - **YES** -> Use **[[Interactive_mode|Interactive REPL]]** (`claude`).
   - **NO** -> Proceed to Step 2.
2. **Is this running in an automated environment (CI/CD, cron, git hook)?**
   - **YES** -> Use **[[Run_Claude_Code_programmatically|Headless Mode]]** (`claude -p "..."`).
   - **NO** -> Proceed to Step 3.
3. **Does the task take hours and require Claude to keep trying until an explicit verification check passes?**
   - **YES** -> Use **[[Keep_Claude_working_toward_a_goal|Goal Mode]]** (`/goal`).
   - **NO** -> Proceed to Step 4.
4. **Do you have multiple independent tasks that should run simultaneously?**
   - **YES** -> Use **[[Manage_multiple_agents_with_agent_view|Agent View]]** (`claude agents`) with **[[Run_parallel_sessions_with_worktrees|Worktree isolation]]**.
   - **NO** -> Use standard REPL or SDK.

---
## Related References
- [[MOC_Claude_Code|Master Index]]
- [[CLI_reference|CLI Reference]]
- [[Matrix_Agentic_Coordination|Agentic Coordination Matrix]]

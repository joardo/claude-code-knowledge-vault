---
title: "Run agents in parallel"
aliases:
  - "agents"
  - "Run agents in parallel"
tags:
  - "claude-code"
  - "workflows"
source_url: "https://code.claude.com/docs/en/agents"
status: "verified"
last_updated: "2026-10"
---

# Run agents in parallel

## Executive Summary
> Compare the ways Claude Code can take on multiple tasks at once: subagents, agent view, agent teams, dynamic workflows, and projects.

## Technical Mechanics & Documentation

Claude Code has five ways to work on several tasks at once: [[Create_custom_subagents|subagents]], [[Manage_multiple_agents_with_agent_view|agent view]], [[Orchestrate_teams_of_Claude_Code_sessions|agent teams]], [[Orchestrate_subagents_at_scale_with_dynamic_workflows|dynamic workflows]], and [[Let_Claude_coordinate_ongoing_work_with_Projects|projects]]. They differ in how involved you stay, from steering each conversation yourself to letting Claude coordinate a group of workers, and in whether the work runs on your machine or in the cloud.

| Approach | What it gives you | Use it when |
| :- | :- | :- |
| [[Create_custom_subagents|Subagents]] | Delegated workers inside one session that do a side task in their own context and return a summary | A side task would flood your main conversation with search results, logs, or file contents you won't reference again |
| [[Manage_multiple_agents_with_agent_view|Agent view]] | One screen to dispatch and monitor sessions running in the background, opened with `claude agents`. Research preview | You have several independent tasks and want to hand them off, check status at a glance, and step in only when one needs you |
| [[Orchestrate_teams_of_Claude_Code_sessions|Agent teams]] | Multiple coordinated sessions with a shared task list and inter-agent messaging, managed by a lead. Experimental and disabled by default | You want Claude to split a project into pieces, assign them, and keep the workers in sync |
| [[Let_Claude_coordinate_ongoing_work_with_Projects|Projects]] | One ongoing conversation at claude.ai/code or in the desktop app. Claude starts parallel sessions called threads, in the cloud or, when you ask, on your computer through Remote Control, gives each one the project's instructions, and shows you which ones need you. Public beta on Pro and Max | The work spans many tasks over days or weeks, should keep running when your machine is off, and you'd rather describe it once than dispatch and track each session |
| [[Orchestrate_subagents_at_scale_with_dynamic_workflows|Dynamic workflows]] | A script that runs many subagents and cross-checks their results, for work too big to coordinate one turn at a time or that needs more than a single pass | A job outgrows a handful of subagents, or you want findings verified against each other: a codebase-wide audit, a 500-file migration, cross-checked research, or a plan drafted from several angles |

In every approach the workers are Claude sessions. To involve a different tool, expose it to Claude as an [[Connect_Claude_Code_to_tools_via_MCP|MCP server]].

Three more tools support this work without being a way to run agents themselves:

* [[Run_parallel_sessions_with_worktrees|Worktrees]] give each session a separate git checkout, so parallel sessions each edit their own copy of the files. Use them for sessions you run yourself. A session you dispatch from agent view [[Manage_multiple_agents_with_agent_view|moves into a worktree of its own before it edits files]], and subagents you spawn can each get one too.
* [[Message_your_other_Claude_Code_sessions|Cross-session messaging]] lets Claude list and message your other Claude Code sessions on this machine, on another machine, or [[Use_Claude_Code_in_the_cloud|in the cloud]], so sessions you run yourself can pass findings and status between themselves.
* [[Commands|`/batch`]] is a [[Extend_Claude_with_skills|skill]] that has Claude split one large change into 5 to 30 worktree-isolated subagents. It's a packaged use of subagents and worktrees, not a separate coordination style.

A few other features run Claude without you driving each step, but they solve a different problem than splitting work across agents:

* A [[Interactive_mode|background bash command]] runs one shell command without blocking the conversation. It doesn't spawn an agent.
* A [[Create_custom_subagents|forked subagent]] is a subagent that inherits your full conversation context instead of starting fresh. It's a way to spawn a subagent, not a separate surface. Start one with `/subtask`. Claude also spawns one itself where [[Create_custom_subagents|fork mode]] is on. To copy the whole session into a new [[Manage_multiple_agents_with_agent_view|background session]] that runs alongside it, use `/fork`. With [[Manage_multiple_agents_with_agent_view|agent view turned off]], the forked-subagent command is `/fork` instead and `/subtask` isn't available.
* A [[Automate_work_with_routines|routine]] runs a session on a schedule in the cloud, not in parallel on your machine.

<Note>
  Running several sessions or subagents at once multiplies token usage. See [[Manage_costs_effectively|Costs]] for usage and rate-limit details.
</Note>

## Choose an approach

The right approach depends on who coordinates the work, whether the workers need to communicate, and whether they edit the same files:

* **Who coordinates the work?**
  * Claude delegates and collects results inside one conversation: [[Create_custom_subagents|subagents]]
  * You hand off independent tasks and check back later: [[Manage_multiple_agents_with_agent_view|agent view]]
  * Claude plans, assigns, and supervises a group of workers: [[Orchestrate_teams_of_Claude_Code_sessions|agent teams]], experimental and disabled by default
  * A script holds the plan instead of Claude's turn-by-turn judgment: [[Orchestrate_subagents_at_scale_with_dynamic_workflows|dynamic workflows]]. See [[Orchestrate_subagents_at_scale_with_dynamic_workflows|how workflows compare to subagents and skills]]
* **Do the workers need to talk to each other?** Claude can pass findings with [[Message_your_other_Claude_Code_sessions|cross-session messaging]] between sessions you run yourself, including the sessions you dispatch from agent view. Subagents report results back to the conversation that spawned them, and agent view sessions report results only to you. Teammates in an agent team message each other directly and, when they [[Tools_reference|have the Task tools]], share a task list.
* **Do the tasks touch the same files?** Isolate the work with [[Run_parallel_sessions_with_worktrees|worktrees]]. Subagents and sessions you run yourself can each use a separate worktree. Agent teams don't isolate teammates in worktrees, so [[Orchestrate_teams_of_Claude_Code_sessions|partition the work]] so each teammate owns a different set of files.

## Check on running work

The command for checking on running work depends on which approach you used:

* For background sessions, `claude agents` opens [[Manage_multiple_agents_with_agent_view|agent view]]: one screen showing every session, its state, and which ones need your input.
* For subagents in the current session, named background subagents appear in the @-mention typeahead with their status. The `/agents` command prints a notice pointing to the subagent file locations. To [[Create_custom_subagents|create and edit custom subagents]], ask Claude or edit the files directly. Despite the similar name, `/agents` is separate from `claude agents`.
* For anything running in the background of the current session, `/tasks` lists each item and lets you check on, attach to, or stop it. The list also includes subagents that have finished.
* For dynamic workflows, `/workflows` lists running and completed runs, the phase each is in, and how many agents have finished.

For a desktop view of all your sessions, see [[Desktop_application|parallel sessions in the desktop app]].

## Learn more

Each guide below covers setup and configuration for one approach:

* [[Create_custom_subagents|Create custom subagents]]: define reusable specialists and control which tools they can use.
* [[Manage_multiple_agents_with_agent_view|Manage agents with agent view]]: dispatch sessions, watch their state, and attach when one needs you.
* [[Orchestrate_teams_of_Claude_Code_sessions|Orchestrate agent teams]]: set up a lead and teammates, assign tasks, and review their work.
* [[Orchestrate_subagents_at_scale_with_dynamic_workflows|Orchestrate dynamic workflows]]: run a bundled workflow or have Claude write one that runs many subagents and verifies their findings against each other.
* [[Run_parallel_sessions_with_worktrees|Run parallel sessions with worktrees]]: start Claude in an isolated checkout, control what gets copied in, and clean up afterward.

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

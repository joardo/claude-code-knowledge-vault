---
title: "MOC: Agentic Workflows & Multi-Agent Coordination"
aliases:
  - "MOC_Workflows_and_Patterns"
tags:
  - "claude-code"
  - "moc"
  - "workflows"
  - "multi-agent"
status: "verified"
last_updated: "2026-10"
---

# MOC: Agentic Workflows & Multi-Agent Coordination

> Strategies for single-agent autonomy, multi-agent swarms, headless automation, and platform integrations.

## 1. Multi-Agent & Parallel Execution
- [[Run_agents_in_parallel|Run Agents in Parallel]]: Comparative overview of subagents, agent view, agent teams, and worktrees.
- [[Create_custom_subagents|Create Custom Subagents]]: Task-specific subagents with isolated context windows.
- [[Manage_multiple_agents_with_agent_view|Agent View]]: Dispatching and monitoring multiple background sessions from one dashboard.
- [[Orchestrate_teams_of_Claude_Code_sessions|Agent Teams]]: Inter-agent coordination, shared tasks, and cross-session messaging.
- [[Message_your_other_Claude_Code_sessions|Cross-Session Messaging]]: Sending peer messages between running Claude Code instances.
- [[Run_parallel_sessions_with_worktrees|Worktree Git Isolation]]: Zero-collision parallel branch execution using Git worktrees.
- [[Orchestrate_subagents_at_scale_with_dynamic_workflows|Dynamic Workflows]]: Programmatically generating subagent orchestration scripts.

## 2. Autonomous Execution & Scripting
- [[Keep_Claude_working_toward_a_goal|Autonomous Goal (/goal)]]: Long-running completion criteria that prevent premature exit.
- [[Run_Claude_Code_programmatically|Run Claude Code Programmatically (Headless)]]: Scripting `claude -p` in bash and pipelines.
- [[Launch_sessions_from_links|Deep Links (`claude-cli://`)]]: One-click session launch from URLs.

## 3. Code Review & CI/CD
- [[Code_Review|Automated Code Review]]: Multi-agent PR review pipelines.
- [[Find_bugs_with_ultrareview|Ultrareview]]: Cloud-based deep bug analysis.
- [[Claude_Code_GitHub_Actions|GitHub Actions]]: Automated bot integration for issues and PRs.
- [[Claude_Code_GitLab_CICD|GitLab CI/CD]]: GitLab pipeline integration.
- [[Catch_security_issues_as_Claude_writes_code|Security Guidance Plugin]]: Real-time vulnerability patching.
- [[Scan_your_codebase_for_vulnerabilities|Claude Security]]: In-session repository security auditing.

## 4. Platforms & Interfaces
- [[Platforms_and_integrations|Platforms Overview]]: Choosing between CLI, Desktop, Web, IDEs, and Mobile.
- [[Desktop_application|Claude Code Desktop]]: Multi-pane visual workspace, app previews, and iOS simulator.
- [[Use_Claude_Code_in_VS_Code|VS Code Extension]]: Inline diffs and editor integration.
- [[JetBrains_IDEs|JetBrains Integration]]: IntelliJ, PyCharm, and WebStorm support.
- [[Use_Claude_Code_with_Chrome|Chrome Integration]]: Browser automation, DOM testing, and console log capture.
- [[Let_Claude_use_your_computer_from_the_CLI|Computer Use]]: GUI desktop automation from terminal.
- [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]: Controlling terminal sessions from web/mobile.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Agent_SDK|Agent SDK]]
- [[Matrix_Agentic_Coordination|Agentic Coordination Matrix]]

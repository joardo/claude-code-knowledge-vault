---
title: "MOC: Lifecycle Hooks & Event Automation"
aliases:
  - "MOC_Hooks_and_Automation"
tags:
  - "claude-code"
  - "moc"
  - "hooks"
  - "automation"
status: "verified"
last_updated: "2026-10"
---

# MOC: Lifecycle Hooks & Event Automation

> Deterministic control planes: lifecycle hooks, push notification channels, and recurring background scheduling.

## 1. Lifecycle Hooks
- [[Automate_actions_with_hooks|Automate Actions with Hooks]]: Practical guide to triggering shell scripts, linters, notifications, and validators.
- [[Hooks_reference|Hooks Reference]]: Exhaustive reference for all hook events (`PreToolUse`, `PostToolUse`, `Prompt`, `Stop`), JSON input/output schemas, exit codes, and async hooks.

## 2. Channels (Push Events into Sessions)
- [[Push_events_into_a_running_session_with_channels|Push Events with Channels Guide]]: Ingesting external events (webhooks, alerts, chat) into live sessions.
- [[Channels_reference|Channels Reference]]: The MCP channel contract, notification events, and reply tools.

## 3. Scheduling & Background Loops
- [[Run_prompts_on_a_schedule|Run Prompts on a Schedule]]: Scheduling recurring checks with `/loop`, cron expressions, and timers.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns]]
- [[Matrix_Extensibility|Extensibility Matrix]]

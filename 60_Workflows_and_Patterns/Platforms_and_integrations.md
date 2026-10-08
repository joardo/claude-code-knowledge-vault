---
title: "Platforms and integrations"
aliases:
  - "platforms"
  - "Platforms and integrations"
tags:
  - "claude-code"
  - "workflows"
source_url: "https://code.claude.com/docs/en/platforms"
status: "verified"
last_updated: "2026-10"
---

# Platforms and integrations

## Executive Summary
> Choose where to run Claude Code and what to connect it to. Compare the CLI, Desktop, VS Code, JetBrains, web, mobile, and integrations like Chrome, Slack, and CI/CD.

## Technical Mechanics & Documentation

Claude Code runs the same underlying engine everywhere, but each surface is tuned for a different way of working. This page helps you pick the right platform for your workflow and connect the tools you already use.

## Where to run Claude Code

Choose a platform based on how you like to work and where your project lives.

| Platform | Best for | What you get |
| :- | :- | :- |
| [[Quickstart|CLI]] | Terminal workflows, scripting, remote servers | Full feature set, [[Run_Claude_Code_programmatically|Agent SDK]], [[Let_Claude_use_your_computer_from_the_CLI|computer use]] on macOS (Pro and Max), third-party providers |
| [[Desktop_application|Desktop]] | Visual review, parallel sessions, managed setup | Diff viewer, app preview, [[Desktop_application|computer use]] and [[Desktop_application|Dispatch]] on Pro and Max |
| [[Use_Claude_Code_in_VS_Code|VS Code]] | Working inside VS Code without switching to a terminal | Inline diffs, integrated terminal, file context |
| [[JetBrains_IDEs|JetBrains]] | Working inside IntelliJ, PyCharm, WebStorm, or other JetBrains IDEs | Diff viewer, selection sharing, terminal session |
| [[Use_Claude_Code_in_the_cloud|Web]] | Long-running tasks that don't need much steering, or work that should continue when you're offline | Cloud, Anthropic-managed by default; continues after you disconnect |
| [[Claude_Code_on_mobile|Mobile]] | Starting and monitoring tasks while away from your computer | Cloud sessions from the Claude app for iOS and Android, [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] for local sessions, [[Desktop_application|Dispatch]] to Desktop on Pro and Max |

The CLI is the most complete surface for terminal-native work: scripting and the Agent SDK are CLI-only. Third-party providers also work in [[Use_Claude_Code_in_VS_Code|VS Code]] and in [[Feature_availability|JetBrains]], which runs the CLI in your IDE's terminal. Enterprise [[Desktop_application|Desktop]] deployments support Google Cloud's Agent Platform, and Desktop supports [[Connect_Claude_Code_to_an_LLM_gateway|gateway providers]]; for Amazon Bedrock or Microsoft Foundry, use the CLI or an IDE extension, or [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview), which runs the Code tab on those providers. Desktop and the IDE extensions trade some CLI-only features for visual review and tighter editor integration. The web runs in the cloud, so tasks keep going after you disconnect. Mobile is a thin client into those same cloud sessions or into a local session via Remote Control, and can send tasks to Desktop with Dispatch.

You can mix surfaces on the same project. Configuration, project memory, and MCP servers are shared across the local surfaces.

## Connect your tools

Integrations let Claude work with services outside your codebase.

| Integration | What it does | Use it for |
| :- | :- | :- |
| [[Use_Claude_Code_with_Chrome|Chrome]] | Controls your browser with your logged-in sessions | Testing web apps, filling forms, automating sites without an API |
| [[Claude_Code_GitHub_Actions|GitHub Actions]] | Runs Claude in your CI pipeline | Automated PR reviews, issue triage, scheduled maintenance |
| [[Claude_Code_GitLab_CICD|GitLab CI/CD]] | Same as GitHub Actions for GitLab | CI-driven automation on GitLab |
| [[Code_Review|Code Review]] | Reviews every PR automatically | Catching bugs before human review |
| [[Claude_Code_in_Slack|Slack]] | Responds to `@Claude` mentions in your channels, under your own account | Turning bug reports into pull requests from team chat on Pro and Max plans |
| [Claude Tag](https://claude.com/docs/claude-tag) | Runs `@Claude` as your organization's shared identity with admin-configured access | Shared team access on Team and Enterprise plans, instead of per-user Slack sessions |

For integrations not listed here, [[Connect_Claude_Code_to_tools_via_MCP|MCP servers]] and [[Desktop_application|connectors]] let you connect almost anything: Linear, Notion, Google Drive, or your own internal APIs.

## Work when you are away from your terminal

Claude Code offers several ways to work when you're not at your terminal. They differ in what triggers the work, where Claude runs, and how much you need to set up.

| | Trigger | Claude runs on | Setup | Best for |
| :- | :- | :- | :- | :- |
| [[Desktop_application|Dispatch]] | Message a task from the Claude mobile app | Your machine (Desktop) | [Pair the mobile app with Desktop](https://support.claude.com/en/articles/13947068) | Delegating work while you're away, minimal setup |
| [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] | Drive a running session from [claude.ai/code](https://claude.ai/code) or the Claude mobile app | Your machine (CLI, Desktop, or VS Code) | Run [[Continue_local_sessions_from_any_device_with_Remote_Control|`claude remote-control` or `/remote-control`]] | Steering in-progress work from another device |
| [[Push_events_into_a_running_session_with_channels|Channels]] | Push events from a chat app like Telegram or Discord, or your own server | Your machine (CLI) | [[Push_events_into_a_running_session_with_channels|Install a channel plugin]] or [[Channels_reference|build your own]] | Reacting to external events like CI failures or chat messages |
| [[Claude_Code_in_Slack|Slack]] | Mention `@Claude` in a team channel | Anthropic cloud | [[Claude_Code_in_Slack|Install the Slack app]] with [[Use_Claude_Code_in_the_cloud|Claude Code on the web]] enabled, on Pro and Max plans | PRs and reviews from team chat |
| [[Self-hosted_environments|Self-hosted environments]] | Start a [[Use_Claude_Code_in_the_cloud|cloud session]] and pick your organization's environment | Your organization's infrastructure | [[Self-hosted_environments_quickstart|Deploy runners]], on Team and Enterprise plans | Cloud sessions that must run inside your network |
| [[Run_prompts_on_a_schedule|Scheduled tasks]] | Set a schedule | [[Run_prompts_on_a_schedule|CLI]], [[Schedule_recurring_tasks_in_Claude_Code_Desktop|Desktop]], or [[Automate_work_with_routines|cloud]] | Pick a frequency | Recurring automation like daily reviews |

If you're not sure where to start, [[Quickstart|install the CLI]] and run it in a project directory. If you'd rather not use a terminal, [[Get_started_with_the_desktop_app|Desktop]] gives you the same engine with a graphical interface.

## Related resources

### Platforms

* [[Quickstart|CLI quickstart]]: install and run your first command in the terminal
* [[Desktop_application|Desktop]]: visual diff review, parallel sessions, computer use, and Dispatch
* [[Use_Claude_Code_in_VS_Code|VS Code]]: the Claude Code extension inside your editor
* [[JetBrains_IDEs|JetBrains]]: the extension for IntelliJ, PyCharm, and other JetBrains IDEs
* [[Use_Claude_Code_in_the_cloud|Web]]: cloud sessions from your browser at claude.ai/code that keep running when you disconnect
* [[Let_Claude_coordinate_ongoing_work_with_Projects|Projects]]: one conversation where Claude coordinates many cloud sessions for a body of work and reports back
* [[Claude_Code_on_mobile|Mobile]]: the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) for starting and monitoring tasks while away from your computer

### Integrations

* [[Use_Claude_Code_with_Chrome|Chrome]]: automate browser tasks with your logged-in sessions
* [[Let_Claude_use_your_computer_from_the_CLI|Computer use]]: let Claude open apps and control your screen on macOS
* [[Claude_Code_GitHub_Actions|GitHub Actions]]: run Claude in your CI pipeline
* [[Claude_Code_GitLab_CICD|GitLab CI/CD]]: the same for GitLab
* [[Code_Review|Code Review]]: automatic review on every pull request
* [[Claude_Code_in_Slack|Slack]]: send tasks from team chat and get PRs back, on Pro and Max plans
* [Claude Tag](https://claude.com/docs/claude-tag): run `@Claude` as your organization's shared identity on Team and Enterprise plans

### Remote access

* [[Desktop_application|Dispatch]]: message a task from your phone and it can spawn a Desktop session
* [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]: drive a running session from your phone or browser
* [[Push_events_into_a_running_session_with_channels|Channels]]: push events from chat apps or your own servers into a session
* [[Run_prompts_on_a_schedule|Scheduled tasks]]: run prompts on a recurring schedule

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

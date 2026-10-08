---
title: "Claude Code on mobile"
aliases:
  - "mobile"
  - "Claude Code on mobile"
tags:
  - "claude-code"
  - "workflows"
source_url: "https://code.claude.com/docs/en/mobile"
status: "verified"
last_updated: "2026-10"
---

# Claude Code on mobile

## Executive Summary
> Start, monitor, and steer Claude Code tasks from your phone with the Claude app for iOS and Android.

## Technical Mechanics & Documentation

The Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) is a client for Claude Code sessions rather than a place where code runs. From your phone you reach [cloud sessions](#start-and-monitor-cloud-sessions) and [[Let_Claude_coordinate_ongoing_work_with_Projects|projects]] in the cloud, a session running on your own machine through [Remote Control](#continue-a-local-session-with-remote-control), or the Desktop app through [[Desktop_application|Dispatch]].

<Note>
  Claude Code doesn't have a separate mobile app: cloud sessions and Remote Control both live in the **Code** tab in the Claude app, and Dispatch is a task you message in the app.
</Note>

## Get the app

<Steps>
  <Step title="Download the Claude app">
    Install the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) or [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude). On an iPad, install the same iOS app.

    <Tip>
      Run `/mobile` in a Claude Code session to show a QR code for [claude.ai/mobile](https://claude.ai/mobile), which opens the right app store for your phone. `/ios` and `/android` do the same thing.
    </Tip>
  </Step>

  <Step title="Sign in">
    Sign in with the same claude.ai account and organization you use for Claude Code. Cloud sessions and Remote Control require a claude.ai account, so they aren't reachable with an Anthropic Console API key or from a third-party provider such as Amazon Bedrock.
  </Step>

  <Step title="Open the Code tab">
    Tap **Code** in the app's navigation to reach your sessions, or open [claude.ai/code/new](https://claude.ai/code/new) on your phone to start a new Code session in the app. If you don't see the Code tab, your plan or organization may not include these features; see [[Feature_availability|availability by subscription plan]].
  </Step>
</Steps>

## Work from your phone

From the app you can start cloud sessions, open a project, drive a Claude Code session running on your computer, or message Dispatch a task. The app is the same for each; they differ in where the work happens.

| Feature | What you connect to | When to use |
| :- | :- | :- |
| [[Use_Claude_Code_in_the_cloud|Cloud sessions]] | A session on cloud infrastructure, Anthropic-managed by default | Your repository is on GitHub and the task should keep running after you put your phone away. See the [[Get_started_with_Claude_Code_in_the_cloud|cloud quickstart]] to set up. |
| [[Let_Claude_coordinate_ongoing_work_with_Projects|Projects]] | A conversation where Claude coordinates parallel threads of work and reports back | You have a stream of related work rather than one task and want to see which threads finished or need you. |
| [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] | A Claude Code session running on your computer | The work needs your local filesystem, tools, or MCP servers. |
| [[Desktop_application|Dispatch]] | The Desktop app on your computer | You want to message a task and let Dispatch decide how to run it. Requires a Pro or Max plan. |

If your computer will be off, use cloud sessions or a project, which run in the cloud and continue with your laptop closed. Remote Control and Dispatch drive your own machine, so it needs to stay on with Claude Code or the Desktop app running. If your machine sleeps during a Remote Control session, Claude Code reconnects when the machine comes back online.

For a fuller comparison, see [[Platforms_and_integrations|work when you are away from your terminal]].

Cloud sessions and Remote Control run from the **Code** tab. For Dispatch, which you message as a task in the app, see [[Desktop_application|sessions from Dispatch]].

### Start and monitor cloud sessions

Cloud sessions run tasks on cloud infrastructure, Anthropic-managed by default, so a session continues after you put your phone away. From the Code tab, select a repository and branch, describe the task, and submit it. Sessions persist across devices: a task you start on your laptop is ready to review from your phone, and one you start from your phone is waiting when you're back at your desk.

Open a session in the app to check progress, answer Claude's questions, or steer it in a new direction. You can also tell Claude to [[Use_Claude_Code_in_the_cloud|watch a pull request]] and fix CI failures or review comments as they arrive. To connect GitHub and set up your environment, follow the [[Get_started_with_Claude_Code_in_the_cloud|cloud quickstart]], and see [[Use_Claude_Code_in_the_cloud|Use Claude Code in the cloud]] for everything cloud sessions can do.

### Continue a local session with Remote Control

Remote Control connects the Claude app to a Claude Code session running on your machine, so code execution and filesystem access stay local while you drive the session from your phone. Start the session on your computer with `claude remote-control`, or run `/remote-control` in a session that's already open. Then scan the QR code the terminal can display, or open the Claude app, tap **Code**, and pick the session from the list. See [[Continue_local_sessions_from_any_device_with_Remote_Control|connect from another device]] for each option.

When you add an attachment in the Claude app, it reaches the local session too:

* **Photos**: Claude sees attached photos directly as part of your message. Claude Code also saves each photo under `~/.claude/uploads/` and tells Claude the saved file path, so Claude can copy the image into files it creates.
* **Other files**: Claude Code downloads them to your machine and passes them to Claude as `@` file references.

For requirements, invocation modes, and troubleshooting, see the [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control overview]].

### Get push notifications

When Remote Control is active, Claude can send push notifications to your phone, typically when a long-running task finishes or when it needs a decision from you. You can also ask for one in your prompt, such as `notify me when the tests finish`. See [[Continue_local_sessions_from_any_device_with_Remote_Control|mobile push notifications]] for the two `/config` toggles and delivery troubleshooting.

Dispatch sends its own notification when a Code session it spawned finishes or needs your approval, described in [[Desktop_application|sessions from Dispatch]].

## Limitations

The mobile client covers most of what a session needs, with a few limitations:

* **Local-only commands**: commands that only run in the terminal interface, such as `/plugin` and `/resume`, don't work from the app. The [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control limitations]] list the commands that do work from mobile and how their behavior differs.
* **Permission modes**: cloud sessions offer Accept edits, Plan, and Auto, and Remote Control sessions offer Manual, Accept edits, Plan, and Auto. You can't select Bypass permissions from the app in either case. See [[Choose_a_permission_mode|switch permission modes]] for when Auto is available.
* **Dispatch plans**: Dispatch requires a Pro or Max plan and isn't available on Team or Enterprise.

## Related resources

* [[Platforms_and_integrations|Platforms and integrations]]: compare every surface Claude Code runs on
* [[Use_Claude_Code_in_the_cloud|Use Claude Code in the cloud]]: how cloud sessions run and how to move work to and from your terminal
* [[Configure_cloud_environments|Configure cloud environments]]: network access levels, environment variables, and setup scripts for cloud sessions
* [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]: continue a local session from any device
* [[Desktop_application|Sessions from Dispatch]]: how Dispatch tasks become Code sessions in the Desktop app
* [[Push_events_into_a_running_session_with_channels|Channels]]: ask Claude something from your phone via Telegram, Discord, or iMessage while the work runs on your machine
* [[Claude_Code_in_Slack|Claude Code in Slack]]: delegate coding tasks from your Slack workspace by mentioning `@Claude`

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

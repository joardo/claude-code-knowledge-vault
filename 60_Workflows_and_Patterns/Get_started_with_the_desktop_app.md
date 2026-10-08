---
title: "Get started with the desktop app"
aliases:
  - "desktop-quickstart"
  - "Get started with the desktop app"
tags:
  - "claude-code"
  - "workflows"
source_url: "https://code.claude.com/docs/en/desktop-quickstart"
status: "verified"
last_updated: "2026-10"
---

# Get started with the desktop app

## Executive Summary
> Install the Claude desktop app, open the Code tab, and start your first Claude Code session on a project folder on your computer.

## Technical Mechanics & Documentation

The desktop app gives you Claude Code with a graphical interface, so you can ask Claude to work on the code in a folder on your computer and review its changes without using a terminal. This page walks through installing the app and starting your first session in the **Code** tab. Claude Code requires a [Pro, Max, Team, or Enterprise subscription](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=desktop_quickstart_pricing).


  <Card title="Download for macOS" icon="apple" href="https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs">
    Universal build for Intel and Apple Silicon
  </Card>

  <Card title="Download for Windows" icon="windows" href="https://claude.ai/api/desktop/win32/x64/setup/latest/redirect?utm_source=claude_code&utm_medium=docs">
    For x64 processors
  </Card>

  - [[Claude_Desktop_on_Linux_beta|Get Claude for Linux (beta)]]: apt or .deb for Ubuntu and Debian


For Windows ARM64, download the [ARM64 installer](https://claude.ai/api/desktop/win32/arm64/setup/latest/redirect?utm_source=claude_code\&utm_medium=docs). On Linux, install with apt; see [[Claude_Desktop_on_Linux_beta|Claude Desktop on Linux]].

<Note>
  These cases are covered on other pages:

  * **Already set up**: see [[Desktop_application|Use Claude Code Desktop]] for everything the Code tab can do
  * **Want `claude` in your terminal**: [[Quickstart|install the CLI]] separately
</Note>

The desktop app has three tabs:

* **Chat**: General conversation with no file access, similar to claude.ai.
* **Cowork**: An autonomous background agent that works on tasks independently while you do other work.
* **Code**: An interactive coding assistant with direct access to your local files. Depending on the permission mode, you approve each change as Claude proposes it or review the changes after Claude makes them.

Chat and Cowork are covered in the [Claude Help Center](https://support.claude.com/); installing and deploying the desktop app is covered in the [Claude Desktop support articles](https://support.claude.com/en/collections/16163169-claude-desktop). This page focuses on the **Code** tab.

## Install

<Steps>
  <Step title="Install and sign in">
    On macOS and Windows, download the installer from the links above and run it. On Linux, follow the install steps in [[Claude_Desktop_on_Linux_beta|Claude Desktop on Linux]]. Launch Claude from your Applications folder on macOS, the Start menu on Windows, or your application launcher on Linux, then sign in with your Anthropic account.
  </Step>

  <Step title="Open the Code tab">
    Click the **Code** tab at the top center. If clicking Code prompts you to upgrade, you need to [subscribe to a paid plan](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=desktop_quickstart_upgrade) first. If it prompts you to sign in online, complete the sign-in and restart the app. If you see a 403 error, see [[Desktop_application|authentication troubleshooting]].
  </Step>
</Steps>

The desktop app includes Claude Code, so you don't need to install Node.js or the CLI to use the Code tab.

## Start your first session

With the Code tab open, choose a project and give Claude something to do.

<Steps>
  <Step title="Choose an environment and folder">
    Select **Local** to run Claude on your machine using your files directly. Click **Select folder** and choose your project directory.

    <Tip>
      Start with a small project you know well. It's the fastest way to see what Claude Code can do.
    </Tip>

    You can also select:

    * **Cloud**: Run sessions in the cloud that continue even if you close the app. See [[Use_Claude_Code_in_the_cloud|Use Claude Code in the cloud]] for how cloud sessions work.
    * **SSH**: Connect to a remote machine over SSH, such as your own servers, cloud VMs, or dev containers. Desktop installs Claude Code on the remote machine automatically the first time you connect.
    * **WSL** (Windows): Run the session inside a [[Claude_Code_Desktop_in_WSL|WSL 2 distribution]]; Claude Code, tools, and git execute on the Linux side with native paths.
  </Step>

  <Step title="Choose a model">
    Select a model from the dropdown next to the send button. See [[Model_configuration|models]] for a comparison of the available models. You can change the model later from the same dropdown.
  </Step>

  <Step title="Tell Claude what to do">
    Type what you want Claude to do:

    * `Find a TODO comment and fix it`
    * `Add tests for the main function`
    * `Create a CLAUDE.md with instructions for this codebase`

    A [[Desktop_application|session]] is a conversation with Claude about your code. Each session tracks its own context and changes.
  </Step>

  <Step title="Review and accept changes">
    What happens next depends on the [[Desktop_application|permission mode]] shown in the selector next to the send button:

    * **Auto or Accept edits**: Claude applies its file changes, and an indicator such as `+12 -1` appears so you can review them in the diff view
    * **Manual**: Claude proposes each change and waits for your approval before applying it. Your files aren't modified until you accept, and if you reject a change, Claude asks how you'd like to proceed instead

    In Manual mode, you'll see:

    1. A [[Desktop_application|diff view]] showing exactly what will change in each file
    2. Accept/Reject buttons to approve or decline each change
    3. Real-time updates as Claude works through your request
  </Step>
</Steps>

## Now what?

You've made your first edit. For the full reference on everything Desktop can do, see [[Desktop_application|Use Claude Code Desktop]]. Here are some things to try next.

**Interrupt and steer.** You can redirect Claude at any point. Click the stop button to interrupt immediately, or type a correction and press **Enter** to send it without stopping the running action. Either way, you don't have to wait for it to finish or start over.

**Give Claude more context.** Type `@filename` in the prompt box to pull a specific file into the conversation, attach images and PDFs using the attachment button, or drag and drop files directly into the prompt. The more context Claude has, the better the results. See [[Desktop_application|Add files and context]].

**Use skills for repeatable tasks.** Type `/` or click **+** → **Slash commands** to browse [[Commands|built-in commands]], [[Extend_Claude_with_skills|custom skills]], and plugin skills. Skills are reusable prompts you can invoke whenever you need them, like code review checklists or deployment steps.

**Review changes before committing.** After Claude edits files, a `+12 -1` indicator appears. Click it to open the [[Desktop_application|diff view]], review modifications file by file, and comment on specific lines. Claude reads your comments and revises. To have Claude review the changes itself, enter [[Desktop_application|`/code-review`]] in the prompt box.

**Adjust how much control you have.** Your [[Desktop_application|permission mode]] sets how much Claude can do without asking for approval:

* **Auto**: a classifier reviews actions in the background and blocks the risky ones instead of asking you.
* **Manual**: Claude asks before editing files or running commands.
* **Accept edits**: Claude auto-accepts file edits for faster iteration.
* **Plan**: Claude proposes an approach without editing any files, which is useful before a large refactor.

**Add plugins for more capabilities.** Click the **+** button next to the prompt box and select **Plugins** to browse and install [[Desktop_application|plugins]] that add skills, agents, MCP servers, and more.

**Arrange your workspace.** Drag the chat, diff, terminal, file, and browser panes into whatever layout you want. Open the terminal with **Ctrl+\`** to run commands alongside your session, or click a file path to open it in the file pane. See [[Desktop_application|Arrange your workspace]].

**Preview your app.** When you run your dev server in the desktop, your app opens in the Browser pane, which can also [[Desktop_application|open external sites]]. Claude can view the running app, test endpoints, inspect logs, and iterate on what it sees. See [[Desktop_application|Preview your app]].

**Track your pull request.** After opening a PR, Claude Code monitors CI check results and can automatically fix failures or merge the PR once all checks pass. See [[Desktop_application|Monitor pull request status]].

**Put Claude on a schedule.** Set up [[Schedule_recurring_tasks_in_Claude_Code_Desktop|scheduled tasks]] to run Claude automatically on a recurring basis: a daily code review every morning, a weekly dependency audit, or a briefing that pulls from your connected tools.

**Scale up when you're ready.** Open [[Desktop_application|parallel sessions]] from the sidebar to work on multiple tasks at once, optionally each in its own Git worktree, and open the [[Desktop_application|tasks pane]] to watch the subagents and background commands a session has running. Open a [[Desktop_application|side chat]] to ask a question without derailing the main thread. Send [[Desktop_application|long-running work to the cloud]] so it continues even if you close the app, or [[Desktop_application|move a session you already started to the cloud]] if a task takes longer than expected. [[Desktop_application|Connect external tools]] like GitHub, Slack, and Linear to bring your workflow together.

## What's next

* [[Desktop_application|Use Claude Code Desktop]]: permission modes, parallel sessions, diff view, connectors, and enterprise configuration
* [[Desktop_application|Coming from the CLI?]]: run Desktop and the CLI on the same project, and compare features, flag equivalents, and what's not available in Desktop
* [[Desktop_application|Troubleshooting]]: solutions to common errors and setup issues
* [[Best_practices_for_Claude_Code|Best practices]]: tips for writing effective prompts and getting the most out of Claude Code
* [[Common_workflows|Common workflows]]: tutorials for debugging, refactoring, testing, and more

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

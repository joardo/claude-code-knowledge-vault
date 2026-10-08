---
title: "Glossary"
aliases:
  - "glossary"
  - "Glossary"
tags:
  - "claude-code"
  - "workflows"
source_url: "https://code.claude.com/docs/en/glossary"
status: "verified"
last_updated: "2026-10"
---

# Glossary

## Executive Summary
> Definitions for Claude Code terminology. Learn what agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP, and other core concepts mean.

## Technical Mechanics & Documentation

This glossary defines Claude Code terminology. Each entry links to the page where the concept is covered in depth. For model-level concepts like tokens, temperature, and RAG, see the [platform glossary](https://platform.claude.com/docs/en/about-claude/glossary). For Claude Desktop terms such as desktop extension, MCPB, and DXT, see the [Claude Help Center](https://support.claude.com/).

## A

### AGENTS.md

A markdown file of project instructions you write for AI coding agents. If your repository has one and no [CLAUDE.md](#claude-md), Claude reads it as your project instructions without you adding a second file. You can change the **Project instructions** setting in `/config` to have Claude read both files or only `CLAUDE.md`. Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later. In some sessions Claude [[How_Claude_remembers_your_project|can't read `AGENTS.md`]], so [[How_Claude_remembers_your_project|import it from a `CLAUDE.md`]] there instead.

Learn more: [[How_Claude_remembers_your_project|AGENTS.md]]

### Agent teams

Multiple independent Claude Code sessions coordinated by a team lead, with a shared task list and peer-to-peer messaging. Unlike [subagents](#subagent), which run within a single session and report only to the parent, teammates each have their own context window and you can interact with any of them directly. Agent teams are experimental and disabled by default; see [[Orchestrate_teams_of_Claude_Code_sessions|Enable agent teams]].

Learn more: [[Orchestrate_teams_of_Claude_Code_sessions|Run agent teams]]

### Agentic coding

A workflow where the AI can read files, run commands, and make changes autonomously while you watch, redirect, or step away, as opposed to chat-based assistants that only respond with text you must apply yourself. Claude Code is agentic because it has [tools](#tool) that let it act, not just advise.

Learn more: [[How_Claude_Code_works|How Claude Code works]]

### Agentic harness

The tools, context management, and execution environment that turn a language model into a capable coding agent. Claude Code is the harness; Claude is the model inside it. The harness supplies file access, shell execution, permission gating, memory loading, and the loop that chains actions together.

Learn more: [[How_Claude_Code_works|How Claude Code works]]

### Agentic loop

The cycle Claude works through for every task: gather context, take action, verify results, and repeat until done. Each tool use returns information that informs the next step. You can interrupt the loop at any point to redirect. Most extension points, including [hooks](#hook), [skills](#skill), and [MCP](#mcp-model-context-protocol), plug into specific phases of this loop.

Learn more: [[How_Claude_Code_works|How Claude Code works]]

### Artifact

A live, interactive web page Claude Code publishes from your session to a private URL on claude.ai, so you can see output visually or share it instead of reading terminal text. The page updates in place when the session republishes. Artifacts you create from Claude Code appear in the same gallery as artifacts created in claude.ai conversations. Sharing options depend on your plan: see [[Share_session_output_as_artifacts|Share an artifact]].

Learn more: [[Share_session_output_as_artifacts|Share session output as artifacts]]

### Auto memory

Notes Claude writes for itself based on your corrections and preferences, stored per git repository under `~/.claude/projects/`. All worktrees of the same repository share one auto memory directory. The first 200 lines or 25 KB of the `MEMORY.md` index loads at the start of every session. Auto memory is the Claude-written counterpart to [CLAUDE.md](#claude-md), which you write.

Learn more: [[How_Claude_remembers_your_project|Auto memory]]

### Auto mode

A [permission mode](#permission-mode) where a separate classifier model reviews actions instead of you, so Claude Code runs most of them without asking you. Claude Code still asks you before actions your explicit ask rules match. With Claude Code v2.1.283 or later, auto mode is the [[Choose_a_permission_mode|built-in starting permission mode]] for interactive terminal and VS Code sessions, and on earlier versions only on Pro, Max, and Team plans. The classifier blocks scope escalation, untrusted infrastructure, and [prompt injection](#prompt-injection). Tool results are stripped from what it sees, so hostile content in a file or web page can't manipulate it directly.

Learn more: [[Choose_a_permission_mode|Eliminate prompts with auto mode]]

## B

### Bare mode

With `--bare`, Claude Code starts without loading hooks, skills, custom commands, subagents, installed plugins, MCP servers, auto memory, or CLAUDE.md, apart from skills in a directory you pass with `--add-dir`. Recommended for CI and scripted calls where you need the same result on every machine.

Learn more: [[Run_Claude_Code_programmatically|Start faster with bare mode]]

### Bundled skills

Prompt-based playbooks included with Claude Code, such as `/batch`, `/code-review`, `/debug`, and `/loop`. Unlike built-in commands, which execute fixed logic, bundled skills give Claude a detailed prompt and let it orchestrate the work, so they can spawn agents, read files, and adapt to your codebase.

Learn more: [[Extend_Claude_with_skills|Bundled skills]]

## C

### Channel

An [MCP server](#mcp-model-context-protocol) that pushes events into your running session so Claude can react to things that happen while you're away from the terminal. Channels can be two-way: Claude reads an inbound event and replies back through the same channel. Telegram, Discord, and iMessage are included in the research preview.

Learn more: [[Push_events_into_a_running_session_with_channels|Channels]]

### Checkpoint

A restore point created at each prompt you send that starts a turn. Claude Code snapshots files before every edit so a checkpoint can revert them. Press `Esc` twice or run `/rewind` to restore code, conversation, or both to an earlier point, or to summarize part of the conversation from a selected message. Checkpoints are saved with the conversation, so a resumed session can still `/rewind` to them. They're separate from git and don't track changes made through the Bash tool.

Learn more: [[Checkpointing]]

### `.claude` directory

The directory where Claude Code reads project-scoped configuration: settings, hooks, skills, subagents, rules, and auto memory. A project has `.claude/` at its root; your user-level defaults are at `~/.claude/`.

Learn more: [[Explore_the_claude_directory|The `.claude` directory]]

### CLAUDE.md

A markdown file of persistent instructions you write for Claude, loaded at the start of every session as a user message after the system prompt. Put project conventions, architecture notes, and "always do X" rules here. Project-root CLAUDE.md survives [compaction](#compaction) and is re-read fresh from disk afterward.

You can place CLAUDE.md at project scope in `./CLAUDE.md` or `./.claude/CLAUDE.md`, at user scope in `~/.claude/CLAUDE.md`, or as [managed policy](#managed-settings) for your organization. All discovered files are concatenated into context rather than overriding each other, ordered from broadest scope to most specific. Claude Code can also load a project's [AGENTS.md](#agents-md) files in place of CLAUDE.md.

Learn more: [[How_Claude_remembers_your_project|CLAUDE.md files]]

### Cloud session

A Claude Code session that keeps running after you close your laptop, because it runs on cloud infrastructure instead of your machine: Anthropic-managed by default, or a [[Self-hosted_environments|self-hosted environment]] your organization operates. You start one from claude.ai/code, the Claude mobile app, the Desktop app with **Cloud** selected, `claude --cloud`, or a [[Automate_work_with_routines|routine]]. A session in your terminal, IDE, or the Desktop app with **Local** selected is a local session; to reach a local session from another device, use [Remote Control](#remote-control).

Learn more: [[Use_Claude_Code_in_the_cloud|Use Claude Code in the cloud]]

### Command

A reusable instruction you invoke by typing `/name` in the prompt. Built-in commands such as `/clear`, `/model`, and `/compact` control the session. You can define your own commands as files in `.claude/commands/`, or install them from a [plugin](#plugin). [Skills](#skill) are the recommended way to package multi-step commands.

Two other uses of the word are unrelated: `claude` CLI subcommands such as `claude mcp add`, listed in the [[CLI_reference|CLI reference]], and the `command` field of a stdio [MCP server](#mcp-server) entry, which specifies the executable Claude Code launches to start the server.

Learn more: [[Commands]] · [[Extend_Claude_with_skills|Skills]]

### Compaction

Automatic summarization of your conversation when the [context window](#context-window) approaches its limit. Older tool outputs are cleared first, then the conversation is summarized. Project-root CLAUDE.md and auto memory survive compaction and reload from disk; instructions given only in conversation may be lost. Run `/compact` to trigger manually, optionally with a focus like `/compact focus on the API changes`.

Learn more: [[Explore_the_context_window|What survives compaction]] · [[How_Claude_Code_works|When context fills up]]

### Connector

An [MCP server](#mcp-server) added to your claude.ai account rather than configured in Claude Code. When you sign in to Claude Code with that account, your connectors appear in `/mcp` alongside the servers you added locally. Organizations can also provision connectors and set per-tool controls on them.

Learn more: [[Connect_Claude_Code_to_tools_via_MCP|Use MCP servers from claude.ai]]

### Context window

The working memory for a session, holding conversation history, file contents, command outputs, CLAUDE.md, auto memory, loaded skills, and system instructions. As you work, context fills up until [compaction](#compaction) summarizes it. Run `/context` to see what's using space. For the underlying model concept, see the [platform glossary](https://platform.claude.com/docs/en/about-claude/glossary#context-window).

Learn more: [[Explore_the_context_window|Explore the context window]]

## D

### Dispatch

A phone-initiated task router that spawns a Claude Code session in the Desktop app when you send a coding task from the Claude mobile app. Your prompt routes to the right tool automatically. Available on Pro and Max plans.

Learn more: [[Desktop_application|Sessions from Dispatch]]

## E

### Effort level

A setting that controls adaptive reasoning, which lets the model decide whether and how much to think on each step. Higher effort means more thinking tokens and deeper reasoning; lower effort is faster and cheaper. Effort is supported on Fable models, on Opus 4.6 and later, on Sonnet 4.6 and later, and on Haiku 5.5.

Learn more: [[Model_configuration|Adjust effort level]]

### Extended thinking

Visible step-by-step reasoning the model performs before responding. You can adjust it with the [effort level](#effort-level), or cap thinking tokens with `MAX_THINKING_TOKENS` on models with a fixed thinking budget. Thinking appears in gray italic text in the terminal.

Learn more: [[Model_configuration|Use extended thinking]]

## F

### Frontmatter

A block of YAML settings at the very top of a Markdown file, between an opening `---` line and a closing `---` line. Skills, subagents, output styles, and rules each read their configuration from frontmatter, such as a skill's `description` or a subagent's `tools`, and treat everything after the closing `---` as the instructions. The opening `---` must be the file's first line. Each file type accepts its own set of fields.

Learn more: [[Extend_Claude_with_skills|Skill frontmatter]], [[Create_custom_subagents|Subagent frontmatter]], [[Output_styles|Output style frontmatter]], [[How_Claude_remembers_your_project|Rule frontmatter]]

## H

### Hook

A user-defined handler that executes automatically at a specific point in Claude Code's lifecycle, such as before a tool runs, after a file edit, or at session start. Handlers can be a shell command, HTTP endpoint, MCP tool, LLM prompt, or subagent. Hooks are deterministic: they fire at fixed lifecycle points rather than at the model's discretion.

A hook configuration has three levels:

* **Hook event**: the lifecycle point
* **Matcher**: filters which events fire it
* **Hook handler**: what runs

Learn more: [[Automate_actions_with_hooks|Get started with hooks]] · [[Hooks_reference|Hooks reference]]

## M

### Managed settings

Settings enforced org-wide by IT or DevOps, delivered from Anthropic's servers through the admin console or deployed to devices at an OS-level path outside `~/.claude`. User and project settings cannot override managed settings. Server-managed delivery applies on [[Configure_server-managed_settings|eligible configurations]]; see [[Configure_server-managed_settings|Security considerations]]. Use this for security policies, compliance requirements, or standardized tooling across a fleet.

Learn more: [[Configure_server-managed_settings|Server-managed settings]] · [[Settings_files_and_precedence|Settings files]]

### MCP (Model Context Protocol)

An open standard for connecting AI tools to external data sources and services. MCP servers give Claude new tools for Slack, Jira, databases, browsers, and hundreds of other integrations. You connect servers via `/mcp` or by adding them to `.mcp.json`. For the protocol itself, see the [platform glossary](https://platform.claude.com/docs/en/about-claude/glossary#mcp-model-context-protocol).

Learn more: [[Connect_Claude_Code_to_tools_via_MCP|Model Context Protocol]]

### MCP server

A program that gives Claude tools, prompts, or resources over [MCP](#mcp-model-context-protocol). You add servers with `claude mcp add`, in `.mcp.json`, through a [plugin](#plugin), or as a claude.ai [connector](#connector). A local stdio server runs as a process Claude Code starts from the `command` and `args` fields of its configuration, which have nothing to do with the [commands](#command) you type at the prompt.

Learn more: [[Connect_Claude_Code_to_tools_via_MCP|Model Context Protocol]]

### MCP Tool Search

A context-saving mechanism that defers MCP tool schemas until needed. Only tool names and server instructions load at startup; Claude fetches the full schema on demand when it decides to use a specific tool. This keeps idle MCP servers from consuming much context.

Learn more: [[Connect_Claude_Code_to_tools_via_MCP|Scale with MCP Tool Search]]

## N

### Non-interactive mode

A mode that executes a single prompt and exits without an interactive prompt, invoked with `-p` or `--print`. Used for CI, scripts, and piping. The run is still saved as a resumable session unless you pass `--no-session-persistence`. The [[Agent_SDK_overview|Agent SDK]] is the Python and TypeScript equivalent. Formerly called headless mode.

Learn more: [[Run_Claude_Code_programmatically|Run Claude Code programmatically]]

## O

### Output style

A configuration that changes the instructions Claude Code gives Claude, to set response behavior, tone, or format. Unlike [CLAUDE.md](#claude-md), which adds project context alongside Claude Code's default instructions, a custom output style adds its own instructions and can leave out the default software engineering instructions.

Learn more: [[Output_styles|Output styles]]

## P

### Permission mode

The baseline approval behavior for the session. Cycle with `Shift+Tab` in the CLI or use the mode selector in VS Code, Desktop, and claude.ai. Available modes are `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, and `bypassPermissions`.

The `default` mode is labeled Manual in the CLI, in the VS Code and JetBrains extensions, and in the desktop app, and Claude Code accepts `manual` as an alias for the value.

Learn more: [[Choose_a_permission_mode|Choose a permission mode]]

### Permission rule

A settings entry that allows, asks about, or denies a tool invocation based on the tool name and argument pattern. Rules are evaluated deny→ask→allow, first match wins. Permission rules are fine-grained controls layered on top of the broader [permission mode](#permission-mode).

Learn more: [[Configure_permissions|Configure permissions]]

### Plan mode

A [permission mode](#permission-mode) where Claude researches and proposes changes without editing your source files. It can read, search, and run exploration commands, then presents a plan for approval before touching anything. Enter plan mode with `/plan` or by pressing `Shift+Tab`.

Learn more: [[Choose_a_permission_mode|Analyze before you edit with plan mode]]

### Plugin

A bundle of skills, hooks, subagents, and MCP servers packaged as a single installable unit. Plugin skills are namespaced as `plugin-name:skill-name` so multiple plugins coexist. Distribute plugins across teams via a [[Plugins_overview|marketplace]].

Learn more: [[Plugins_overview|Plugins]]

### Project trust

A dialog accepting a directory before Claude Code loads its configuration. Acceptance is saved per project directory, except your home directory, where trust is held for the current session only and the prompt reappears on each launch. Until you trust a directory, Claude Code holds back some of the content its repository supplies, such as project allow rules and marketplaces from `.claude/settings.json`. [[Configure_permissions|What runs before you trust a folder]] lists each kind of content, including what a `-p` session runs without a dialog.

Learn more: [[Explore_the_claude_directory|The `.claude` directory]]

### Prompt injection

Hostile instructions embedded in a file, web page, or tool result that attempt to redirect Claude toward actions you never asked for. Claude Code's defenses include the permission system, command injection detection, and trust verification. [Auto mode](#auto-mode) adds a server-side probe that scans tool results for suspicious content and a classifier that reviews actions with tool results stripped, so injected text can't manipulate it directly.

Learn more: [[Security|Protect against prompt injection]]

## R

### Remote Control

A way to continue a local Claude Code session from your phone or browser via claude.ai. Your code execution and files stay on your machine; the interface is remote. Different from a [[Use_Claude_Code_in_the_cloud|cloud session]], which runs in a cloud sandbox.

Learn more: [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]

### Rules

Modular instruction files in `.claude/rules/` that load alongside CLAUDE.md. A rule can be path-scoped with YAML `paths:` frontmatter so it only loads when Claude reads, writes, or edits a matching file, keeping context lean until it's relevant.

Learn more: [[How_Claude_remembers_your_project|Organize rules with `.claude/rules/`]]

## S

### Sandboxing

OS-level filesystem and network isolation for the Bash tool. Commands run inside a boundary you define upfront, so Claude can work freely within it without per-command approval prompts. Sandboxing is a separate layer from [permission rules](#permission-rule).

Learn more: [[Configure_the_sandboxed_Bash_tool|Sandboxing]]

### Session

A conversation tied to your current directory, with its own independent [context window](#context-window). Sessions can be resumed with `claude -c`, forked with `--fork-session` to preserve history under a new session ID, or run in parallel across terminals. Running `/clear` starts a new session; the previous one stays stored and is available via `/resume`. Each session's transcript is stored under `~/.claude/projects/`.

Learn more: [[How_Claude_Code_works|Work with sessions]]

### Settings layers

The hierarchy Claude Code reads configuration from, in precedence order from highest to lowest: [managed policy](#managed-settings), settings you pass with the `--settings` flag, local settings at `.claude/settings.local.json`, project settings at `.claude/settings.json`, then user settings at `~/.claude/settings.json`. Arrays merge across layers; scalars at a higher layer override lower ones. See [[Settings_files_and_precedence|Settings precedence]].

Learn more: [[Settings_files_and_precedence|Settings files]]

### Skill

A `SKILL.md` file containing instructions, knowledge, or a workflow that Claude adds to its toolkit. Claude loads a skill automatically when relevant, or you invoke it directly with `/skill-name`. Skills follow the Agent Skills open standard; Claude Code extends it with invocation control and subagent execution.

Skills are the recommended successor to custom commands. A file at `.claude/commands/deploy.md` and one at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way; existing command files continue to work.

Learn more: [[Extend_Claude_with_skills|Extend Claude with skills]]

### Subagent

A specialized AI assistant that runs in its own context window with a custom system prompt, specific tool access, and independent permissions. It works on a delegated task and returns a summary to the main conversation. Use subagents to keep large explorations out of your primary context or to run parallel research. A subagent stays inside the session that spawned it. To pass findings between separate sessions you run yourself, use [[Message_your_other_Claude_Code_sessions|cross-session messaging]].

Built-in subagents include Explore, Plan, and general-purpose.

Learn more: [[Create_custom_subagents|Create custom subagents]]

### Surface

Any place you access Claude Code: the CLI, VS Code, JetBrains, Desktop, or claude.ai. All surfaces share the same engine. Sessions on your machine read your local CLAUDE.md, settings, and skills; [[Configure_cloud_environments|cloud sessions]] start from a fresh clone of your repository and don't read `~/.claude/` on your machine. Slack and the Chrome extension are integrations that connect to a surface rather than surfaces themselves.

Learn more: [[Platforms_and_integrations|Platforms and integrations]]

### System prompt

The instructions Claude Code sends ahead of your conversation on every request, covering how Claude uses tools, behaves safely, and formats its responses. You can add to the system prompt with `--append-system-prompt` or replace it with `--system-prompt`. The system prompt is the first layer of the [[How_Claude_Code_uses_prompt_caching|prompt cache]].

Your [CLAUDE.md](#claude-md) files and the instructions of your [output style](#output-style) aren't part of the system prompt. Claude Code delivers them in the conversation as [system reminders](#system-reminder).

Learn more: [[CLI_reference|System prompt flags]]

### System reminder

A message that Claude Code, as the [harness](#agentic-harness), adds to the conversation to give Claude context. You don't send system reminders yourself. Claude Code inserts them as a session runs, for example when the session starts, when a hook returns text, or when a file changes on disk. Claude reads them alongside your messages. The following all reach Claude as system reminders:

* Your [CLAUDE.md](#claude-md) files
* The instructions of your [output style](#output-style)
* Text a [hook](#hook) returns as `additionalContext`
* The list of available [skills](#skill)
* A note that a file Claude read earlier has changed on disk
* The commit and pull request attribution lines

In a logged API request, a system reminder appears wrapped in `<system-reminder>` tags inside a user message, or on some models as a separate message with the `system` role.

Learn more: [[Agent_SDK_Modifying_system_prompts|Context Claude Code adds outside the system prompt]]

## T

### Teleport

A command, `/teleport`, that pulls a cloud Claude Code session into your local terminal. Claude fetches the branch, loads the conversation history, and resumes from the cloud session's last state. The reverse direction is `--cloud`, which sends a local task to run in the cloud.

Learn more: [[Use_Claude_Code_in_the_cloud|From cloud to terminal]]

### Tool

An action Claude can take: read a file, edit code, run a shell command, search the web, spawn a subagent. Tools are what make Claude Code agentic. Without them, Claude can only respond with text. Each tool use returns a result that informs Claude's next decision in the [agentic loop](#agentic-loop).

Learn more: [[Tools_reference|Tools available to Claude]]

### Transcript

The stored record of a [session](#session). The conversation is what you and Claude exchange; the transcript is that conversation kept as a file, by default at `~/.claude/projects/<project>/<session-id>.jsonl`. Claude Code reads the file back when you resume, which is how a conversation continues after the session ends. For the on-screen view of the same conversation, see the [[Interactive_mode|transcript viewer]].

Learn more: [[Manage_sessions|Where transcripts are stored]]

### Turn

One complete response from Claude within a [session](#session). A turn begins when you send a message and ends when Claude finishes responding, with any number of [tool](#tool) calls in between. [Stop hooks](#hook) fire at the end of each turn. A session consists of many turns, and the [agentic loop](#agentic-loop) describes what happens inside one.

Learn more: [[How_Claude_Code_works|How Claude Code works]]

## V

### Verification loop

How a session knows the work is actually done instead of accepting a result that looks plausible. You give Claude a check it can run, such as a test suite, a build, or a screenshot comparison, and Claude iterates until the check passes instead of stopping after one attempt. A verification loop is the prerequisite for [[Keep_Claude_working_toward_a_goal|`/goal`]], unattended runs, and [[Orchestrate_subagents_at_scale_with_dynamic_workflows|dynamic workflows]]: without one, the only thing deciding the agent is finished is the agent itself.

Learn more: [[Best_practices_for_Claude_Code|Give Claude a way to verify its work]]

## W

### Worktree isolation

An isolation mode that runs Claude in a separate git worktree under `.claude/worktrees/`, enabled with the `-w` flag or `isolation: worktree` in subagent config. Changes stay on a separate branch in a separate directory, so parallel agents don't overwrite each other's files.

Learn more: [[Run_parallel_sessions_with_worktrees|Run parallel sessions with git worktrees]]

***

## Deprecated and renamed terms

These terms appear in older docs, blog posts, and community content. Use the current name when searching this site.

| Old term | Now called | Notes |
| - | - | - |
| Headless mode | [Non-interactive mode](#non-interactive-mode) | Same `-p` flag, same behavior |
| Web session; "Claude Code on the web" as the name for any cloud session | [Cloud session](#cloud-session) | "Claude Code on the web" now names only the browser surface at claude.ai/code |
| Custom commands | [Skills](#skill) | `.claude/commands/` files still work |
| Slash commands | Commands | "Slash" dropped from product copy |

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

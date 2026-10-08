---
title: "Week 36 · August 31 – September 4, 2026"
aliases:
  - "whats-new/2026-w36"
  - "Week 36 · August 31 – September 4, 2026"
tags:
  - "claude-code"
  - "release-notes"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w36"
status: "verified"
last_updated: "2026-10"
---

# Week 36 · August 31 – September 4, 2026

## Executive Summary
> Switch to Claude Fable 5.1, let computer use run in the background on Desktop, and watch Claude's edits in a live /diff panel.

## Technical Mechanics & Documentation

<div className="digest-meta">
  <span>Releases [[Claude_Code_changelog|v2.1.251 → v2.1.261]]</span>
  <span>4 features · August 31 – September 4</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Fable 5.1</span>
    <span className="digest-feature-pill">new model</span>
  </div>

  <p className="digest-feature-lede">Claude Fable 5.1 is available in Claude Code with a 1M-token context window, and the <code>fable</code> alias now selects it. In Claude apps gateway sessions, <code>fable</code> still selects Fable 5. If your gateway serves Fable 5.1, run <code>/model claude-fable-5-1</code>. Requires v2.1.257 or later.</p>

  <p className="digest-feature-try">Switch the current session to Fable 5.1 and save it as your default:</p>

  ```text Claude Code theme={null}
  > /model fable
  ```

  <p className="digest-feature-try">On the Anthropic API, the picker lists Fable only once the server reports it available for your organization, but typing <code>/model fable</code> checks with the server directly.</p>

  [[Model_configuration|Work with Fable]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Computer use runs in the background on Desktop</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">On macOS, computer use in the Claude Code Desktop app now works in the background: Claude sees and acts in the apps you've approved while you keep working. Background computer use is in beta on Pro and Max plans.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/background-computer-use.jpg?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=a599a6c6fa544cb8d1b426b93706caf4" alt="A Claude Code Desktop session where Claude asks to use Xcode, with a Computer use permission card that reads Let Claude see and act in the apps you approve, in the background or with full control of your screen, next to an Enable button" width="1440" height="810" data-path="images/whats-new/background-computer-use.jpg" />
  </Frame>

  [[Desktop_application|Let Claude use your computer]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Live diff panel in fullscreen rendering</span>
    <span className="digest-feature-pill">v2.1.260</span>
  </div>

  <p className="digest-feature-lede">In fullscreen rendering, <code>/diff</code> now opens a panel beside the conversation instead of a viewer you have to close. The panel lists the changed files with their added and removed line counts and refreshes each time Claude edits a file or runs a shell command. Select lines in the panel with the mouse to attach them to your next prompt.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/diff-panel.mp4?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=9d7553c19e7f227891cd95f1f59d796d" data-path="images/whats-new/diff-panel.mp4" />
  </Frame>

  <p className="digest-feature-try">With fullscreen rendering on, inside a git repository, and in a terminal at least 110 columns wide, toggle the panel:</p>

  ```text Claude Code theme={null}
  > /diff
  ```

  <p className="digest-feature-try">Run <code>/diff</code> again or click the <code>✕</code> in its header to close it.</p>

  [[Interactive_mode|Diff panel]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Find unused skills with /skill-doctor</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede"><code>/skill-doctor</code> shows what each of your skills costs in context and how often it gets used, so you can decide which ones to turn off. Every skill in the [[Extend_Claude_with_skills|skill listing]] adds to your context on every turn, whether or not Claude ever uses it. Requires v2.1.252 or later and isn't available in sessions that skip [[Environment_variables|feature-flag fetching]].</p>

  <p className="digest-feature-try">Run it in an interactive session to open the report in the <code>/plugin</code> manager's <strong>Stats</strong> tab:</p>

  ```text Claude Code theme={null}
  > /skill-doctor
  ```

  <p className="digest-feature-try">In non-interactive mode with <code>-p</code>, Claude Code prints the report as text instead.</p>

  [[Extend_Claude_with_skills|Find unused skills]]
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>A [[Hooks_reference|<code>PreModelSwitch</code>]] hook can block a model switch you request, and a [[Hooks_reference|<code>PostModelSwitch</code>]] hook can add context for Claude after the session's model changes</div>
    <div>[[Manage_costs_effectively|<code>/cost</code>]] adds a <code>Prompt cache (main)</code> line: the share of input tokens served from cache, the cache misses, whether the cache is warm, and a likely cause for the last miss when Claude Code can name one. Status line scripts get a matching <code>prompt\_cache</code> object</div>
    <div>Organizations can list HTTP and SSE MCP servers under the [[Control_MCP_server_access_for_your_organization|<code>managedMcpServers</code>]] managed setting to give them to every user, in addition to the servers that users add on their own</div>
    <div><code>/effort</code> and the <code>/model</code> picker now [[Model_configuration|save a separate effort level for each model]]; press <code>s</code> instead of <code>Enter</code> to apply a level to the current session only</div>
    <div>By default, the auto mode classifier [[Choose_a_permission_mode|now also blocks]] actions such as requesting credentials from the cloud instance-metadata endpoint or connecting to sibling containers that Claude didn't start</div>
    <div>In auto mode, Claude Code asks you before Claude [[Choose_a_permission_mode|first reads a file outside your working directories]], with an option to block such reads from then on</div>
    <div>Raise [[All_settings|<code>bashOutputMaxChars</code>]] and [[All_settings|<code>taskOutputMaxChars</code>]], up to 128,000 characters, so Claude receives more of the output from a successful command or background task inline</div>
    <div>The prompt's [[Interactive_mode|word-editing shortcuts follow readline]] for everyone, and the <code>keybindingFlavor</code> setting no longer has any effect. <code>Ctrl+W</code> deletes back to the previous whitespace, and <code>Alt+B</code>, <code>Alt+F</code>, and <code>Alt+D</code> treat punctuation such as <code>/</code> and <code>.</code> as word breaks</div>
    <div>If you set <code>defaultMode</code> to <code>"bypassPermissions"</code> in a project's <code>.claude/settings.json</code> or <code>.claude/settings.local.json</code>, it [[Choose_a_permission_mode|no longer takes effect]] and the session starts in Manual mode; set <code>"bypassPermissions"</code> in user or managed settings instead, or pass `--permission-mode`</div>
    <div>Seat-based Enterprise plans now [[Model_configuration|default to Opus 5]]</div>
    <div>In the VS Code extension, click the model name at the bottom of the prompt box to [[Use_Claude_Code_in_VS_Code|open the model picker]]</div>
    <div>In the VS Code extension, select <strong>Output styles</strong> in the command menu's Customize section to [[Use_Claude_Code_in_VS_Code|pick an output style]], including your custom ones</div>
  </div>
</div>

[[Claude_Code_changelog|Full changelog for v2.1.251–v2.1.261 →]]

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Release_Notes|Release Notes MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

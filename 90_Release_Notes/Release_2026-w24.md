---
title: "Week 24 · June 8–12, 2026"
aliases:
  - "whats-new/2026-w24"
  - "Week 24 · June 8–12, 2026"
tags:
  - "claude-code"
  - "release-notes"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w24"
status: "verified"
last_updated: "2026-10"
---

# Week 24 · June 8–12, 2026

## Executive Summary
> Move a session to a new directory with /cd, let subagents spawn their own subagents, and troubleshoot a broken configuration with safe mode.

## Technical Mechanics & Documentation

<div className="digest-meta">
  <span>Releases [[Claude_Code_changelog|v2.1.166 → v2.1.176]]</span>
  <span>3 features · June 8–12</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Move a session with /cd</span>
    <span className="digest-feature-pill">v2.1.169</span>
  </div>

  <p className="digest-feature-lede">The new <code>/cd</code> command moves the current session to a different working directory without rebuilding the prompt cache: the new directory's <code>CLAUDE.md</code> is appended as a message instead of replacing the system prompt. The session relocates to the new directory's project storage, so `--resume` and `--continue` find it there. Claude prompts you to trust the directory if you haven't worked in it before.</p>

  <p className="digest-feature-try">Move the session into another project without restarting:</p>

  ```text Claude Code theme={null}
  > /cd ../other-project
  ```

  [[Commands|Commands reference]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Subagents can spawn subagents</span>
    <span className="digest-feature-pill">v2.1.172</span>
  </div>

  <p className="digest-feature-lede">Subagents can now spawn their own subagents. The subagent panel below the prompt shows the full tree: each row carries a count of its descendants and a path back to <code>main</code>. Subagent chains are capped at five levels deep to prevent runaway concurrent trees.</p>

  <p className="digest-feature-try">Open the agents view to watch the nested tree as work fans out:</p>

  ```text Claude Code theme={null}
  > /agents
  ```

  [[Create_custom_subagents|Spawn nested subagents]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Troubleshoot with safe mode</span>
    <span className="digest-feature-pill">v2.1.169</span>
  </div>

  <p className="digest-feature-lede">Start Claude Code with `--safe-mode`, or set <code>CLAUDE\_CODE\_SAFE\_MODE</code>, to launch with all customizations disabled: <code>CLAUDE.md</code>, skills, plugins, hooks, MCP servers, and custom commands and agents do not load. Authentication, model selection, built-in tools, and permissions still work. If a problem disappears in safe mode, one of those surfaces is the cause.</p>

  <p className="digest-feature-try">Launch a clean session to isolate a broken configuration:</p>

  ```bash terminal theme={null}
  claude --safe-mode
  ```

  [[Debug_your_configuration|Test against a clean configuration]]
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>[[Model_configuration|<code>fallbackModel</code>]] configures up to three fallback models tried in order when the primary is overloaded or unavailable, and `--fallback-model` now applies to interactive sessions too</div>
    <div>Session titles are now generated in the language of your conversation; pin a specific one with the <code>language</code> setting</div>
    <div>`claude agents --json` adds `--all` to include completed sessions plus new <code>id</code> and <code>state</code> fields, and no longer omits blocked or newly dispatched sessions</div>
    <div>Browsing a marketplace's plugins in <code>/plugin</code> now has a search bar</div>
    <div>New <code>disableBundledSkills</code> setting and <code>CLAUDE\_CODE\_DISABLE\_BUNDLED\_SKILLS</code> hide bundled skills, workflows, and built-in commands from the model</div>
    <div>Deny rules accept a glob in the tool-name position, so <code>"\*"</code> denies all tools, and unknown tool names in deny rules now warn at startup</div>
    <div>Agent messaging is hardened: messages relayed via <code>SendMessage</code> from other agents no longer carry user authority, and auto mode blocks them</div>
    <div>Amazon Bedrock reads the AWS region from <code>\~/.aws</code> config files when <code>AWS\_REGION</code> is unset, and <code>/status</code> shows where the region came from</div>
    <div>New <code>enforceAvailableModels</code> managed setting makes the <code>availableModels</code> allowlist also constrain the Default model</div>
    <div>Claude in Chrome browser tools now load in a single batched call instead of one per tool</div>
    <div><code>claude update</code> announces the target version before downloading instead of going silent</div>
    <div>New <code>footerLinksRegexes</code> setting adds regex-matched link badges to the footer row</div>
  </div>
</div>

[[Claude_Code_changelog|Full changelog for v2.1.166–v2.1.176 →]]

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Release_Notes|Release Notes MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

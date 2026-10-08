---
title: "Week 17 · April 20–24, 2026"
aliases:
  - "whats-new/2026-w17"
  - "Week 17 · April 20–24, 2026"
tags:
  - "claude-code"
  - "release-notes"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w17"
status: "verified"
last_updated: "2026-10"
---

# Week 17 · April 20–24, 2026

## Executive Summary
> /ultrareview opens as a research preview, automatic session recaps when you return to a terminal, custom color themes you can build and ship in plugins, and a redesigned Claude Code on the web.

## Technical Mechanics & Documentation

<div className="digest-meta">
  <span>Releases [[Claude_Code_changelog|v2.1.114 → v2.1.119]]</span>
  <span>4 features · April 20–24</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/ultrareview</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">Now in public research preview. Ultrareview runs a fleet of bug-hunting agents in the cloud against your branch or a PR, and findings land back in the CLI or Desktop automatically. Run it before merging critical changes such as auth or data migrations.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/ultrareview.mp4?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=0fb1271365d38f414ad155aeb8edb08e" data-path="images/whats-new/ultrareview.mp4" />
  </Frame>

  <p className="digest-feature-try">Review the branch you're on:</p>

  ```text Claude Code theme={null}
  > /ultrareview
  ```

  <p className="digest-feature-try">Or point it at a PR:</p>

  ```text Claude Code theme={null}
  > /ultrareview 1234
  ```

  [[Find_bugs_with_ultrareview|Ultrareview guide]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Session recap</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">Switch focus away from a session and come back to a one-line recap of what happened while you were gone. Helpful for staying in flow while running several Claude sessions at once.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/session-recap.mp4?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=0a8db1470bd0161a47efeb2f322af76f" data-path="images/whats-new/session-recap.mp4" />
  </Frame>

  <p className="digest-feature-try">Generate a recap on demand, or turn the automatic one off from <code>/config</code>:</p>

  ```text Claude Code theme={null}
  > /recap
  ```

  [[Interactive_mode|Interactive mode: session recap]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Custom themes</span>
    <span className="digest-feature-pill">v2.1.118</span>
  </div>

  <p className="digest-feature-lede">Build and switch between named color themes from <code>/theme</code>, or hand-edit JSON files in <code>\~/.claude/themes/</code>. Each theme picks a base preset and overrides only the tokens you care about. Plugins can ship themes too.</p>

  <p className="digest-feature-try">Open the theme picker and create a new one:</p>

  ```text Claude Code theme={null}
  > /theme
  ```

  [[Configure_your_terminal_for_Claude_Code|Terminal config: create a custom theme]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Code on the web</span>
    <span className="digest-feature-pill">web</span>
  </div>

  <p className="digest-feature-lede">A new look for <a href="https://claude.ai/code">claude.ai/code</a> that matches the redesigned desktop app: sessions sidebar, drag-and-drop layout, and a refreshed routines view. Key parts were rebuilt for quicker responses and a more reliable experience.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/web-redesign.jpeg?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=a2aca1b49e295b7337f5779038db8e2c" alt="Claude Code on the web redesign overview: new UI, speed and reliability, work across web, mobile, and CLI" width="1602" height="1610" data-path="images/whats-new/web-redesign.jpeg" />
  </Frame>

  [[Use_Claude_Code_in_the_cloud|Claude Code on the web]]
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>[[Interactive_mode|Vim visual mode]]: press <code>v</code> for character selection or <code>V</code> for line selection in the prompt input, with operators and visual feedback</div>
    <div>Hooks can now call MCP tools directly via [[Hooks_reference|<code>type: "mcp\_tool"</code>]], so a hook can hit an already-connected server without spawning a process</div>
    <div><code>/cost</code> and <code>/stats</code> are merged into [[Commands|<code>/usage</code>]]; the old names still work as typing shortcuts that open the relevant tab</div>
    <div><code>/config</code> changes (theme, editor mode, verbose, and similar) now persist to <code>\~/.claude/settings.json</code> and follow the same project/local/policy precedence as other [[Settings_files_and_precedence|settings]]</div>
    <div>[[Create_custom_subagents|Forked subagents]] can be enabled on external builds with <code>CLAUDE\_CODE\_FORK\_SUBAGENT=1</code>: a fork inherits your full conversation context instead of starting fresh</div>
    <div>Default [[Model_configuration|effort level]] for Pro and Max subscribers on Opus 4.6 and Sonnet 4.6 is now <code>high</code> (was <code>medium</code>)</div>
    <div>Native macOS and Linux builds replace the <code>Glob</code> and <code>Grep</code> tools with embedded <code>bfs</code> and <code>ugrep</code> available through Bash, for faster searches without a separate tool round-trip</div>
    <div>`--from-pr` now accepts GitLab merge request, Bitbucket pull request, and GitHub Enterprise PR URLs in addition to github.com</div>
    <div>Auto mode: include <code>"\$defaults"</code> in [[Configure_auto_mode|<code>autoMode.allow</code>, <code>soft\_deny</code>, or <code>environment</code>]] to add custom rules alongside the built-in list instead of replacing it</div>
    <div>New [[Plugin_dependencies|<code>claude plugin tag</code>]] command creates release git tags for plugins with version validation</div>
    <div>Opus 4.7 sessions now compute against the model's native 1M context window, fixing inflated <code>/context</code> percentages and premature autocompaction</div>
    <div><code>/resume</code> on large sessions is up to 67% faster and now offers to summarize stale, large sessions before re-reading them</div>
  </div>
</div>

[[Claude_Code_changelog|Full changelog for v2.1.114–v2.1.119 →]]

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Release_Notes|Release Notes MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

---
title: "Week 30 · July 20–24, 2026"
aliases:
  - "whats-new/2026-w30"
  - "Week 30 · July 20–24, 2026"
tags:
  - "claude-code"
  - "release-notes"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w30"
status: "verified"
last_updated: "2026-10"
---

# Week 30 · July 20–24, 2026

## Executive Summary
> Opus 5 becomes the default Opus model, Claude Code Desktop adds an iOS Simulator pane, and the Claude Security plugin scans your code for vulnerabilities.

## Technical Mechanics & Documentation

<div className="digest-meta">
  <span>Releases [[Claude_Code_changelog|v2.1.214 → v2.1.219]]</span>
  <span>3 features · July 20–24</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Opus 5</span>
    <span className="digest-feature-pill">new model</span>
  </div>

  <p className="digest-feature-lede">Claude Opus 5 is the new default Opus model in Claude Code. It's the default on Max, Team Premium, Enterprise pay-as-you-go, and the Anthropic API, and on Claude Platform on AWS, Amazon Bedrock, and Google Cloud's Agent Platform. On the Anthropic API and on Max, Team, and Enterprise plans, Opus 5 runs with a [[Model_configuration|1M-token context window]]; on Amazon Bedrock and Google Cloud's Agent Platform, select the 1M model variant. Fast mode moves to Opus 5 at \$10/\$50 per MTok. Requires v2.1.219 or later.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/N3yEaTYPXMXFrF6k/images/whats-new/opus-5.mp4?fit=max&auto=format&n=N3yEaTYPXMXFrF6k&q=85&s=8536b1cb3180e539008f39930403e47b" data-path="images/whats-new/opus-5.mp4" />
  </Frame>

  <p className="digest-feature-try">Switch to Opus 5 by name, or pick it from the model picker:</p>

  ```text Claude Code theme={null}
  > /model claude-opus-5
  ```

  [[Model_configuration|Model configuration]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">iOS Simulator in Claude Code Desktop</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">Claude Code Desktop on macOS gets an iOS Simulator pane, in public beta on Pro, Max, and Team plans. When Claude builds, launches, or checks your app in a simulator, the pane opens next to the conversation and streams the device screen live, so you can watch Claude tap through the app to verify its changes or drive the device yourself. Requires Xcode with the iOS platform installed, and Claude Desktop v1.24012.0 or later.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/N3yEaTYPXMXFrF6k/images/whats-new/ios-simulator.jpg?fit=max&auto=format&n=N3yEaTYPXMXFrF6k&q=85&s=6c88418ed14ed0fb12cc1af75b17f2ee" alt="Claude Code Desktop with the iOS Simulator pane showing an iPhone app next to the conversation" width="2048" height="1152" data-path="images/whats-new/ios-simulator.jpg" />
  </Frame>

  <p className="digest-feature-try">Ask Claude to run or test your app, and the pane opens when the app launches:</p>

  ```text Claude Code theme={null}
  > Build the app and run it in the simulator to check the onboarding flow.
  ```

  [[Test_iOS_apps_in_the_simulator|Test iOS apps in the simulator]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Security plugin</span>
    <span className="digest-feature-pill">plugin</span>
  </div>

  <p className="digest-feature-lede">The Claude Security plugin runs a multi-agent vulnerability scan of your codebase inside a Claude Code session: agents map your architecture, build a threat model, hunt for vulnerabilities, and independently review every finding before writing the report to a <code>CLAUDE-SECURITY-\<timestamp>/</code> directory. Scan a whole repository or only a branch's diff, a pull request, or a single commit, then turn the findings you choose into reviewed patches that you apply yourself.</p>

  <p className="digest-feature-try">Install the plugin from the official Anthropic marketplace, run <code>/reload-plugins</code>, then start a scan with <code>/claude-security</code>:</p>

  ```text Claude Code theme={null}
  > /plugin install claude-security@claude-plugins-official
  ```

  [[Scan_your_codebase_for_vulnerabilities|Scan and fix your codebase]]
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>[[Code_Review|<code>/code-review</code>]] now runs as a background subagent with its own context window, so review work stays out of your conversation and the findings arrive when it completes</div>
    <div><code>/verify</code>, <code>/code-review</code>, and <code>/deep-research</code> run only when you invoke them; Claude no longer launches them on its own</div>
    <div>[[Interactive_mode|Emoji shortcodes]] autocomplete in the prompt input: type <code>:heart:</code> to insert an emoji, or two or more characters after <code>:</code> for suggestions; turn it off with <code>emojiCompletionEnabled</code></div>
    <div>Skills with <code>context: fork</code> [[Extend_Claude_with_skills|run in the background]] by default, and <code>background: false</code> in the skill's frontmatter waits for the result in the same turn</div>
    <div>A session runs up to 20 subagents concurrently by default; change the [[Create_custom_subagents|limit]] with <code>CLAUDE\_CODE\_MAX\_CONCURRENT\_SUBAGENTS</code></div>
    <div>`--max-budget-usd` now enforces the cap on subagents: once spend reaches it, Claude can't start more and running background subagents stop</div>
    <div>New [[Configure_the_sandboxed_Bash_tool|<code>sandbox.filesystem.disabled</code>]] setting skips filesystem isolation while keeping network egress control</div>
    <div>In auto mode, the checks for dangerous <code>rm</code> commands, background jobs, and suspicious Windows paths no longer open permission dialogs; the auto-mode classifier adjudicates them instead</div>
    <div>Bash permission checks fail closed on more shell forms, including file-descriptor redirects, Zsh variable subscripts in <code>\[\[ ]]</code> comparisons, <code>help</code> and <code>man</code> invocations that could run unsafe options, and commands over 10,000 characters</div>
    <div>[[Speed_up_responses_with_fast_mode|Fast mode]] no longer supports Opus 4.7: <code>/fast</code> now applies to Opus 5 and Opus 4.8</div>
    <div>Long-running tool calls emit a periodic progress heartbeat instead of going silent</div>
  </div>
</div>

[[Claude_Code_changelog|Full changelog for v2.1.214–v2.1.219 →]]

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Release_Notes|Release Notes MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

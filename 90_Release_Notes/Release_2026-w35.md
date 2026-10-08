---
title: "Week 35 · August 24–28, 2026"
aliases:
  - "whats-new/2026-w35"
  - "Week 35 · August 24–28, 2026"
tags:
  - "claude-code"
  - "release-notes"
source_url: "https://code.claude.com/docs/en/whats-new/2026-w35"
status: "verified"
last_updated: "2026-10"
---

# Week 35 · August 24–28, 2026

## Executive Summary
> Resume terminal sessions in the Claude Code Desktop app, review feedback reports that Claude drafts for you, and start a session in restricted mode.

## Technical Mechanics & Documentation

<div className="digest-meta">
  <span>Releases [[Claude_Code_changelog|v2.1.240 → v2.1.250]]</span>
  <span>3 features · August 24–28</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Resume terminal sessions in the Desktop app</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">Type <code>/resume</code> in the Claude Code Desktop prompt box to pick up any session you started from the CLI and continue it in the app with the full conversation and context intact. Search your sessions by title, folder, or branch, and preview where you left off before you resume.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/desktop-resume-cli-session.mp4?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=41e4a5fda6b9d63280589f2cbdabf44f" data-path="images/whats-new/desktop-resume-cli-session.mp4" />
  </Frame>

  <p className="digest-feature-try">In a Desktop session, run the command to list your terminal sessions:</p>

  ```text Claude Code theme={null}
  > /resume
  ```

  <p className="digest-feature-try">Select a session and press <code>Enter</code>. The conversation opens in the app where you left off.</p>

  [[Desktop_application|Move between the CLI and Desktop]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude-drafted feedback</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">When a tool keeps failing, Claude can't help with a request, or you point out a mistake, Claude now drafts a feedback report for you with the <code>SendFeedback</code> tool. A card above your prompt shows the draft, and you can review, send, or dismiss it from there. Nothing reaches Anthropic until you send it. Requires v2.1.238 or later.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/claude-drafted-feedback.jpg?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=5cacb3be0dffd1cbd417381f3721637e" alt="A Claude Code session where Claude has drafted a bug report titled Sandbox image pull fails behind proxy, shown as a card above the prompt with options to review, send, or dismiss" width="1440" height="756" data-path="images/whats-new/claude-drafted-feedback.jpg" />
  </Frame>

  <p className="digest-feature-try">Run <code>/feedback</code> with no argument to open your queue of drafts from every session:</p>

  ```text Claude Code theme={null}
  > /feedback
  ```

  <p className="digest-feature-try">Select a draft, then edit, send, or discard it. To turn drafting off, set <strong>Claude-drafted feedback</strong> to <code>off</code> in <code>/config</code>.</p>

  [[Tools_reference|SendFeedback tool behavior]]
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Restricted mode</span>
    <span className="digest-feature-pill">v2.1.248</span>
  </div>

  <p className="digest-feature-lede">Restricted mode starts Claude Code without the built-in tools that run commands or code. Use it when an evaluation harness drives <code>claude</code> on a shared machine. Start it with `--restricted` or set <code>CLAUDE\_CODE\_RESTRICTED=1</code>. Claude Code also removes <code>WebFetch</code>, confines the file tools to the working directories, loads only managed settings and `--settings`, and refuses the <code>bypassPermissions</code> permission mode.</p>

  <p className="digest-feature-try">Run a non-interactive query without the command-running tools:</p>

  ```bash terminal theme={null}
  claude --restricted -p "review src/ for SQL injection risks"
  ```

  <p className="digest-feature-try">To give Claude one of the removed tools back, list it in `--tools` together with the other built-in tools you want, for example `--tools "Bash,Read,Edit"`. `--tools` is an allowlist, and its <code>default</code> preset doesn't restore the removed tools.</p>

  [[CLI_reference|CLI flags]]
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Set the new [[All_settings|<code>modelPicker</code>]] setting to extend or replace the <code>/model</code> picker's built-in list with your own ordered, labeled entries, including Amazon Bedrock or Google Cloud's Agent Platform model IDs</div>
    <div>Set [[How_Claude_Code_uses_prompt_caching|<code>promptCacheTtl</code>]] to <code>1h</code> to keep a one-hour prompt cache on the main conversation when you use an API key or a cloud provider; <code>subagentPromptCacheTtl</code> sets the TTL for subagents and all other requests outside the main conversation</div>
    <div>On Pro, Max, Team, and Enterprise plans, [[Manage_costs_effectively|<code>/usage</code>]] adds a Loops breakdown: run count, total tokens, tokens per run, and last run for the <code>/loop</code> and scheduled tasks that used the most tokens</div>
    <div>Organizations on contracted rates can set the [[Manage_costs_effectively|<code>modelPricing</code>]] managed setting so <code>/usage</code>, the status line, and OpenTelemetry report cost at those rates instead of list price</div>
    <div><code>/login</code> offers <strong>Sign in with your Console account</strong> under the <strong>Anthropic Console account</strong> option, so members of Console organizations that don't allow API keys can sign in without creating one</div>
    <div>Run <code>/permissions</code> and open the new [[Configure_auto_mode|<strong>Auto mode</strong> tab]] to view and edit auto mode classifier rules without opening a settings file</div>
    <div>When auto mode is available, Bash permission prompts in the Manual and <code>acceptEdits</code> permission modes offer a [[Choose_a_permission_mode|<strong>Yes, and switch to auto mode</strong>]] option; select it to approve the command and switch the session to auto mode</div>
    <div>After you [[Configure_permissions|move a session with <code>/cd</code>]], the new directory's project settings, hooks, <code>.mcp.json</code> servers, skills, and subagents take effect immediately instead of on the next `--resume`</div>
    <div>In non-interactive sessions, including <code>-p</code> runs, Agent SDK runs, and cloud sessions, Claude Code [[Error_reference|continues a response]] that a server error, dropped connection, or stall cut off mid-stream, when the partial response contains text and no tool calls</div>
    <div>A subagent that stops at its <code>maxTurns</code> limit returns its output marked as partial, with a hint that Claude can [[Create_custom_subagents|continue it with <code>SendMessage</code>]], instead of appearing finished</div>
    <div>On Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry, sessions on the same machine can now [[Message_your_other_Claude_Code_sessions|message each other]], <code>/loop</code> can [[Run_prompts_on_a_schedule|choose its own interval]], and <code>/model</code> and <code>/effort</code> apply immediately instead of after the turn ends</div>
    <div>The native installer and auto-updater download a zstd-compressed build, about 75 MB instead of 340 MB on Linux x64, and native builds load code on demand, using roughly 40 to 70 MB less memory per session</div>
  </div>
</div>

[[Claude_Code_changelog|Full changelog for v2.1.240–v2.1.250 →]]

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Release_Notes|Release Notes MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

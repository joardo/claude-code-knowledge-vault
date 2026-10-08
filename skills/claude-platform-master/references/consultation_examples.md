---
title: "Claude Platform Master: Consultation Examples & Case Studies"
aliases:
  - "consultation_examples"
  - "Claude Consultation Case Studies"
tags:
  - "claude-code"
  - "reference"
  - "case-studies"
status: "verified"
last_updated: "2026-10"
---

# Claude Platform Consultation Examples & Case Studies

> Five detailed, end-to-end consultation blueprints demonstrating optimal tool selection across common real-world engineering archetypes.

---

## Demonstration 1: Unattended Overnight Refactoring & Test Suite Repair

### User Request
> "I have a legacy repository with 60 failing TypeScript tests after a major version upgrade. I want Claude to work autonomously overnight to fix all failing tests, run the build, and ensure zero regressions without me sitting here approving every prompt."

### Master Consultation Response

#### 1. Triage & Architectural Assessment
- **Category**: Long-running autonomous loop + automated code verification.
- **Core Challenge**: Context window exhaustion over hours of execution; potential infinite loops or premature exits; avoiding manual approval prompts without sacrificing host safety.

#### 2. Primary Recommendation: `/goal` with Auto-Mode & Fast Checkpointing
Run Claude Code in an interactive session upgraded to autonomous goal mode:
```bash
# 1. Launch with Auto Mode to eliminate interactive confirmation prompts safely
claude --permission-mode autoMode --model opus
```
In the session prompt, set the completion goal:
```text
/goal All 60 failing tests in `npm test` must pass, `npm run build` must succeed with zero type errors, and git status must only show clean, targeted modifications. Run the test suite after every file change to verify progress.
```

**Why this is optimal**:
- `/goal` monitors the completion condition and prevents Claude from stopping until the tests actually pass.
- `autoMode` uses the classifier to approve safe file edits and npm test runs automatically while safeguarding against destructive operations (e.g., deleting git history).
- Context compaction fires automatically when needed.

#### 3. Alternatives Comparison
| Approach | Autonomy | Safety | Risk of Premature Stop | Token Overhead |
| :--- | :--- | :--- | :--- | :--- |
| **Primary: `/goal` + AutoMode** | **High (Unattended)** | **High (Classifier guardrails)** | **Zero (Stays until goal met)** | **Optimized (Auto-compact)** |
| Alt A: Headless Script (`claude -p`) | Medium (Single turn) | High | High (Exits after first turn) | Low |
| Alt B: `--dangerously-skip-permissions` | Unchecked | Very Low (No protection) | Medium | Identical |
| Alt C: Dynamic Workflow Script | High (Multi-agent) | High | Low | Higher (Orchestrator overhead) |

#### 4. Safety Guardrail: PreToolUse Hook
Add a safety hook to `.claude/settings.json` to prevent accidental git hard resets:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "command": "python3 -c 'import sys, json; data=json.load(sys.stdin); cmd=data.get(\"input\", {}).get(\"command\", \"\"); sys.exit(1 if \"git reset --hard\" in cmd or \"rm -rf\" in cmd else 0)'"
      }
    ]
  }
}
```

---

## Demonstration 2: Zero-Trust CI/CD Automated PR Review

### User Request
> "We want to run Claude Code inside our GitHub Actions pipeline to review incoming community pull requests, detect security bugs, and leave comments on the PR, but we cannot trust the PR code because of potential prompt injection attacks."

### Master Consultation Response

#### 1. Triage & Architectural Assessment
- **Category**: Headless automated CI/CD pipeline + untrusted input security boundary.
- **Core Challenge**: Malicious pull request code containing prompt injection attempting to steal CI secrets (`GITHUB_TOKEN`, API keys) or run malicious bash commands.

#### 2. Primary Recommendation: Headless `claude -p` + Sandboxed Bash + Ephemeral Runner
Configure GitHub Actions with strict isolation:
```yaml
name: Secure Claude Code PR Review
on:
  pull_request_target:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    container:
      image: anthropic/claude-code-sandbox:latest
      options: --cap-drop=ALL --read-only
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - name: Run Review with Sandboxed Tools
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "Review this pull request diff for security vulnerabilities, OWASP top 10, and memory leaks. Output findings in Markdown format." \
            --output-format json \
            --tools "ReadFile,GlobTool,GrepTool" \
            --sandbox-bash \
            --model sonnet
```

**Why this is optimal**:
- Restricts tools to read-only operations (`ReadFile`, `GlobTool`, `GrepTool`), completely revoking arbitrary bash execution.
- The `--sandbox-bash` flag prevents egress to external endpoints, thwarting exfiltration attacks.
- Piped output writes to a structured file for safe GitHub bot commenting.

---

## Demonstration 3: Massive Codebase Exploration & High-Concurrency Refactor

### User Request
> "We have a monorepo with 40 microservices. We need to migrate all services from logging library A to library B. If I do this in one session, the context window explodes after 2 services."

### Master Consultation Response

#### 1. Triage & Architectural Assessment
- **Category**: Multi-agent parallel coordination + context isolation.
- **Core Challenge**: Context window thrashing; file collision across simultaneous edits.

#### 2. Primary Recommendation: Agent View with Git Worktrees (`--worktree`)
Spin up isolated parallel workers across packages using Claude's worktree support:
```bash
# In the root monorepo, dispatch parallel background workers for each service:
for service in auth billing checkout users inventory; do
  claude --worktree \
         --permission-mode autoMode \
         --name "migrate-$service" \
         "Migrate packages/$service from logging library A to library B. Update imports, replace logger calls, and run 'pnpm --filter @services/$service test' until green." &
done
```
Then monitor all sessions concurrently in the interactive dashboard:
```bash
claude agents
```

**Why this is optimal**:
- Each session receives a fresh, isolated 200k context window dedicated entirely to one microservice.
- `--worktree` checks out independent temporary git branches, preventing file conflicts.
- `claude agents` provides real-time progress, diff review, and attach capabilities (`claude attach <id>`).

---

## Demonstration 4: Cost-Constrained Batch Processing

### User Request
> "I have 500 markdown documentation files that need style guide formatting. I have a tight token budget and cannot afford Opus or verbose conversational output."

### Master Consultation Response

#### 1. Triage & Architectural Assessment
- **Category**: High-volume batch script + strict token budgeting.

#### 2. Primary Recommendation: Haiku + Concise Output Style + Piped Headless Execution
```bash
find docs/ -name "*.md" | while read -r doc; do
  cat "$doc" | claude -p "Format this markdown document to strictly comply with standard style rules. Output only the updated markdown content without conversational commentary." \
    --model haiku \
    --style concise \
    > "${doc}.tmp" && mv "${doc}.tmp" "$doc"
done
```

**Why this is optimal**:
- Model Selection: Haiku is ~10x cheaper than Sonnet and ~50x cheaper than Opus for mechanical formatting.
- `--style concise`: Disables conversational chit-chat, hedging, and pleasantries, saving ~70% on output token billing.
- Piped stdin/stdout: Runs one-shot without maintaining persistent multi-turn conversational history.

---

## Demonstration 5: Deterministic Quality Gates (Hooks vs MCP vs Skills)

### User Request
> "We want to ensure that whenever Claude edits Python files, black and flake8 are run automatically, and if flake8 fails, Claude must fix the issue before claiming completion. Should I build a skill, an MCP server, or a hook?"

### Master Consultation Response

#### 1. Triage & Tool Selection
- **Diagnosis**: You need **100% deterministic quality enforcement**.
- **Decision**: Use a **`PostToolUse` Lifecycle Hook**, NOT an MCP server or a Skill!
- **Why Hooks Beat Skills & MCP here**:
  - An LLM skill relies on Claude "remembering" to run a command. It can hallucinate or skip it under high cognitive load.
  - An MCP tool still requires Claude to choose to call it.
  - A **`PostToolUse` Hook is deterministic OS-level code**. Every time Claude calls `Edit` or `Write` on a `.py` file, the hook fires in bash automatically.

#### 2. Implementation Configuration
In `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "command": "python3 -c 'import sys, json, subprocess; data=json.load(sys.stdin); tool=data.get(\"tool_name\"); path=data.get(\"input\", {}).get(\"path\", \"\"); (subprocess.run([\"black\", path], check=True) if path.endswith(\".py\") and tool in [\"Edit\", \"WriteFile\"] else None)'"
      }
    ]
  }
}
```
And in `CLAUDE.md`:
```markdown
- After making Python edits, verify that `flake8` passes. A PostToolUse hook automatically applies `black` formatting.
```

---
title: "Decision Matrix: Tool Approval & Security Boundaries"
aliases:
  - "Matrix_Tool_Approval_and_Security"
  - "Security Matrix"
tags:
  - "claude-code"
  - "matrix"
  - "security"
  - "permissions"
status: "verified"
last_updated: "2026-10"
---

# Decision Matrix: Tool Approval & Security Boundaries

> Selecting the appropriate isolation, permission mode, and sandboxing level for local, cloud, and enterprise environments.

## Comparative Matrix

| Mode / Mechanism | Prompt Behavior | Filesystem Boundary | Network Boundary | Threat Model Fit |
| :--- | :--- | :--- | :--- | :--- |
| **Default Interactive Mode** | Asks for Bash commands & critical edits | Host machine | Host network | Standard local development with human oversight |
| **Auto Mode (`autoMode`)** | AI classifier auto-approves safe actions; prompts on destructive actions | Host machine | Host network | Experienced developers wanting frictionless local flow |
| **Accept Edits Mode** | Auto-approves file edits; prompts for Bash commands | Host machine | Host network | Code refactoring where shell execution requires manual review |
| **Bypass (`--dangerously-skip-permissions`)** | **Never prompts** (unrestricted) | Host machine | Host network | **Disposable containers ONLY**; strictly forbidden on production host machines |
| **Sandboxed Bash Tool** | Configurable prompts | Restricted to project root jail | Restricted egress domain whitelist | Mitigating prompt injection when analyzing untrusted open-source repos |
| **Devcontainers / Docker** | Isolated environment | Container mount only | Container bridge network | Team consistency; untrusted third-party dependencies |
| **Cloud Self-Hosted Runners** | Cloud orchestrated | Isolated cloud VM runner | Enterprise VPC egress | Zero developer machine exposure; air-gapped internal corporate code |

---

## Security Selection Rules

1. **Analyzing an untrusted external repo (e.g. assessing CVEs or unfamiliar PRs)?**
   - **Enforce [[Configure_the_sandboxed_Bash_tool|Sandboxed Bash]]** or run inside a **[[Development_containers|Devcontainer]]**. Never run unrestricted permissions on untrusted repositories.
2. **Running unattended CI/CD jobs?**
   - Run in an isolated container/runner with ephemeral tokens. Use fine-grained permission rules rather than blanket bypass where possible.
3. **Enterprise Governance?**
   - Enforce settings using [[Deploy_managed_settings|Managed Settings]] to lock down allowed models, disable telemetry leakage, and restrict MCP servers with [[Control_MCP_server_access_for_your_organization|Managed MCP]].

---
## Related References
- [[Choose_a_permission_mode|Choose a Permission Mode]]
- [[Configure_the_sandboxed_Bash_tool|Sandboxed Bash Tool]]
- [[Set_up_Claude_Code_for_your_organization|Organization Setup]]

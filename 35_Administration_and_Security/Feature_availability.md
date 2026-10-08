---
title: "Feature availability"
aliases:
  - "feature-availability"
  - "Feature availability"
tags:
  - "claude-code"
  - "admin-security"
source_url: "https://code.claude.com/docs/en/feature-availability"
status: "verified"
last_updated: "2026-10"
---

# Feature availability

## Executive Summary
> Compare which Claude Code features are available across Anthropic subscription plans, the Anthropic Console, Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, and Microsoft Foundry.

## Technical Mechanics & Documentation

The Claude Code CLI and everything that runs locally work on every provider. For setup instructions per provider, see the [[Enterprise_deployment_overview|Enterprise deployment overview]]. To skip straight to what is missing on your provider, see the [summary by provider](#summary-by-provider) tabs.

In the tables below, ✓ means available, ✗ means not available, and "See note" links to a footnote for partial support. A qualifier after ✓ narrows availability to that subset, and "Admin-enabled" means the feature is off until an organization admin turns it on.

## Availability by model provider

How you authenticate determines which features Claude Code can reach. For a single list of what is missing on your provider, see the [summary by provider](#summary-by-provider) tabs. To find your column in the tables:

* **Claude subscription**: you sign in with a claude.ai account on the Pro, Max, Team, or Enterprise plan
* **Anthropic Console**: you authenticate with an Anthropic API key or by [[Authentication|signing in to a Console account without one]]
* **Amazon Bedrock**: you use Claude models from the Amazon Bedrock model catalog and set `CLAUDE_CODE_USE_BEDROCK`. The [[Claude_Code_on_Amazon_Bedrock|Mantle endpoint]] (`CLAUDE_CODE_USE_MANTLE`) is covered by this column
* **Claude Platform on AWS**: you bought Claude through AWS Marketplace but call the Anthropic API, and set `CLAUDE_CODE_USE_ANTHROPIC_AWS`
* **Google Cloud's Agent Platform**: Google-operated; you set `CLAUDE_CODE_USE_VERTEX`
* **Microsoft Foundry**: Anthropic-operated; you set `CLAUDE_CODE_USE_FOUNDRY`

### Features available on every provider

These work on every provider:

* [[Quickstart|CLI]] and [[Agent_SDK_overview|Agent SDK]]
* [[Use_Claude_Code_in_VS_Code|VS Code]] and [[JetBrains_IDEs|JetBrains]] extensions
* [[Create_custom_subagents|Subagents]], [[Automate_actions_with_hooks|hooks]], [[Commands|commands]], and [[Extend_Claude_with_skills|skills]]
* [[How_Claude_remembers_your_project|CLAUDE.md memory]], [[Plugins_overview|plugins]], and [[Connect_Claude_Code_to_tools_via_MCP|MCP servers]]
* [[Checkpointing|Checkpoints]], [[Configure_the_sandboxed_Bash_tool|sandboxing]], and [[Orchestrate_subagents_at_scale_with_dynamic_workflows|Workflows]]
* [[Monitoring|OpenTelemetry metrics]] and the [[Deploy_managed_settings|managed settings file]]

These have provider-specific differences:

* **MCP servers**: [[Connect_Claude_Code_to_tools_via_MCP|connectors from claude.ai]] load only when your claude.ai subscription is the active authentication method. [[Connect_Claude_Code_to_tools_via_MCP|Tool search]] is off by default when `ANTHROPIC_BASE_URL` points to a non-first-party host, and isn't supported on Google Cloud's Agent Platform models earlier than the Claude 4.5 generation or on Microsoft Foundry [deployments hosted on Azure](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options)
* **Subagents**: when the main conversation runs Fable, the built-in [[Create_custom_subagents|Explore subagent]] runs on Opus with a Claude subscription, an Anthropic Console account, or an [[Other_LLM_gateways|LLM gateway]] reached through `ANTHROPIC_BASE_URL`. On other providers, including Claude Platform on AWS, it runs on Fable
* **[[Commands]]**:
  * `/design-sync` and `/import` with its `claude import` subcommand form are unavailable on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and Claude Platform on AWS, and through a [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]]
  * `/voice` requires a claude.ai account
  * `/list-agents` and its alias `/peers` are available only in sessions where [[Message_your_other_Claude_Code_sessions|cross-session messaging is enabled]]

### Features that require a Claude subscription

These require signing in with a claude.ai account and are not reachable with an Anthropic Console API key or from a third-party provider:

* [[Use_Claude_Code_in_the_cloud|Cloud sessions]] and Claude Code on mobile
* [[Claude_Code_in_Slack|Claude Code in Slack]]: Pro and Max plans
* [[Desktop_application|Claude Code Desktop]]
* [[Automate_work_with_routines|Routines]] (`/schedule`)
* [[Find_bugs_with_ultrareview|Ultrareview]]
* [[Code_Review|Code Review]]: Team and Enterprise plans
* [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]
* [[Use_Claude_Code_with_Chrome|Chrome extension]]
* [[Let_Claude_use_your_computer_from_the_CLI|Computer use]]: Pro and Max plans
* [[Share_session_output_as_artifacts|Artifacts]]: Pro, Max, Team, and Enterprise plans
* [[Voice_dictation|Voice dictation]]

Desktop is the partial exception: [[Connect_Claude_Code_to_an_LLM_gateway|gateway routing can be configured in the app or by an administrator]], Enterprise deployments can route Desktop to Google Cloud's Agent Platform or a gateway provider via [managed settings](https://claude.com/docs/third-party/claude-desktop/configuration), and [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview) runs the Code tab on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or a self-hosted LLM gateway. For per-plan availability of these features, see [Availability by subscription plan](#availability-by-subscription-plan).

### CLI capabilities that vary by provider

These features work in the local CLI but depend on a server-side capability that not every provider exposes.

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Claude subscription</th>
      <th>Anthropic Console</th>
      <th>Amazon Bedrock</th>
      <th>Claude Platform on AWS</th>
      <th>Google Cloud's Agent Platform</th>
      <th>Microsoft Foundry</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[[Tools_reference|Web search]]</td>
      <td>✓</td>
      <td>✓</td>
      <td>✗</td>
      <td>✓</td>
      <td>See note <sup><a href="#fn1">1</a></sup></td>
      <td>✓</td>
    </tr>

    <tr>
      <td>[[Speed_up_responses_with_fast_mode|Fast mode]]</td>
      <td>✓ ([[Speed_up_responses_with_fast_mode|Owner-enabled]] on Team and Enterprise)</td>
      <td>✓ (provisioned organizations)</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
    </tr>

    <tr>
      <td>[[Configure_auto_mode|Auto mode]]</td>
      <td>✓</td>
      <td>✓</td>
      <td>See note <sup><a href="#fn2">2</a></sup></td>
      <td>✓</td>
      <td>See note <sup><a href="#fn2">2</a></sup></td>
      <td>See note <sup><a href="#fn2">2</a></sup></td>
    </tr>

    <tr>
      <td>[[Escalate_hard_decisions_with_the_advisor_tool|Advisor]]</td>
      <td>✓</td>
      <td>✓</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
    </tr>

    <tr>
      <td>[[Message_your_other_Claude_Code_sessions|Cross-session messaging]]</td>
      <td>✓ <sup><a href="#fn5">5</a></sup></td>
      <td>✓ (same machine) <sup><a href="#fn5">5</a></sup></td>
      <td>✓ (same machine) <sup><a href="#fn5">5</a></sup></td>
      <td>✓ (same machine) <sup><a href="#fn5">5</a></sup></td>
      <td>✓ (same machine) <sup><a href="#fn5">5</a></sup></td>
      <td>✓ (same machine) <sup><a href="#fn5">5</a></sup></td>
    </tr>

    <tr>
      <td>[[Push_events_into_a_running_session_with_channels|Channels]]</td>
      <td>✓</td>
      <td>✓</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
    </tr>

    <tr>
      <td>[[Claude_Code_GitHub_Actions|GitHub Actions]]</td>
      <td>✓</td>
      <td>✓</td>
      <td>✓</td>
      <td>✗</td>
      <td>✓</td>
      <td>✓</td>
    </tr>

    <tr>
      <td>[[Claude_Code_GitLab_CICD|GitLab CI/CD]]</td>
      <td>✓</td>
      <td>✓</td>
      <td>✓</td>
      <td>✓</td>
      <td>✓</td>
      <td>✗</td>
    </tr>
  </tbody>
</table>

### Admin and analytics

Organization-level controls and usage visibility.

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Claude subscription</th>
      <th>Anthropic Console</th>
      <th>Amazon Bedrock</th>
      <th>Claude Platform on AWS</th>
      <th>Google Cloud's Agent Platform</th>
      <th>Microsoft Foundry</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[[Track_team_usage_with_analytics|Analytics dashboard and API]]</td>
      <td>✓ (dashboard: Team and Enterprise; API: Enterprise)</td>
      <td>✓ <sup><a href="#fn4">4</a></sup></td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
    </tr>

    <tr>
      <td>[[Configure_server-managed_settings|Server-managed settings]]</td>
      <td>✓ (Team and Enterprise)</td>
      <td>✓ (Team and Enterprise)</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
      <td>✗</td>
    </tr>

    <tr>
      <td>[[Zero_data_retention|Zero Data Retention]]</td>
      <td>✓ (qualified Enterprise accounts)</td>
      <td>✓ (qualified accounts)</td>
      <td>See note <sup><a href="#fn3">3</a></sup></td>
      <td>✓ (qualified accounts)</td>
      <td>See note <sup><a href="#fn3">3</a></sup></td>
      <td>See note <sup><a href="#fn3">3</a></sup></td>
    </tr>
  </tbody>
</table>

<span id="fn1" style={{display: 'block', position: 'relative', top: '-120px'}} /><sup>1</sup> On Google Cloud's Agent Platform, web search is available for Claude 4 models and later.<br />
<span id="fn2" style={{display: 'block', position: 'relative', top: '-120px'}} /><sup>2</sup> On these providers, auto mode supports only Claude Sonnet 5 or later, Opus 4.7 or later, Haiku 5.5, and the Fable models. See [[Configure_auto_mode|Auto mode configuration]]. For the permission mode a session on these providers starts in, see [[Choose_a_permission_mode|Which mode a session starts in]]. In v2.1.158 through v2.1.206, auto mode on these providers also required setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`; v2.1.207 removed the requirement.<br />
<span id="fn3" style={{display: 'block', position: 'relative', top: '-120px'}} /><sup>3</sup> Subject to your agreement with the cloud provider.<br />
<span id="fn4" style={{display: 'block', position: 'relative', top: '-120px'}} /><sup>4</sup> Dashboard and API only. [[Track_team_usage_with_analytics|Contribution metrics]] requires a claude.ai Team or Enterprise organization.<br />
<span id="fn5" style={{display: 'block', position: 'relative', top: '-120px'}} /><sup>5</sup> Requires Claude Code v2.1.224 or later on macOS and Linux, including Linux inside WSL 2. On native Windows, requires Claude Code v2.1.234 or later. With API key authentication, messaging is same-machine only. On Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, and Microsoft Foundry, messaging is same-machine only and requires Claude Code v2.1.248 or later. Claude can find your [[Use_Claude_Code_in_the_cloud|cloud sessions]] and your sessions on other machines only from a session that is connected to [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]. To connect, you need a claude.ai sign-in and the other [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control requirements]]. See [[Message_your_other_Claude_Code_sessions|Message sessions on other machines]].

<Note>
  If you authenticate through an [[Other_LLM_gateways|LLM gateway]], feature availability matches the underlying provider the gateway forwards to, except for the features Claude Code itself turns off. Whenever `ANTHROPIC_BASE_URL` points at a host other than `api.anthropic.com`, Claude Code turns off features such as [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] and [[Configure_server-managed_settings|server-managed settings]], whatever the gateway forwards. Some Anthropic-only features such as the [[Escalate_hard_decisions_with_the_advisor_tool|Advisor]] work only if the gateway forwards requests intact to the Anthropic API.

  For how the requests Claude Code sends differ between an Amazon Bedrock- or Agent Platform-format gateway, an `ANTHROPIC_BASE_URL` gateway, and a Claude apps gateway sign-in, see [[Claude_Code_gateway_compatibility_guide|client behavior by connection method]].
</Note>

### Summary by provider

Each tab lists what is unavailable or partially supported on that provider, with alternatives where one exists. Everything not listed works the same as on a Claude subscription, apart from the [provider-specific differences](#features-available-on-every-provider) noted above. On Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and Claude Platform on AWS, error reporting and telemetry to Anthropic are off by default. See [[Data_usage|default behaviors by API provider]] for what traffic still reaches Anthropic and how to opt out.

<Tabs>
  <Tab title="Amazon Bedrock">
    **Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [[Tools_reference|web search]], [[Speed_up_responses_with_fast_mode|fast mode]], [[Escalate_hard_decisions_with_the_advisor_tool|Advisor]], [[Push_events_into_a_running_session_with_channels|Channels]], the [[Track_team_usage_with_analytics|analytics dashboard]], [[Configure_server-managed_settings|server-managed settings]], and the [[Commands|`/design-sync` and `/import` commands]].

    **Partial support:**

    * [[Desktop_application|Desktop]]: only via [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview)
    * [[Configure_auto_mode|Auto mode]]: Sonnet 5 or later, Opus 4.7 or later, Haiku 5.5, and Fable models only
    * [[Message_your_other_Claude_Code_sessions|Cross-session messaging]]: between your sessions on this machine only <sup><a href="#fn5">5</a></sup>
    * [[Zero_data_retention|Zero Data Retention]]: subject to your AWS agreement

    **Alternatives:** for scheduling, use [[Run_prompts_on_a_schedule|`/loop`]] instead of `/schedule`. For cloud sessions, use [[Claude_Code_GitHub_Actions|GitHub Actions]] or [[Claude_Code_GitLab_CICD|GitLab CI/CD]]. For web lookups, use the [[Tools_reference|WebFetch tool]] with a specific URL.
  </Tab>

  <Tab title="Claude Platform on AWS">
    **Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [[Speed_up_responses_with_fast_mode|fast mode]], [[Escalate_hard_decisions_with_the_advisor_tool|Advisor]], [[Push_events_into_a_running_session_with_channels|Channels]], [[Claude_Code_GitHub_Actions|GitHub Actions]], the [[Track_team_usage_with_analytics|analytics dashboard]], [[Configure_server-managed_settings|server-managed settings]], and the [[Commands|`/design-sync` and `/import` commands]].

    **Available where Amazon Bedrock is not:** [[Tools_reference|web search]].

    **Partial support:**

    * [[Message_your_other_Claude_Code_sessions|Cross-session messaging]]: between your sessions on this machine only <sup><a href="#fn5">5</a></sup>

    **Alternatives:** for scheduling, use [[Run_prompts_on_a_schedule|`/loop`]] instead of `/schedule`. For cloud sessions, use [[Claude_Code_GitLab_CICD|GitLab CI/CD]].
  </Tab>

  <Tab title="Google Cloud's Agent Platform">
    **Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [[Speed_up_responses_with_fast_mode|fast mode]], [[Escalate_hard_decisions_with_the_advisor_tool|Advisor]], [[Push_events_into_a_running_session_with_channels|Channels]], the [[Track_team_usage_with_analytics|analytics dashboard]], [[Configure_server-managed_settings|server-managed settings]], and the [[Commands|`/design-sync` and `/import` commands]].

    **Partial support:**

    * [[Desktop_application|Desktop]]: via [managed settings](https://claude.com/docs/third-party/claude-desktop/configuration) or [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview)
    * [[Tools_reference|Web search]]: Claude 4 models and later
    * [[Configure_auto_mode|Auto mode]]: Sonnet 5 or later, Opus 4.7 or later, Haiku 5.5, and Fable models only
    * [[Message_your_other_Claude_Code_sessions|Cross-session messaging]]: between your sessions on this machine only <sup><a href="#fn5">5</a></sup>
    * [[Zero_data_retention|Zero Data Retention]]: subject to your Google Cloud agreement

    **Alternatives:** for scheduling, use [[Run_prompts_on_a_schedule|`/loop`]] instead of `/schedule`. For cloud sessions, use [[Claude_Code_GitHub_Actions|GitHub Actions]] or [[Claude_Code_GitLab_CICD|GitLab CI/CD]].
  </Tab>

  <Tab title="Microsoft Foundry">
    **Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription), plus [[Speed_up_responses_with_fast_mode|fast mode]], [[Escalate_hard_decisions_with_the_advisor_tool|Advisor]], [[Push_events_into_a_running_session_with_channels|Channels]], [[Claude_Code_GitLab_CICD|GitLab CI/CD]], the [[Track_team_usage_with_analytics|analytics dashboard]], [[Configure_server-managed_settings|server-managed settings]], and the [[Commands|`/design-sync` and `/import` commands]].

    **Partial support:**

    * [[Desktop_application|Desktop]]: only via [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview)
    * [[Configure_auto_mode|Auto mode]]: Sonnet 5 or later, Opus 4.7 or later, Haiku 5.5, and Fable models only
    * [[Message_your_other_Claude_Code_sessions|Cross-session messaging]]: between your sessions on this machine only <sup><a href="#fn5">5</a></sup>
    * [[Zero_data_retention|Zero Data Retention]]: subject to your Azure agreement

    **Alternatives:** for scheduling, use [[Run_prompts_on_a_schedule|`/loop`]] instead of `/schedule`. For cloud sessions, use [[Claude_Code_GitHub_Actions|GitHub Actions]].
  </Tab>

  <Tab title="Anthropic Console">
    **Not available:** all [features that require a Claude subscription](#features-that-require-a-claude-subscription).

    Everything in [CLI capabilities that vary by provider](#cli-capabilities-that-vary-by-provider) is available, except that [[Speed_up_responses_with_fast_mode|fast mode]] requires [[Speed_up_responses_with_fast_mode|provisioned access]]. [[Configure_server-managed_settings|Server-managed settings]] are also available when your API key belongs to a Team or Enterprise organization.
  </Tab>
</Tabs>

## Availability by subscription plan

If you authenticate through Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or an Anthropic Console API key, this section does not apply to you. When you sign in with a claude.ai account, your plan determines which of the features below are available.

In Enterprise organizations with the [[Set_up_Claude_Code_local_mode_for_a_HIPAA-ready_organization|HIPAA configuration]] applied, some features in this table are turned off.

| Feature | Pro | Max | Team | Enterprise |
| :- | :- | :- | :- | :- |
| [[Use_Claude_Code_in_the_cloud|Cloud sessions]] | ✓ | ✓ | ✓ | ✓ <sup><a href="#fn6">6</a></sup> |
| [[Automate_work_with_routines|Routines]] | ✓ | ✓ | ✓ | ✓ |
| [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]] | ✓ | ✓ | Admin-enabled | Admin-enabled |
| [[Push_events_into_a_running_session_with_channels|Channels]] | ✓ | ✓ | Admin-enabled | Admin-enabled |
| [[Let_Claude_use_your_computer_from_the_CLI|Computer use]] | ✓ | ✓ | ✗ | ✗ |
| Dispatch ([[Desktop_application|Desktop]]) | ✓ | ✓ | ✗ | ✗ |
| [[Code_Review|Code Review]] | ✗ | ✗ | ✓ | ✓ |
| [[Share_session_output_as_artifacts|Artifacts]] | ✓ | ✓ | ✓ | ✓ |
| [[Track_team_usage_with_analytics|Analytics dashboard and contribution metrics]] | ✗ | ✗ | ✓ | ✓ |
| [[Track_team_usage_with_analytics|Enterprise Analytics API]] | ✗ | ✗ | ✗ | ✓ |
| [[Configure_server-managed_settings|Server-managed settings]] | ✗ | ✗ | ✓ | ✓ |
| [SSO](https://support.claude.com/en/articles/9266767-what-is-the-team-plan) | ✗ | ✗ | ✓ | ✓ |
| SCIM | ✗ | ✗ | ✗ | ✓ |
| [Compliance API](https://platform.claude.com/docs/en/api/compliance) | ✗ | ✗ | ✗ | ✓ |
| [[Zero_data_retention|Zero Data Retention]] | ✗ | ✗ | ✗ | ✓ <sup><a href="#fn7">7</a></sup> |

<span id="fn6" style={{display: 'block', position: 'relative', top: '-120px'}} /><sup>6</sup> On Enterprise, requires a premium seat or a Chat + Claude Code seat. See [[Use_Claude_Code_in_the_cloud|Use Claude Code in the cloud]].<br />
<span id="fn7" style={{display: 'block', position: 'relative', top: '-120px'}} /><sup>7</sup> Not included in the standard Enterprise plan. Requires separate enablement by Anthropic for qualified accounts. See [[Zero_data_retention|Zero Data Retention]].

For pricing and the full plan comparison, see [Team plans](https://support.claude.com/en/articles/9266767-what-is-the-team-plan) and [Enterprise plans](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan).

## Model availability

For which Claude models and context-window sizes are available per provider and region, see [[Model_configuration|Model configuration]] and the [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview). Vision, PDF input, and extended thinking are model capabilities rather than Claude Code features and work on every provider that offers the model. [[How_Claude_Code_uses_prompt_caching|Prompt caching]] works the same way on most providers; on Amazon Bedrock, support varies by model.

## Related resources

* [[Enterprise_deployment_overview|Enterprise deployment overview]]: compare authentication, billing, and regions across providers
* Provider setup guides: [[Claude_Code_on_Amazon_Bedrock|Amazon Bedrock]], [[Claude_Code_on_Claude_Platform_on_AWS|Claude Platform on AWS]], [[Claude_Code_on_Google_Clouds_Agent_Platform|Google Cloud's Agent Platform]], [[Claude_Code_on_Microsoft_Foundry|Microsoft Foundry]]
* [[Platforms_and_integrations|Platforms and integrations]]: where Claude Code runs, including the CLI, Desktop, IDE extensions, web, mobile, and CI/CD

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Administration_and_Security|Administration & Security MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

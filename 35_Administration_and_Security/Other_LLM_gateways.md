---
title: "Other LLM gateways"
aliases:
  - "llm-gateway"
  - "Other LLM gateways"
tags:
  - "claude-code"
  - "admin-security"
source_url: "https://code.claude.com/docs/en/llm-gateway"
status: "verified"
last_updated: "2026-10"
---

# Other LLM gateways

## Executive Summary
> Route Claude Code through an LLM gateway your organization already runs. Covers connecting Claude Code to a gateway, rolling one out for your organization, and what Claude Code sends to a gateway.

## Technical Mechanics & Documentation

This section covers using a gateway product your organization already runs, rather than [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]]. For what a gateway is, how it sits between Claude Code and your provider, and how to choose between Claude apps gateway and another product, see the [[Run_Claude_Code_through_a_gateway|gateway overview]].

<Note>
  * If you're a developer connecting to an existing gateway: [[Connect_Claude_Code_to_an_LLM_gateway|connect Claude Code to your gateway]]
  * If you're an admin rolling out a gateway for your organization: [[Roll_out_an_LLM_gateway_for_your_organization|deploy and distribute a gateway]]
  * If you're configuring a gateway product: the [[Claude_Code_gateway_compatibility_guide|gateway compatibility guide]]
</Note>

Any gateway that exposes a [[Claude_Code_gateway_compatibility_guide|supported API format]] works. Anthropic doesn't endorse, maintain, or audit third-party gateway products, and doesn't support routing Claude Code to non-Claude models through any gateway. Deploy the gateway following its own documentation, then complete the Claude Code side with the [rollout steps below](#roll-out-a-gateway).

## What a gateway provides

A gateway gives your organization one place to manage:

* **Credentials**: the provider key stays server-side; developers hold gateway credentials instead
* **Usage tracking**: attribute usage by developer or team, regardless of which provider serves the request
* **Cost controls**: enforce budgets and rate limits in one place
* **Audit logging**: log every model request for compliance
* **Provider switching**: change the provider in gateway configuration, without touching developer machines

All of these except provider switching apply whether the upstream is Anthropic's API or a [[Enterprise_deployment_overview|cloud provider]]. Provider switching without reconfiguring developer machines also depends on the gateway exposing a single [[Claude_Code_gateway_compatibility_guide|Anthropic-format endpoint]] regardless of upstream. A gateway that exposes a provider's own format ties the client configuration to that provider and changes [[Claude_Code_gateway_compatibility_guide|what Claude Code sends and which defaults it applies]].

The tradeoff is that the gateway becomes infrastructure your organization operates. Claude Code adds capabilities with each release, and a gateway that doesn't forward them breaks the corresponding features, so the gateway product needs to be kept updated as Claude Code evolves. The [[Claude_Code_gateway_compatibility_guide|gateway compatibility guide]] covers what to forward.

## Roll out a gateway

When you're ready to roll out an LLM gateway to your organization, the sequence is the same whichever gateway product you choose:

1. Deploy the gateway and give it your provider credential, so it can authenticate the requests it forwards.
2. Issue each developer a gateway credential, so usage is attributed to the developer and offboarding revokes one credential.
3. Distribute the configuration through a [[Deploy_managed_settings|managed settings file]] and your secrets tooling, so every machine receives the base URL and a credential. When both are distributed, developers don't configure anything. If you don't have settings distribution in place, developers follow the [[Connect_Claude_Code_to_an_LLM_gateway|connect page]] to set the variables themselves.
4. Have each developer [[Connect_Claude_Code_to_an_LLM_gateway|check for the configuration in Claude Code]], so distribution problems surface before they depend on the gateway.

[[Roll_out_an_LLM_gateway_for_your_organization|Roll out an LLM gateway for your organization]] walks each step and shows the configuration files to distribute at each one. The gateway is one part of organization setup; for policy enforcement, usage visibility, and data handling decisions, see [[Set_up_Claude_Code_for_your_organization|Set up Claude Code for your organization]].

To make a gateway reached through `ANTHROPIC_BASE_URL` the only destination a managed machine may use, set [[All_settings|`allowedProviders`]] to `["customEndpoint"]` in the same managed settings file and put the gateway's `ANTHROPIC_BASE_URL` in that file's `env` block. Claude Code then refuses a session pointed anywhere else, including at Anthropic directly or at a developer's own proxy, and accepts `ANTHROPIC_BASE_URL` only with the value you set there. For a gateway reached through a provider-specific endpoint variable such as `ANTHROPIC_BEDROCK_BASE_URL`, the `allowedProviders` entry says which variable to pin. Requires Claude Code v2.1.285 or later.

## Subscriptions and gateways

While a [[Connect_Claude_Code_to_an_LLM_gateway|gateway credential variable]] or `apiKeyHelper` is active, requests carry that credential in place of a developer's claude.ai subscription login, and the subscription's usage limits don't apply to them. Claude Code keeps a saved claude.ai login on the machine but doesn't send it with those requests. That traffic is billed per token to whoever owns the credential the gateway forwards, such as your organization's Anthropic Console account, or your Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry account when the gateway routes there.

[[Connect_Claude_Code_to_an_LLM_gateway|`ANTHROPIC_BASE_URL`]] is the variable that points Claude Code at the gateway. Setting only that variable, without a gateway credential, doesn't replace the subscription. Requests still route through the gateway, but a saved claude.ai login remains the active credential, so its usage limits and billing apply. Gateways that pass this traffic on to Anthropic must forward the OAuth capability in `anthropic-beta`; see the [[Claude_Code_gateway_compatibility_guide|request headers reference]].

## Related pages

* [[Run_Claude_Code_through_a_gateway|Gateway overview]]: how a gateway works and how to choose between Claude apps gateway and another product
* [[Claude_apps_gateway_for_Amazon_Bedrock_Claude_Platform_on_AWS_Google_Cloud_and_Microsoft_Foundry|Claude apps gateway]]: Anthropic's self-hosted gateway with SSO sign-in and OTLP telemetry
* [[Connect_Claude_Code_to_an_LLM_gateway|Connect Claude Code to an LLM gateway]]: set the base URL and credential on your own machine, with per-surface configuration and a troubleshooting table
* [[Roll_out_an_LLM_gateway_for_your_organization|Roll out an LLM gateway for your organization]]: the admin checklist for deploying a gateway, issuing developer credentials, and distributing managed settings
* [[Claude_Code_gateway_compatibility_guide|Gateway compatibility guide]]: what Claude Code sends to a gateway, for operators configuring one, covering endpoints, headers to forward, and feature pass-through

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Administration_and_Security|Administration & Security MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

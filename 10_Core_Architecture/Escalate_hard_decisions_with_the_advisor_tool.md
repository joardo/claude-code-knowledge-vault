---
title: "Escalate hard decisions with the advisor tool"
aliases:
  - "advisor"
  - "Escalate hard decisions with the advisor tool"
tags:
  - "claude-code"
  - "architecture"
source_url: "https://code.claude.com/docs/en/advisor"
status: "verified"
last_updated: "2026-10"
---

# Escalate hard decisions with the advisor tool

## Executive Summary
> Pair your main model with a stronger advisor model that Claude consults at key moments during a task.

## Technical Mechanics & Documentation

<Note>
  The advisor tool is experimental and requires the Anthropic API. It is not available on Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, or Microsoft Foundry. Behavior, pricing, and availability may change.
</Note>

The advisor tool lets Claude consult a second, typically stronger model at key moments during a task, such as before committing to an approach, when stuck on a recurring error, or before declaring a task complete. The advisor receives the full conversation, including every tool call and result, and returns guidance that Claude applies before continuing.

The advisor runs server-side on Anthropic's infrastructure as a [server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool), available to both subscription and API-billed accounts. You choose which model acts as the advisor, and Claude decides when to call it.

This page covers how to enable the advisor, which model pairings are accepted, what Claude shows during a consultation, and how advisor usage is billed.

## When to use the advisor

The advisor fits long, multi-step tasks where most turns are routine but plan quality determines the outcome. Examples include large refactors, debugging sessions where an error keeps recurring, and tasks you want independently checked before Claude declares them done.

It adds less value on short tasks where there is little to plan, or on work where every turn needs the strongest model. For those, [[Model_configuration|switch the main model]] instead, or see [how the advisor compares with opusplan and subagents](#compare-with-related-features) for other ways to get a second opinion.

## Enable the advisor

You can set the advisor model in three ways:

* **`/advisor` command**: set or change the advisor mid-session and save it as your default
* **`advisorModel` setting**: configure a persistent default in your [[Settings_files_and_precedence|settings file]]
* **`--advisor` flag**: set the advisor for a single session at launch

Each of these enables the advisor for sessions whose main model [supports it](#choose-an-advisor-model). After the session starts, Claude Code shows an `Advisor Tool (experimental) is on and may use more tokens · /advisor` notification. To stop using the advisor, see [Turn the advisor off](#turn-the-advisor-off).

On some plans, Fable as the advisor also needs your one-time [[Model_configuration|consent to bill Fable usage to usage credits]]. For what happens before you have given that consent, see [Fable advisor and usage credits](#fable-advisor-and-usage-credits).

### Use the `/advisor` command

Run `/advisor` without arguments to open a picker listing the available advisor models, or pass the model directly:

```
/advisor opus
```

The command confirms with `Advisor set to` followed by the advisor model name. Your selection is saved to `advisorModel` in your user settings and persists across sessions, except in the cases the [[All_settings|`advisorModel` entry]] lists as applying to the current session only.

The command also works where there is no terminal picker: in [[Run_Claude_Code_programmatically|non-interactive mode]] with `-p`, in the Agent SDK, in the desktop app, and over [[Continue_local_sessions_from_any_device_with_Remote_Control|Remote Control]]. This requires Claude Code v2.1.260 or later. On those surfaces:

* Run `/advisor` with no argument to print the current advisor model and the aliases it accepts.
* Run `/advisor` with a model, such as `/advisor opus`, to set it.
* Run `/advisor off` to turn it off.

Claude Code doesn't invoke a saved advisor that your organization's [[Model_configuration|`availableModels`]] allowlist excludes. To use the advisor, pick an allowed model with `/advisor`.

Claude Code still saves an advisor that your current main model doesn't support. That advisor activates after you switch to a [compatible main model](#choose-an-advisor-model) with [[Model_configuration|`/model`]]. If the API already refused the saved advisor in the current conversation, it stays off until `/clear` or `/compact`, even after you switch models.

On some plans, Fable as the advisor also needs your one-time [[Model_configuration|consent to bill Fable usage to usage credits]]. For what `/advisor fable` does before you have given that consent, see [Fable advisor and usage credits](#fable-advisor-and-usage-credits).

### Set `advisorModel` in settings

To configure the advisor as a default without opening a session, set it in your settings file:

```json theme={null}
{
  "advisorModel": "opus"
}
```

### Use the `--advisor` flag

To set the advisor for a single session without changing your saved setting, launch with the flag:

```bash theme={null}
claude --advisor opus
```

Claude Code uses the flag instead of the `advisorModel` setting for that session. It doesn't list `--advisor` in `claude --help`. Claude Code exits with an error at launch if:

* The session's main model doesn't support the advisor
* The requested model, such as Haiku 4.5, can't act as an advisor
* Your organization's [[Model_configuration|`availableModels`]] allowlist excludes the requested model
* You requested Fable and your account still requires the [usage-credits consent](#fable-advisor-and-usage-credits)

If you start a [[Manage_multiple_agents_with_agent_view|background session]] with `--advisor` and one of these applies, Claude Code starts the session without the advisor instead of exiting.

If the requested model can act as an advisor but [ranks below](#choose-an-advisor-model) the session's main model, Claude Code starts the session anyway. Outside background sessions, it also warns at launch that the model `cannot advise` the main model.

## Choose an advisor model

Claude Code ranks models by capability for the advisor role, and an advisor must rank at or above your session's main model. Rows run from the lowest-ranked main model to the highest:

| Main model | Accepted advisors |
| - | - |
| Haiku 4.5 | Fable, Opus, Sonnet, Haiku 5.5 |
| Sonnet 4.6 | Fable, Opus, Sonnet, Haiku 5.5 |
| Opus 4.6 | Fable, Opus, Sonnet 5 or later, Haiku 5.5 |
| Sonnet 5 or Haiku 5.5 | Fable, Opus 4.7 or later, Sonnet 5 or later, Haiku 5.5 |
| Opus 4.7 or Opus 4.8 | Fable, Opus 4.7 or later, Sonnet 5.5 |
| Sonnet 5.5 | Fable, Opus 5 or later, Sonnet 5.5 |
| Opus 5 or Opus 5.5 | Fable, Opus 5 or later |
| Fable 5 | Fable 5.1 or Fable 5 |
| Fable 5.1 | Fable 5.1 |

Fable 5.1 requires Claude Code v2.1.257 or later. Fable models require [[Model_configuration|Fable access]]. Sonnet 5.5 as the advisor for an Opus 4.7 or Opus 4.8 main model requires Claude Code v2.1.287 or later. Haiku 5.5 as the main model or as the advisor requires Claude Code v2.1.293 or later.

Set the advisor as `fable`, `opus`, or `sonnet`. These aliases resolve to Claude Code's [[Model_configuration|built-in default version]] for each model family, which advances with new Claude Code releases. You can also pass a full model ID such as `claude-opus-5-5` or `claude-haiku-5-5`. Haiku 4.5 can call the advisor but can't act as one.

Subagents inherit the configured advisor and apply the same pairing check against their own model.

Claude Code validates the pairing before sending a request, and the API validates it again:

* For an advisor that ranks below the main model, Claude Code doesn't attach it to the main model's requests. The `/advisor` command output and a notification show this; see [[Error_reference|Advisor is less capable than the current main model]]. Subagents whose own model satisfies the pairing may still use the advisor.
* If the API refuses the pairing of an advisor that Claude Code attached, Claude Code resends that request without the advisor. The conversation continues without one, so you see no error and get no advisor calls. If you then pick a different advisor with `/advisor`, it takes effect after `/clear` or `/compact` and in new sessions.
* If the main model or the advisor is a model Claude Code does not recognize, the advisor is not attached.

### Fable advisor and usage credits

On some plans, Fable usage bills to usage credits, and Fable as the advisor bills the same way. If your account requires the [[Model_configuration|one-time consent to bill Fable usage to usage credits]], Claude Code asks for it when you select a Fable model with `/model` and doesn't apply Fable as the advisor until you have accepted that consent.

Before you have accepted it, Claude Code doesn't save Fable as the advisor when you type `/advisor fable` or pick Fable in the `/advisor` picker. It points you to `/model fable` instead. With `claude --advisor fable`, Claude Code exits at launch with a message that points to `/model fable`. In a [background session](#use-the-advisor-flag), it starts the session without the advisor instead of exiting. With Fable already saved as your `advisorModel`, Claude Code sends requests without the advisor. In an interactive session whose main model supports the advisor, it also shows a notification that points to `/model fable`.

To accept the consent, run `/model fable` and choose to continue on Fable. Claude Code records the consent and [[Model_configuration|saves Fable as your selected model]]. Then select Fable as the advisor.

### Common model pairings

Any accepted pairing works. These combinations balance cost against capability in different ways:

| Pairing | When to use |
| - | - |
| Sonnet main + Opus advisor | Sonnet handles routine work and escalates planning, ambiguous failures, and completion checks to Opus |
| Sonnet main + Fable advisor | Fable guidance at decision points without running Fable throughout. Requires Fable access |
| Haiku main + Opus advisor | Lowest-cost main model with strong planning. Expect higher cost than Haiku alone but lower than switching the main model to Sonnet or Opus |
| Opus main + Opus advisor | A second Opus reviews the first. Useful for high-stakes tasks where an independent check matters more than cost |
| Fable main + Fable advisor | Highest-capability pairing when Fable is available. Claude Code doesn't apply an Opus or Sonnet advisor to a Fable main model |
| Sonnet main + Sonnet advisor | A lower-cost second opinion for catching routine oversights |

## When Claude consults the advisor

Claude decides when to call the advisor. It tends to consult before committing to an approach, when an error keeps recurring, and before declaring a task done, but the timing is model-driven rather than rule-based.

You can ask for a consultation in your prompt the same way you would request any tool, for example `consult the advisor before you continue`. There is no setting to cap or force advisor calls; if you want Claude to consult more or less often during a task, say so in your instructions.

## What you see during a session

When Claude calls the advisor, the transcript shows an `Advising` line with the advisor model name while the call is in progress. When the result returns, the line reports whether the advisor gave guidance:

* **Reviewed**: the line confirms that the advisor has reviewed the conversation. When the advisor returned readable guidance, press `Ctrl+O` to read it.
* **Declined**: the line reads `Advisor declined to advise on this request`. If the advisor gave a reason, press `Ctrl+O` to read it.
* **Unavailable**: the advisor call failed, and the line reads `Advisor unavailable (<error_code>)`, where `<error_code>` is the code the call returned.

Claude generally follows the advisor's guidance, but adapts when its own evidence contradicts a specific claim: if a recommended step fails when tried, or the file contents contradict the advice, Claude surfaces the conflict rather than following the guidance unconditionally.

The advisor always receives the full conversation, and Claude controls the timing. For more control or a different configuration, see [how the advisor compares with subagents and opusplan](#compare-with-related-features).

## Cost

When Claude calls the advisor, the advisor model reads the conversation, so each call consumes tokens at the advisor model's rates in addition to your main model's usage. How those advisor tokens are billed depends on how you pay:

* **API billing**: you pay the advisor model's input and output rates for advisor tokens
* **Subscription plans**: advisor usage counts toward your plan's usage limits, except that a Fable advisor bills to [[Model_configuration|usage credits]] on plans where Fable usage does

If your account requires the usage-credits consent, a Fable advisor bills nothing before you give it, because Claude Code [doesn't apply the selection](#fable-advisor-and-usage-credits) until then.

Claude calls the advisor at decision points rather than on every turn, so pairing a faster main model with a stronger advisor typically costs less than running the stronger model throughout. Advisor usage counts toward the session totals shown by [[Manage_costs_effectively|`/usage`]].

For how advisor tokens are reported in API responses, see [Usage and billing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#usage-and-billing) in the Claude API documentation.

## Impact on prompt caching

Enabling or disabling the advisor mid-session does not invalidate your main model's [[How_Claude_Code_uses_prompt_caching|prompt cache]]. Unlike [[How_Claude_Code_uses_prompt_caching|switching models]], toggling `/advisor` keeps the cached prefix intact, and the advisor's returned guidance is cached as part of the transcript on later turns.

The advisor model's own read of the conversation is not cached. Each advisor call processes the full transcript anew, with no reuse between calls.

## Requirements

The advisor tool requires all of the following:

* **Anthropic API only**: the advisor is a server-executed tool. It is not available on Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, or Microsoft Foundry. Through an [[Other_LLM_gateways|LLM gateway]] configured with `ANTHROPIC_BASE_URL`, availability depends on whether the gateway forwards the request intact to the Anthropic API. If the gateway or its upstream doesn't recognize the advisor tool, see [[Claude_Code_gateway_compatibility_guide|Automatic retry and error forwarding]] for how Claude Code responds.
* **Supported main model**: Fable, Opus 4.6 or later, Sonnet 4.6 or later, Haiku 4.5, or Haiku 5.5. See [Choose an advisor model](#choose-an-advisor-model) for which advisors each accepts.
* **Feature-flag fetching**: Claude Code turns the advisor on through a feature flag it fetches from Anthropic. In a session where a variable that turns flag fetching off is set, such as `DISABLE_TELEMETRY`, the advisor stays off. See [[Environment_variables|Features that need feature-flag fetching]].

## Turn the advisor off

To stop using the advisor, run `/advisor off` or choose **No advisor** in the `/advisor` picker:

```
/advisor off
```

To disable the advisor tool entirely, set `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1`. The `/advisor` command becomes unavailable and any configured `advisorModel` is ignored. The `--advisor` flag is accepted but has no effect. See [[Environment_variables|Environment variables]].

## Compare with related features

The advisor is one of several ways to combine model strengths. Pick based on when you want a second model involved.

| Approach | When the stronger model runs | How it starts |
| - | - | - |
| Advisor tool | At decision points mid-task | Claude calls it when it needs guidance |
| [[Model_configuration|`opusplan`]] | During plan mode when [[Model_configuration|allowed by `availableModels`]], then switches to Sonnet for execution | You enter plan mode |
| [[Create_custom_subagents|Subagents]] with `model` set | For the entire delegated subtask | Claude delegates, or you invoke the subagent |
| [[Model_configuration|`/model`]] | From the next request onward | You switch models |

## See also

* [[Model_configuration|Model configuration]]: switch models, set effort levels, and use `opusplan`
* [[Manage_costs_effectively|Manage costs effectively]]: track token usage across models
* [Advisor tool in the Claude API](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool): understand the underlying server tool, or use it directly from the Messages API
* [The advisor strategy](https://claude.com/blog/the-advisor-strategy): why pairing a fast main model with a stronger advisor works

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Core_Architecture|Core Architecture MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

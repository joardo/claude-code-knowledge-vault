---
title: "Plugins overview"
aliases:
  - "plugins/overview"
  - "Plugins overview"
tags:
  - "claude-code"
  - "extensibility"
source_url: "https://code.claude.com/docs/en/plugins/overview"
status: "verified"
last_updated: "2026-10"
---

# Plugins overview

## Executive Summary
> Understand what a Claude Code plugin is, when you need one instead of a standalone skill or MCP server, and which page to read to install or create one.

## Technical Mechanics & Documentation

A Claude Code plugin is a directory of skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit. Most plugins come from a marketplace, which is a catalog that lists plugins and where to fetch each one. You can also load a plugin from a folder someone gives you, or [[Create_a_Claude_Code_plugin|build your own]].

<Note>
  These cases are covered on other pages:

  * **You use claude.ai chat or Cowork and not Claude Code**: see [Plugins on claude.ai and in Cowork](https://claude.com/docs/plugins/overview)
  * **You built an MCP server and want it in Anthropic's directory**: see [Publish to the directory](https://claude.com/docs/directory/publish)
  * **You want Claude Code inside VS Code or a JetBrains IDE**: that's the VS Code extension or the JetBrains plugin, not a Claude Code plugin. See [[Use_Claude_Code_in_VS_Code|Use Claude Code in VS Code]] or [[JetBrains_IDEs|JetBrains IDEs]]
</Note>

To try a plugin now, run `/plugin` in a Claude Code terminal session and install one from the **Discover** tab, which lists the plugins from your marketplaces. From there:

* [[Install_and_manage_plugins|Install and manage plugins]]: the full install steps, scopes, and other surfaces
* [[Create_a_Claude_Code_plugin|Create a plugin]]: build your own
* [Decide whether you need a plugin](#decide-whether-you-need-a-plugin): whether a plugin is the right tool for what you want

## Understand what a plugin is

A plugin is a directory of components, usually with a manifest. The manifest, a JSON file at `.claude-plugin/plugin.json`, gives the plugin its name and can add a version, a description, and other [[Plugin_manifest_reference|metadata]]. The components are what the plugin adds to Claude Code, such as:

* [[Add_components_to_a_plugin|**Skills**]]: `SKILL.md` instructions Claude loads when relevant, and that you can also run as a command
* [[Add_components_to_a_plugin|**Agents**]]: subagent definitions Claude can delegate to
* [[Add_components_to_a_plugin|**Hooks**]]: commands Claude Code runs at points in its lifecycle, such as after every edit
* [[Mods_overview|**A hooks module**]]: hooks written as JavaScript functions, which can also draw panes and add commands. A plugin that has one is called a mod
* [[Add_components_to_a_plugin|**MCP servers**]]: tool servers Claude Code connects to while the plugin is enabled

This diagram shows a plugin named `my-plugin` that holds a skill, an agent, hooks, and an MCP server, and what you get from each file once the plugin loads.

<img src="https://mintcdn.com/claude-code/2Q_GtOEovg5qaBem/images/plugin-directory.svg?fit=max&auto=format&n=2Q_GtOEovg5qaBem&q=85&s=f623b64e82713b830e48174f0a922888" className="dark:hidden" alt="Diagram in two columns joined by five straight arrows. Left, the directory of a plugin named my-plugin, holding a manifest at .claude-plugin/plugin.json, skills/review/SKILL.md, agents/reviewer.md, hooks/hooks.json, .mcp.json, and other components. Right, what each file gives you in your session: the manifest sets the plugin name, my-plugin; the skill runs as /my-plugin:review; the agent file is a subagent Claude can delegate to; the hooks file holds hooks that run on lifecycle events; and .mcp.json adds an MCP server that gives Claude tools." width="760" height="336" data-path="images/plugin-directory.svg" />

<img src="https://mintcdn.com/claude-code/2Q_GtOEovg5qaBem/images/plugin-directory-dark.svg?fit=max&auto=format&n=2Q_GtOEovg5qaBem&q=85&s=17ee2bd45b63154fcc148ae1d1f736d8" className="hidden dark:block" alt="Diagram in two columns joined by five straight arrows. Left, the directory of a plugin named my-plugin, holding a manifest at .claude-plugin/plugin.json, skills/review/SKILL.md, agents/reviewer.md, hooks/hooks.json, .mcp.json, and other components. Right, what each file gives you in your session: the manifest sets the plugin name, my-plugin; the skill runs as /my-plugin:review; the agent file is a subagent Claude can delegate to; the hooks file holds hooks that run on lifecycle events; and .mcp.json adds an MCP server that gives Claude tools." width="760" height="336" data-path="images/plugin-directory-dark.svg" />

For every component type a plugin can hold, with an example of each, see [[Add_components_to_a_plugin|Plugin components]]. To see where each piece is located in a plugin's directory, use the [[Add_components_to_a_plugin|plugin explorer]] on that page.

### Decide whether you need a plugin

Skills, subagents, hooks, and MCP servers all work on their own, without a plugin. A skill you save in `~/.claude/skills/`, for example, is available in every project on your machine. To set one up on its own, see [[Extend_Claude_with_skills|Skills]], [[Create_custom_subagents|Subagents]], [[Automate_actions_with_hooks|Hooks]], or [[Connect_Claude_Code_to_tools_via_MCP|MCP]].

Use a plugin when you want several skills, subagents, hooks, or MCP servers packaged as one unit. Install one to get a setup someone else built, with one command and updates from its marketplace. Make one to give your own setup to teammates, install it in many projects, or publish versioned releases.

### What an enabled plugin adds to your sessions

An enabled plugin is part of every session, not only the sessions where you use it. That has a few consequences worth knowing before you install one:

* **Context and usage**: for each skill, agent, and command that [[Extend_Claude_with_skills|Claude can invoke on its own]], the name and description are in Claude's context on every turn so that Claude knows it exists. Those tokens count toward your usage and leave less room in the [[Explore_the_context_window|context window]] even in sessions where nothing from the plugin runs. The full text of a skill or agent loads only when it's used. What the plugin's MCP servers add per turn follows [[Connect_Claude_Code_to_tools_via_MCP|MCP tool search]].
* **Processes**: MCP servers the plugin defines run alongside each session where it's enabled, and its hooks fire at their events.
* **Permissions**: what the plugin runs, it runs as you. See [[Plugin_security_and_trust|Plugin security and trust]] for what to review first.

You can check a plugin's footprint at each stage:

* **Before you install**: open the plugin from the **Marketplaces** tab in `/plugin`. Plugins in Anthropic's official marketplace show a **Context cost** estimate there.
* **After you install**: [[Measure_plugin_cost_and_usage|Measure what a plugin costs]] shows how to read a plugin's footprint, and the **Installed** tab's **Not used recently** group lists plugins you could turn off.
* **To stop it without uninstalling**: disable the plugin with `/plugin` or, in your shell, `claude plugin disable`. See [[Install_and_manage_plugins|Manage installed plugins]].

## Get plugins from a marketplace

A marketplace is a repository or directory with a `.claude-plugin/marketplace.json` file that lists plugins and where to fetch each one. It's a catalog, not a hosted store. You add a marketplace once, then install plugins from it by name, such as `commit-commands@claude-plugins-official`.

<Note>
  A plugin marketplace isn't [Claude Marketplace](https://claude.com/marketplace). Claude Marketplace is the website at claude.com/marketplace where you browse plugins, connectors, partner products, and service partners. It isn't a marketplace you add with `/plugin marketplace add`.
</Note>

Claude Code adds Anthropic's official marketplace the first time you start an interactive terminal session, unless a [[Manage_Claude_Code_plugins_for_your_organization|managed policy]] blocks it. Claude Code doesn't add Anthropic's community and demo marketplaces on its own. To distinguish the three Anthropic marketplaces, read [[Anthropics_marketplaces|Anthropic's marketplaces]]. To see what the official one lists, open the **Discover** tab of `/plugin` in a session or browse [Claude Marketplace](https://claude.com/marketplace/plugins).

This diagram shows the path from a marketplace to your session. A marketplace lists a plugin, you install that plugin, and Claude Code loads its components.

<img src="https://mintcdn.com/claude-code/2Q_GtOEovg5qaBem/images/plugins-model.svg?fit=max&auto=format&n=2Q_GtOEovg5qaBem&q=85&s=4196344954b7c2e27fc0bd6a9a1113a1" className="dark:hidden" alt="Diagram of the marketplace path in three boxes, left to right. A marketplace, a catalog of plugins, lists a plugin. The plugin is one directory installed as a unit, holding skills, agents, hooks, MCP servers, and other components. You install the plugin into Claude Code, which loads its components." width="760" height="252" data-path="images/plugins-model.svg" />

<img src="https://mintcdn.com/claude-code/2Q_GtOEovg5qaBem/images/plugins-model-dark.svg?fit=max&auto=format&n=2Q_GtOEovg5qaBem&q=85&s=f6cdefe1fc05daf3b253d26e9f3f70f6" className="hidden dark:block" alt="Diagram of the marketplace path in three boxes, left to right. A marketplace, a catalog of plugins, lists a plugin. The plugin is one directory installed as a unit, holding skills, agents, hooks, MCP servers, and other components. You install the plugin into Claude Code, which loads its components." width="760" height="252" data-path="images/plugins-model-dark.svg" />

[[Install_and_manage_plugins|Install and manage plugins]] has the install steps for each place you run Claude Code. While you're developing a plugin, you don't need a marketplace: load it straight from its folder with `--plugin-dir`, as [[Create_a_Claude_Code_plugin|Develop without a marketplace]] shows.

### Make an installed plugin available in your session

Before a plugin you installed gives you a skill you can run, it has to be present at each of these layers:

* **Settings**: your settings list the marketplaces you've added and the plugins that are enabled.
* **Disk**: `~/.claude/plugins/` holds what Claude Code has fetched and installed.
* **Session**: plugins load at startup, or when you [[Plugin_loading_reference|reload plugins]].

Read [[Plugin_loading_reference|Plugin loading reference]] for the rules at each layer, including which settings file takes precedence and where the files are on disk.

## Tell Anthropic's marketplaces from third-party ones

A marketplace's name places it in one of three tiers. Claude Code accepts the official and community names only for marketplaces sourced from `github.com/anthropics/` repositories:

* **Official**: marketplaces with one of Anthropic's [[Plugin_security_and_trust|official marketplace names]], including `claude-plugins-official` and the demo marketplace `claude-code-plugins`.
* **Community**: marketplaces with one of Anthropic's community names, such as `claude-community`. [[Plugin_security_and_trust|Identify Anthropic's marketplaces by name]] lists them.
* **Third-party**: every other marketplace. A marketplace your coworker or your organization publishes is third-party.

Whatever the tier, a plugin you install can run code with your user privileges. Read [[Plugin_security_and_trust|Plugin security and trust]] for how to review a plugin before you install it.

Through [[Settings_files_and_precedence|managed settings]], an organization can allowlist or block marketplaces, force-install plugins, and turn off session-only loading. Read [[Manage_Claude_Code_plugins_for_your_organization|Manage plugins for your organization]] for those controls.

## Understand install scopes

When you install a plugin, you pick a scope, and the scope decides who the plugin is enabled for:

* **User scope**: enabled for you in every project on this computer
* **Project scope**: enabled for everyone who works in this repository, through the committed `.claude/settings.json`. Each collaborator still [[Plugin_loading_reference|installs it on their own machine]]
* **Local scope**: enabled for you in this repository only

A plugin you install at user scope in the terminal, the desktop app's local sessions, or the VS Code extension is available in the other two on that computer, because all three read the same settings files. See [[Install_and_manage_plugins|Choose an install scope]] for how to pick one.

A cloud session, including one in the browser at claude.ai/code, doesn't load the plugins in your local settings. For install steps in the terminal, VS Code, and the desktop app, and for what a cloud session loads, see [[Install_and_manage_plugins|Install a plugin]].

<Note>
  The same plugin format also installs on claude.ai and in Cowork, where a different set of components loads. For those surfaces, see [Plugins on claude.ai and in Cowork](https://claude.com/docs/plugins/overview) on claude.com and its [component support table](https://claude.com/docs/plugins/platform-support#compare-component-support-by-app).
</Note>

## Next steps

Most people start by installing a plugin from Anthropic's official marketplace, which Claude Code adds the first time you start an interactive terminal session. Run `/plugin` in a terminal session to browse it, or follow [[Install_and_manage_plugins|Install and manage plugins]], which also covers the desktop app and VS Code. To see what's in that marketplace before you open Claude Code, browse [Claude Marketplace](https://claude.com/marketplace/plugins) on the web.

To build your own, [[Create_a_Claude_Code_plugin|Create a plugin]] starts with an empty directory and ends with a working plugin.

Once you've installed or built a plugin, these pages cover what comes next:

* **Share what you built**: [[Publish_and_distribute_a_plugin|Publish and distribute a plugin]], through your own marketplace or [[Publish_and_distribute_a_plugin|Anthropic's directory]]
* **Check whether it works and is used**: [[Test_plugins_with_evals|Test plugins with evals]] and [[Measure_plugin_cost_and_usage|Measure plugin cost and usage]]
* **Run a marketplace for your team**: [[Create_a_marketplace|Create a marketplace]], then [[Host_and_maintain_a_marketplace|Host and maintain a marketplace]]
* **Set plugin policy for an organization**: [[Manage_Claude_Code_plugins_for_your_organization|Manage plugins for your organization]]
* **Fix a problem**: [[Troubleshoot_plugins|Troubleshoot plugins]]

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Extensibility_and_MCP|Extensibility & MCP MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

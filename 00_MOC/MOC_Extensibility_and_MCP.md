---
title: "MOC: Extensibility, MCP & Plugins"
aliases:
  - "MOC_Extensibility_and_MCP"
tags:
  - "claude-code"
  - "moc"
  - "extensibility"
  - "mcp"
status: "verified"
last_updated: "2026-10"
---

# MOC: Extensibility, MCP & Plugins

> Extending Claude Code's capabilities through Model Context Protocol (MCP), custom skills, modular plugins, and terminal UI mods.

## 1. Model Context Protocol (MCP)
- [[Connect_to_MCP_servers|Connect to MCP Servers Quickstart]]: Fast setup for stdio and HTTP/SSE MCP servers.
- [[Connect_Claude_Code_to_tools_via_MCP|Connect Claude Code to Tools via MCP]]: Comprehensive guide to MCP configurations, authentication, and custom servers.
- [[Control_MCP_server_access_for_your_organization|Managed MCP Configuration]]: Enterprise restriction allowlists and global server distribution.

## 2. Skills & Custom Commands
- [[Extend_Claude_with_skills|Extend Claude with Skills]]: Authoring custom reusable skills, YAML metadata, and slash commands.
- [[Share_session_output_as_artifacts|Share Session Output as Artifacts]]: Generating interactive web artifacts and sharing links.

## 3. Plugins Ecosystem
- [[Plugins_overview|Plugins Overview]]: Understanding the plugin packaging model.
- [[Install_and_manage_plugins|Install and Manage Plugins]]: Installing from registries, local paths, and git repos.
- [[Anthropics_marketplaces|Anthropic's Marketplaces]]: Official, community, and partner marketplaces.
- [[Code_intelligence_plugins|Code Intelligence Plugins]]: Integrating Language Server Protocol (LSP) for compiler diagnostics and symbol search.
- [[Create_a_Claude_Code_plugin|Create a Claude Code Plugin]]: Step-by-step authoring of new plugins.
- [[Add_components_to_a_plugin|Add Components to a Plugin]]: Bundling skills, hooks, and MCP servers into single packages.
- [[Plugin_dependencies|Plugin Dependencies]]: SemVer dependency resolution.
- [[Test_plugins_with_evals|Test Plugins with Evals]]: Automated test suites and performance evaluation.
- [[Publish_and_distribute_a_plugin|Publish and Distribute a Plugin]]: Releasing to marketplaces.
- [[Plugin_manifest_reference|Plugin Manifest Reference]]: Complete `plugin.json` schema.

## 4. Mods (UI & Event Interceptors)
- [[Mods_overview|Mods Overview]]: Enhancing the terminal interface and tool interceptors.
- [[Mod_Create_a_mod|Create a Mod]]: Writing custom JavaScript/TypeScript mods.
- [[Mods_reference|Mods Reference]]: Mod APIs, lifecycle hooks, and render targets.
- [[Mod_Draw_in_the_interface_with_a_mod|Draw in Interface]]: Custom panels, status bars, and UI widgets.
- [[Mod_React_to_events_with_a_mod|React to Events]]: Intercepting prompts, tool calls, and LLM turns.

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Hooks_and_Automation|Hooks & Automation]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

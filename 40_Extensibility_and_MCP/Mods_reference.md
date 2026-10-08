---
title: "Mods reference"
aliases:
  - "plugins/mods/reference"
  - "Mods reference"
tags:
  - "claude-code"
  - "extensibility"
source_url: "https://code.claude.com/docs/en/plugins/mods/reference"
status: "verified"
last_updated: "2026-10"
---

# Mods reference

## Executive Summary
> Complete reference for Claude Code mods: hooks module layout, events, mods API methods, render sites, elements by surface, limits, and settings.

## Technical Mechanics & Documentation

Look up any event a [[Mods_overview|mod]] can handle, mods API method it can call, or render site it can draw in, for the Claude Code CLI and the Desktop app as of v2.1.290. Each entry gives the name and a one-line description, and links to the guide section that explains it where there is one.

<Note>
  The complete reference is Claude Code's [TypeScript declarations for mods](https://github.com/anthropics/claude-code/blob/main/mods/types/claude-code.d.ts), which describe every event, method, and element, with examples. The copy on GitHub can be older than the Claude Code version you have installed. When the two disagree, trust [[Mod_Create_a_mod|the copy Claude Code writes for your version]].
</Note>

## Files

A mod is a plugin directory with these files:

| File | Required | Contents |
| :- | :- | :- |
| `.claude-plugin/plugin.json` | Yes | The plugin [[Plugin_manifest_reference|manifest]]. Mods add no required fields. |
| `hooks/hooks.json` | Yes | `modules`: an array with one path, relative to this file, to the hooks module, as in `"modules": ["./register.js"]`. Can also hold [[Hooks_reference|settings hooks]] under `hooks`. |
| The hooks module, such as [[Mod_Create_a_mod|`hooks/register.js`]] | Yes | The mod's entry point. Exports `register(on, options)`. Named `.js`, `.mjs`, `.cjs`, `.jsx`, `.ts`, `.mts`, `.cts`, or `.tsx`. An ES module. |
| [[Mod_Draw_in_the_interface_with_a_mod|`types/index.d.ts`]], named by `types` in the manifest | When the mod uses `$.state` or adds a namespace to the mods API | Declares `PluginState` values and any namespace the mod adds |
| Files whose names end in `.test.ts` or `.test.tsx` | No | Tests that [[Mod_Test_a_mod|`claude plugin test`]] runs |

`register` receives `on` and `options`. `options` holds the values of the [[Add_components_to_a_plugin|`userConfig`]] fields the manifest declares, with defaults filled in.

## The hook function

A mod registers each of its hooks, which are event handlers, by calling `on` inside `register`. `on` takes the event's name, an optional [[Mod_React_to_events_with_a_mod|matcher]], which is a filter on the event's fields, and the hook, as in `on('tool.call', { tool: 'Bash' }, async ($, e, next) => next(e))`. `on` returns a registration with one method, `.catch(handler)`, which sets the hook's [[Mod_React_to_events_with_a_mod|error handler]].

| Argument | What it is |
| :- | :- |
| [[Mod_React_to_events_with_a_mod|`$`]] | The mods API: every method in [mods API methods](#mods-api-methods). Write each call in full, namespace then method, as in `$.fs.read('notes.md')`. |
| [[Mod_React_to_events_with_a_mod|`e`]] | The event's input, as deeply frozen plain data. To change it, pass a copy to `next`. |
| [[Mod_React_to_events_with_a_mod|`next(e)`]] | The next handler, as in middleware. Runs the hooks after this one, then Claude Code's behavior. Resolves to the event's result. |
| [[Mod_Use_the_mods_API|`next.signal`]] | An `AbortSignal` that aborts when the event is abandoned |
| `next.origin` | `{ plugin, tier }` of whoever fired the event. Claude Code itself is `{ plugin: 'engine', tier: 'core' }`. A mod's `tier` is its priority group in the [[Mod_React_to_events_with_a_mod|order mods run in]]: `prepend`, `user`, `append`, or `builtin`. |
| `next.budget` | The hook's time limit in milliseconds: `next.budget.ms` is the whole limit, and `next.budget.remainingMs` is what's left now |
| `next.to(e, tier)` | Skips to a later tier, which is `append`, `builtin`, or `core`. `next.to(e, 'append')` skips the mods a user installed. Only a mod in `prependPlugins` or `appendPlugins` can call it. |
| `next.error`, `next.called` | In a `.catch` handler only. `next.error.kind` is `throw` or `timeout`, `next.error.message` is the error's text, and `next.called` is `true` when the failed hook had called `next`. |

## Events

Events are grouped by what they concern, each with when it fires and what a hook on it can return. Hooks on `turn.step` and `process.spawn` are async generators, and other hooks are async functions.

The last column of each table uses shorthand. `next(e)` passes the event on unchanged. `next({ ...e, text })` passes on a copy with the named field changed, as in `next({ ...e, text: e.text.trim() })`. An object answers the event without calling `next`, and a word such as `reason` stands for a string you write, as in `{ deny: 'Use the file tools.' }`.

### Tools

Tool events fire around each tool call Claude makes, from the description Claude reads to the decision on whether the call runs:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| [[Mod_React_to_events_with_a_mod|`tool.call`]] | A tool is about to run | `next(e)`, `{ deny: reason }`, or `{ result }` |
| [[Mod_React_to_events_with_a_mod|`tool.check`]] | Claude Code decides whether a tool call may run, after the `tool.call` and `PreToolUse` hooks. `next(e)` resolves to the decision the rules, the permission mode, and those hooks reached. | `{ decision }`, which is `allow`, `ask`, or `deny` |
| `tool.describe` | Once for each tool, when its description is first sent to Claude | `{ description }`, optionally with `isDeferred` set to `true` to put the tool behind [[Connect_Claude_Code_to_tools_via_MCP|tool search]] or `false` to load it upfront |

### Prompts and what Claude reads

Prompt events cover the text the user types and the text Claude Code sends to Claude on its own, such as the system prompt and reminders:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| [[Mod_React_to_events_with_a_mod|`prompt.submit`]] | A prompt is submitted | `next({ ...e, text })`, `next({ ...e, context })`, or `{ drop: reason }` |
| `prompt.fill`, `prompt.suggest` | Text is about to go into the prompt box as a draft, or as a dim suggestion | `next(e)` with changed text |
| `prompt.edit` | The user edits the prompt box | `next(e)` |
| `prompt.compose` | Claude Code renders a system prompt | `{ sections }`, a list of `{ id, text, scope }` in the order they're sent |
| [[Mod_React_to_events_with_a_mod|`prompt.section`]] | Once for each named section of the system prompt. `e.name` is the section's `id` in `prompt.compose`. | `{ text }`, or `{ text: null }` to omit the section |
| [[Mod_React_to_events_with_a_mod|`prompt.context`]] | Once for each conversation, for the context sent with the first message | `{ blocks }` |
| `prompt.attachment` | Claude Code adds a message of its own for Claude, such as a reminder. `e.type` names the kind, and for the kinds the types declare, `e.detail` holds the facts the text was written from. | `{ text }`, or `{ text: null }` to omit it |
| `prompt.mention` | Claude Code is about to read a file that a prompt @-mentions. Requires Claude Code v2.1.290 or later. | `next({ ...e, path })` to read a different file, or `{ deny: reason }` |
| [[Mod_React_to_events_with_a_mod|`skill.prompt`]] | A skill's text is expanded for Claude | `{ text }` |
| `attribution.text` | Claude Code composes commit or pull request attribution text | `{ text }` |

### Commands and configuration

Command and configuration events fire when a command runs or is listed, and when a `/config` row is shown or changed:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| [[Mod_Use_the_mods_API|`command.run`]] | A command is about to run | `{ text }`, `{}`, or `next(e)` |
| `command.describe` | Once for each command, for the command list | `{ description, argumentHint, isHidden }` |
| `config.set` | A `/config` row is about to change | `next({ ...e, value })` or `{ deny: reason }` |
| `config.describe` | Once for each `/config` row | `{ label, description, isHidden }` |

### Turns

Turn events follow one answer from start to finish, including each request to the model within it:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| [[Mod_React_to_events_with_a_mod|`turn.start`]] | A turn begins | `next(e)` |
| [[Mod_React_to_events_with_a_mod|`turn.step`]] | One request is about to go to the model | `yield* next(e)`, or `next({ ...e, model })`, `next({ ...e, effort })` |
| [[Mod_React_to_events_with_a_mod|`turn.complete`]] | A turn ended | `next(e)`, or `{ text }` to show a line under the answer |

<h3 id="session">
  Session
</h3>

Session events mark the session starting, ending, compacting, and exchanging messages with other sessions:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| [[Mod_Use_the_mods_API|`session.start`]] | Once for each loaded mod, before the first prompt, and again after a reload of that mod. Not after `/clear`, `/resume`, or `/branch`. | `next(e)` |
| `session.end` | The session ends, or `/clear`, `/resume`, or `/branch` runs. `e.reason` is `clear`, `resume`, `logout`, `prompt_input_exit`, or `other`. `/branch` reports `resume`. | `next(e)` |
| `session.compact` | The conversation is about to be compacted | `{ skip: reason }` |
| [[Mod_Use_the_mods_API|`session.receive`]], [[Mod_Use_the_mods_API|`session.send`]] | A message arrives from, or is about to go to, another agent or session. See [[Mod_Use_the_mods_API|Send and receive messages between sessions]]. | `{ consumed: reason }` for `receive`, `{ isDelivered: false, reason }` for `send` |
| `session.append` | Once for each row the conversation keeps, such as a prompt, a response block, a tool result, or a notice, before it's stored | `next({ ...e, message })` to rewrite the row's `content` |
| `session.attach`, `session.detach` | Another app connects to or disconnects from the session | `next(e)` |
| `session.measure` | After each turn, and when a plan limit's percent used changes | `next(e)` |

### Subagents

Subagent events fire when a subagent type is offered to Claude and when a subagent or an agent-team teammate is about to start:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| `agent.offer` | A subagent type is offered to Claude | `{ isOffered: false }` to withhold it |
| `agent.spawn` | A subagent or an [[Orchestrate_teams_of_Claude_Code_sessions|agent team]] teammate is about to start. For a teammate, `e.isTeammate` is `true`. | `next({ ...e, model })` to choose its model, or `{ deny: reason }` |

### Interface

Interface events fire when Claude Code draws a render site and when the user uses a control a mod drew. [[Mod_Draw_in_the_interface_with_a_mod|Draw in the interface]] shows what a `ui.render` hook returns:

| Event | Fires when |
| :- | :- |
| [[Mod_Draw_in_the_interface_with_a_mod|`ui.render`]] | A [render site](#render-sites) is about to be drawn |
| `ui.resolve` | Mods load, once for each app, render site, and mod. The result is the element table that `$.ui.resolve(e)` reads. |
| [[Mod_Draw_in_the_interface_with_a_mod|`ui.press`]], [[Mod_Draw_in_the_interface_with_a_mod|`ui.input`]], [[Mod_Draw_in_the_interface_with_a_mod|`ui.select`]] | A `Button`, `Input`, or `Select` a mod drew is used |
| `ui.focus`, `ui.scroll` | The focused control or the scroll position of a pane or the band is about to change |
| `ui.close` | A pane is about to close. `e.id` is the pane and `e.origin.kind` is `plugin`, `person`, or `unload`. |
| [[Mod_Draw_in_the_interface_with_a_mod|`ui.message`]] | A `Client` element posts data to its mod |
| [[Mod_Draw_in_the_interface_with_a_mod|`ui.fault`]] | A `Client` element your mod drew failed to load, draw, or run. `e.phase` is `load`, `render`, or `run`, and `e.reason` is the error message. Requires Claude Code v2.1.289 or later. |

### Other mods

These events let a mod act on other mods as they load, to refuse one or change the mods API it receives:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| [[Mod_Manage_mods_for_your_organization|`plugin.register`]] | A hooks module is about to load. `e.uses` lists its events, mods API calls, environment variables, and state, as `claude plugin validate` prints them. Each call is written without the `$.` prefix, such as `fs.read`. | `{ refuse: reason }` |
| `engine.create` | The mods API is being built for this mod | A changed mods API, to add a namespace. A mod outside the `user` [tier](#the-hook-function) can also withhold one. |

### Telemetry

Telemetry events fire for the usage records Claude Code logs:

| Event | Fires when | A hook can return |
| :- | :- | :- |
| `telemetry.log`, `telemetry.mark` | A telemetry record is about to be logged, or one use of a feature is marked. In a mod you install, give a telemetry hook the filter `{ to: 'collector' }`, as in `on('telemetry.log', { to: 'collector' }, hook)`. Without the filter, the mod fails `claude plugin validate`. `*` doesn't match these events. | `next(e)`, or `{ deny: reason }` |

### Settings hook events

Each [[Hooks_reference|settings hook event]] is an event named `classic.<Event>`, such as `classic.Stop` or `classic.PostToolUse`. `e` is the hook's stdin JSON.

### Mods API calls

Every [mods API method](#mods-api-methods) is also an event, named for its namespace and method, such as `fs.read`, `model.complete`, or `ui.open`. A hook on one intercepts calls from the mods that run after it, and can return `next(e)`, `{ deny: reason }`, or `{ value }`.

## Mods API methods

The mods API is the `$` argument every hook receives. Its methods are grouped in namespaces, such as `$.ui`. This table lists each namespace's methods by name, so `open` in the `$.ui` row is the call `$.ui.open(...)`. The guides show the common ones in use, and [[Mod_Create_a_mod|the types for your build]] document every method with an example.

| Namespace | Methods |
| :- | :- |
| `$.plugin` | `name`, `root`: this plugin's name and directory |
| [[Mod_Draw_in_the_interface_with_a_mod|`$.ui`]] | `resolve`, `invalidate`, `open`, `close`, `panes`, `focus`, `scroll`, `toast`, `status`, `log`, `notice`, `ask`, `copy`, `selection`, `blit` |
| [[Mod_Use_the_mods_API|`$.command`]] | `register`, `run`, `list` |
| [[Mod_Use_the_mods_API|`$.tool`]] | `register`, `call`, `check`, `list` |
| `$.agent` | `register`, `spawn`, `list` |
| [[Mod_Use_the_mods_API|`$.model`]] | `complete`, `fork`, `classify` |
| [[Mod_Use_the_mods_API|`$.prompt`]] | `submit`, `read`, `fill`, `suggest`, `compose`. Claude reads text from `submit({ text })` after a sentence that names your mod as the sender. `submit({ text, asUser: true })` sends the text as the user's own words, without that sentence. |
| `$.turn` | `abort` |
| [[Mod_Use_the_mods_API|`$.session`]] | `messages`, `cwd`, `root`, `model`, `turns`, `id`, `repo`, `surfaces`, `usage`, `version`, `compact`, `send`, `append`, `authorize`. `usage()` returns `{ startedAt, context, rateLimits, cost }`: `context` has `tokens`, `window`, and `percent`, and `rateLimits` is a list of `{ kind, percentUsed, resetsAt }`. |
| `$.config` | `list`, `set` |
| [[Mod_Use_the_mods_API|`$.settings`]] | `read` |
| [[Mod_Use_the_mods_API|`$.env`]] | `get`, `set` |
| [[Mod_Use_the_mods_API|`$.fs`]] | `read`, `write`, `list`, `exists`, `stat`, `ancestors`. `write` isn't atomic: it replaces the file's content in place, so another process can read a partly written file. Keep data that several sessions change in `$.store`. |
| [[Mod_Draw_in_the_interface_with_a_mod|`$.store`]] | `get`, `set`, `delete`, `keys`. A key-value store that every session on the machine shares. See [[Mod_Draw_in_the_interface_with_a_mod|Save from more than one session]]. |
| [[Mod_Draw_in_the_interface_with_a_mod|`$.state`]] | Reactive state: `get`, `set`, with the helpers `atom`, `read`, `update`, `derive`, and `memberOf` imported from `claude-code` |
| [[Mod_Use_the_mods_API|`$.clock`]] | `now`, `sleep`, `after`, `every` |
| [[Mod_Use_the_mods_API|`$.http`]] | `fetch` |
| [[Mod_Use_the_mods_API|`$.process`]] | `run`, `spawn` |
| [[Mod_Use_the_mods_API|`$.mcp`]] | `call`, `connect`. `connect(server)` connects an MCP server that your own plugin's manifest lists. |
| `$.audio` | `play`, `speak` |
| `$.telemetry` | `log`, `mark`. A record is sent only when Claude Code or a built-in mod makes the call. |

## Render sites

A render site is an extension point in Claude Code's interface. Each row is a value of `e.component` in a `ui.render` hook, with the fields of `e.props` and the apps that render it. `e.surface` is `terminal` or `desktop`. [[Mod_Draw_in_the_interface_with_a_mod|Change what Claude Code already draws]] shows what a hook can do at a site, with an example of each choice.

| Site | `e.props` | `e.requestId` | Rendered on |
| :- | :- | :- | :- |
| [[Mod_Draw_in_the_interface_with_a_mod|`Pane`]] | `title`, `isFocused`, `bodyColumns`, `placement`, `scroll`, `view` | The pane's `id` | Terminal, Desktop |
| [[Mod_Draw_in_the_interface_with_a_mod|`AbovePrompt`]] | `hasSurvey`, `isWorking`, `maxRows`, `bodyColumns`, `scroll`, `view` | One instance | Terminal, Desktop |
| `UserMessage` | `text`, `origin`, `isExpanded`, and `task` or `from` by origin | The message id | Terminal, Desktop |
| `AssistantMessage` | The reply's text | The message id | Terminal, Desktop |
| `ToolUse`, `ToolResult`, `ToolGroup` | The tool's name, input, and result | The tool call id | Terminal, Desktop |
| `CommandOutput` | `command`, `text` | The message id | Terminal, Desktop |
| [[Mod_Draw_in_the_interface_with_a_mod|`AskUserQuestion`]] | The question and options | The tool call id | Terminal, Desktop |
| `ToolProgress` | `kind` | The tool call id | Terminal |
| [[Mod_Draw_in_the_interface_with_a_mod|`Spinner`]] | `word`, `message`, `suffix`, `mode` | The agent id | Terminal, Desktop |
| `TurnDuration` | `word`, `durationMs` | The message id | Terminal |
| `InfoNotice` | `text`, `command` | The message id | Terminal |
| `SessionMode` | `modes` | One instance | Terminal, Desktop |
| `PromptHint` | `isDraft`, `isWorking`, `hint` | One instance | Terminal, Desktop |

`e.viewport` holds `columns`, `rows`, and `isFullscreen`. It's absent until the app has measured its window. Its `rows` is the height of the whole window, not of your pane.

To fit a tree to its site, read these props in the hook:

* **Width of a `Pane` or the band**: draw to `e.props.bodyColumns`
* **Height of a `Pane` beside the transcript**: where `e.props.placement` is `'dock'`, `e.props.scroll.bodyRows` is the number of rows the pane has for your tree
* **Height of a `Pane` above the prompt**: where `e.props.placement` is `'inline'`, the pane grows with your tree up to a limit, and `bodyRows` is that limit. The [[Mod_Draw_in_the_interface_with_a_mod|`rows` field of `$.ui.open`]] asks for a different one.

A tree taller than the pane scrolls as a whole.

## Elements

Elements are the building blocks of a tree a `ui.render` hook returns, and you get them from `$.ui.resolve(e)`. [[Mod_Draw_in_the_interface_with_a_mod|Build a tree from elements]] shows the common ones with how the terminal draws them, and the [[Mod_Interface_gallery_for_mods|interface gallery]] has screenshots of most. A check mark means the app can draw the element.

| Element | Main props | Terminal | Desktop |
| :- | :- | :-: | :-: |
| [[Mod_Draw_in_the_interface_with_a_mod|`Box`]] | `key`, flex layout, `gap`, `padding`, `margin`, `width`, `height`, [`borderStyle`](#box-border-styles), `backgroundColor`, `position`, `hover` | ✓ | ✓ |
| [[Mod_Draw_in_the_interface_with_a_mod|`Text`]] | `color`, `backgroundColor`, `bold`, `italic`, `underline`, `dimColor`, `inverse`, `wrap` | ✓ | ✓ |
| [[Mod_Draw_in_the_interface_with_a_mod|`Button`]] | `key`, `label`, `onPress`, `hotkey`, `plain`, `dimColor`, `autoFocus`, `action` | ✓ | ✓ |
| `Link` | `href`, `label` | ✓ | ✓ |
| [[Mod_Interface_gallery_for_mods|`Code`]] | `source`, `language`, `path`, `startLine`, `format`, `wrap` | ✓ | ✓ |
| `Markdown` | `text`, `key`, `dimColor`, `onLinkPress`, `pressableLinks` | ✓ | ✓ |
| [[Mod_Draw_in_the_interface_with_a_mod|`Input`]] | `key`, `label`, `placeholder`, `value`, `submitLabel`, `onSubmit`, `onInput`, `autoFocus` | ✓ | ✓ |
| `Select` | `key`, `label`, `options`, `value`, `onSelect`, `autoFocus` | ✓ | ✓ |
| `Svg` | An SVG document, up to 131,072 characters | | ✓ |
| [[Mod_Draw_in_the_interface_with_a_mod|`Client`]] | `module`, `key` | ✓ | ✓ |
| [[Mod_Draw_in_the_interface_with_a_mod|`Raster`]] | `key`, `columns` up to 512, `rows` up to 256, `cells`. See [[Mod_Draw_in_the_interface_with_a_mod|Draw a grid of colored cells]]. | ✓ | |
| `Image` | PNG or RGBA bytes up to 2 MiB, or a file path, `columns` and `rows` up to 255, and `alt` text. | ✓ | |

More `Button` rules: `action` names one of Claude Code's own [[Customize_keyboard_shortcuts|keybinding actions]], and the user's binding for it presses the button when that binding is a chord or a modified key. A digit `hotkey` on a button in the band also fires when the user types that digit alone into an empty prompt and pauses. When two buttons in one drawing name the same `hotkey`, the later one gets it. `autoFocus` accepts only `true` on any control, so omit the prop to leave it off.

<h3 id="box-border-styles">
  `Box` border styles
</h3>

To draw a border around a `Box`, set its `borderStyle` to one of these names, as in `borderStyle: 'round'`. Each row says what the terminal draws for that name and shows the top edge of the border.

| `borderStyle` | What the terminal draws | Top edge |
| :- | :- | :- |
| `'single'` | Thin lines with square corners | `┌──┐` |
| `'double'` | Double lines | `╔══╗` |
| `'round'` | Thin lines with rounded corners | `╭──╮` |
| `'bold'` | Thick lines | `┏━━┓` |
| `'singleDouble'` | Thin lines on the top and bottom, double lines on the sides | `╓──╖` |
| `'doubleSingle'` | Double lines on the top and bottom, thin lines on the sides | `╒══╕` |
| `'classic'` | The ASCII characters `+`, `-`, and `\|` | `+--+` |
| `'arrow'` | Arrows that point into the `Box` | `↘↓↓↙` |
| `'dashed'` | Dashed lines with blank corners | `╌╌` |
| `'quote'` | A bar, `▎`, down the left side and blank cells on the other three sides | Blank |

A `Box` whose `borderStyle` names anything else, such as `'rounded'`, draws with no border.

## Limits

Hooks and mods API calls run under time and size limits. Claude Code skips a hook that exceeds a time limit and rejects a call that exceeds a size limit.

| Limit | Value |
| :- | :- |
| A hook's own execution time for one event, not counting time inside `next` or a mods API call other than `$.clock.sleep` | 10 seconds, or 50 milliseconds for a `prompt.edit` hook |
| A `.catch` handler's execution time | 1 second |
| All `session.end` hooks together | As long as the [[Hooks_reference|SessionEnd hook budget]], 1.5 seconds unless you change it, counted from when your settings `SessionEnd` hooks finish |
| `$.process.run` timeout | 30 seconds by default, 10 minutes at most |
| `$.model.complete` `maxTokens` | 1024 by default, up to 64,000 or the model's output limit |
| `$.fs.read` and `$.fs.write` | 4 MiB for one file |
| Text in one tree | The first 100,000 characters are drawn |
| `$.store` | 4 MiB of JSON in total |
| `$.session.messages()` | The newest 4,096 entries |
| `$.ui.invalidate('ui.render')` redraws | Throttled to 10 a second, or 30 in the terminal for the visible pane, the expanded band, and the hint line under the prompt. Calls that come sooner are coalesced. |
| `$.ui.toast` | Shown for 4 seconds unless you pass `{ timeoutMs }` |
| A pane opened without the user asking | Placed from 144 terminal columns, 110 after they've opened it once |
| Command, tool, subagent type, and pane names | Letters, digits, `_`, and `-`, up to 64 characters |
| One `claude plugin test` test | 5 seconds unless the test sets `timeoutMs` |

## Settings and environment variables

These are the settings and environment variables that affect mods. The Where column says which settings file or environment each one is read from:

| Name | Where | What it does |
| :- | :- | :- |
| `CLAUDE_CODE_PLUGIN_DIRS` | Environment, or `env` in `~/.claude/settings.json` | Plugin directories to load as `--plugin-dir` does, for apps you can't pass a flag to. Absolute paths separated by `:`, or `;` on Windows. |
| `CLAUDE_CODE_PLUGIN_DIR_WATCH` | Environment | `1` makes a long-running non-interactive session reload `--plugin-dir` mods on save |
| `prependPlugins`, `appendPlugins` | Managed settings. User settings only on a machine with no managed settings, for a user who isn't signed in with a Team or Enterprise plan. | Lists of plugin ids, such as `acme-guard@acme-tools`. Mods in `prependPlugins` run before every mod a user installs, and mods in `appendPlugins` run after, in the listed order. See [[Mod_React_to_events_with_a_mod|The order mods run in]]. |
| `allowManagedModsOnly` | Managed settings, as an [[Mod_Manage_mods_for_your_organization|option on the built-in guard]] | Only mods that [[Mod_Manage_mods_for_your_organization|count as your organization's]], and mods built into Claude Code, run their hooks. Users' settings hooks keep running. |
| `allowModsToOverrideDenyRules` | Managed settings, as an [[Mod_Manage_mods_for_your_organization|option on the built-in guard]] | Lets a mod a user installed approve a tool call that a `deny` rule refuses |
| `allowManagedHooksOnly` | Managed settings | Blocks hooks and installed mods that aren't your organization's. See [[All_settings|what keeps running]]. |
| `disableAllHooks` | Any settings file | In managed settings, no mod or hook from an installed plugin runs. In your own settings, what your organization manages keeps running. See [[All_settings|`disableAllHooks`]]. |
| `disableSideloadFlags` | Managed settings | Rejects `--plugin-dir` and `--plugin-url` at startup |
| `pluginConfigs` | User or managed settings | Holds `userConfig` values for a mod, keyed by the plugin's id, such as `acme-guard@acme-tools`, or its name and `@inline`, such as `first-mod@inline`, for one loaded with `--plugin-dir` |

`sec-default@builtin` is a guard built into Claude Code, listed as `cc-plugin-sec-default` in `/plugin` and the debug log. It loads ahead of every mod a person installs on a machine with managed settings, or for a user signed in with a Team or Enterprise plan. If managed `prependPlugins` is set, the guard loads only when that list names it, at the position listed. Its source is in the [`mods/sec-default` directory of the Claude Code repository](https://github.com/anthropics/claude-code/tree/main/mods/sec-default).

## Commands

These commands and flags load, inspect, and test a mod. The `claude` commands run in your shell and the `/` commands at the Claude Code prompt. In the table, `<directory>` stands for a path you type, as in `claude plugin validate ./first-mod`. Square brackets mark an optional argument.

| Command | What it does |
| :- | :- |
| [[Mods_overview|`/plugin`]] | Shows a line such as `1 mod active · first-mod` under its tabs when a mod that isn't built in has loaded |
| [[Mod_Create_a_mod|`claude plugin validate <directory>`]] | Reads a plugin's manifest and hooks module and reports errors, the events it handles, and the mods API calls it makes. `--strict` treats warnings as errors and `--json` prints a machine-readable report. |
| [`claude plugin test [directory]`](/docs/en/plugins/mods/test#write-a-test) | Runs every file under the directory, or the current directory when you give none, whose name ends in `.test.ts` or `.test.tsx`. Exits with status 1 when a test fails. |
| [[Mod_Create_a_mod|`claude --plugin-dir <directory>`]] | Loads a plugin directory for one session and reloads its hooks module when you save. Repeat the flag to load several. |
| `/reload-plugins` | Reloads plugins when you run it |

## Related Concepts
- [[MOC_Claude_Code|Master Index (MOC)]]
- [[MOC_Extensibility_and_MCP|Extensibility & MCP MOC]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]
- [[Matrix_Extensibility|Extensibility & Tools Matrix]]

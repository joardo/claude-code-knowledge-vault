---
title: "MOC: Claude Agent SDK"
aliases:
  - "MOC_Agent_SDK"
tags:
  - "claude-code"
  - "moc"
  - "sdk"
status: "verified"
last_updated: "2026-10"
---

# MOC: Claude Agent SDK

> Building production-grade autonomous AI agents using Claude Code as a programmatic library in Python and TypeScript.

## 1. Architecture & Core Concepts
- [[Agent_SDK_overview|Agent SDK Overview]]: Architecture of Claude Code as a library.
- [[Agent_SDK_Quickstart|SDK Quickstart]]: First agent script in Python and TypeScript.
- [[Agent_SDK_How_the_agent_loop_works|How the Agent Loop Works]]: In-depth lifecycle of SDK turns, context, and message streaming.
- [[Agent_SDK_Use_Claude_Code_features_in_the_SDK|Use Claude Code Features in SDK]]: Loading `CLAUDE.md`, skills, and hooks programmatically.

## 2. Tools & Custom Extensions
- [[Agent_SDK_Give_Claude_custom_tools|Custom In-Process Tools]]: Exposing internal functions and APIs directly as agent tools.
- [[Agent_SDK_Connect_to_external_tools_with_MCP|MCP in the SDK]]: Connecting external MCP servers.
- [[Agent_SDK_Scale_to_many_tools_with_tool_search|Tool Search]]: Handling 1,000+ tools with dynamic vector discovery.
- [[Agent_SDK_Subagents_in_the_SDK|Subagents in SDK]]: Programmatic subagent delegation.

## 3. Input, Output & State
- [[Agent_SDK_Streaming_Input|Streaming Input]]: Single mode vs streaming input patterns.
- [[Agent_SDK_Stream_responses_in_real-time|Real-Time Streaming Output]]: Consuming token and tool event streams.
- [[Agent_SDK_Get_structured_output_from_agents|Structured Outputs]]: Guaranteed JSON validation via Pydantic and Zod.
- [[Agent_SDK_Work_with_sessions|Sessions Management]]: Saving, resuming, and branching programmatic sessions.
- [[Agent_SDK_Persist_sessions_to_external_storage|External Session Storage]]: Mirroring transcripts to Redis, S3, or PostgreSQL.

## 4. References & Guides
- [[Agent_SDK_reference_-_Python|Python SDK Reference]]
- [[Agent_SDK_reference_-_TypeScript|TypeScript SDK Reference]]
- [[Agent_SDK_Hosting_the_Agent_SDK|Hosting & Deployment in Production]]

---
## Related Maps
- [[MOC_Claude_Code|Master Index]]
- [[MOC_Workflows_and_Patterns|Workflows & Patterns]]
- [[Matrix_Execution_Modes|Execution Modes Matrix]]

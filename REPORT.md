# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->

## Task 1A  Bare agent

### Q: What is the agentic loop?
A: The agent explained the iterative loop (perceive  reason  plan  act  observe) and emphasized repeated tool-call cycles until done.

### Q: What labs are available in our LMS?
A: The agent returned task descriptions based on local repository context ("based on lab plan and task files"), not live LMS backend tool calls.


## Task 1B  Agent with LMS tools

### Q: What labs are available?
A: The agent returned real LMS labs via MCP, including:
- Lab 01  Products, Architecture & Roles
- Lab 02  Run, Fix, and Deploy a Backend Service
- Lab 03  Backend API: Explore, Debug, Implement, Deploy
- Lab 04  Testing, Front-end, and AI Agents
- Lab 05  Data Pipeline and Analytics Dashboard
- Lab 06  Build Your Own Agent
- Lab 07  Build a Client with an AI Coding Agent
- lab-08

### Q: Describe the architecture of the LMS system
A: The agent described a layered architecture with clients (React/Flutter/Telegram), Caddy reverse proxy, FastAPI backend, PostgreSQL data layer, observability stack (OTel + VictoriaLogs + VictoriaTraces), and Qwen Code API for LLM access.

## Task 1C  Skill prompt

### Q: Show me the scores
A: The agent first requested missing lab context, then provided structured score data for Lab 04 (completion rate, task averages, attempts, top learners), and noted Lab 08 had no submissions.


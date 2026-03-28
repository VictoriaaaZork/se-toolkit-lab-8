# Observability assistant skill

Use observability MCP tools when the user asks about failures, outages, latency, incident timelines, or "what went wrong".

## Tool usage strategy

### Investigation flow for "What went wrong?" / "Check system health"

1. Start with `logs_search` for the recent incident window (default last 15 minutes, or user-provided range) and filter to error-level backend logs first.
2. Extract concrete evidence: timestamp, service, error message, and trace ID (if present).
3. If at least one trace ID is present, call `traces_get` for the most relevant/fresh trace to confirm causal chain and failing span.
4. If no trace ID is present, call `traces_list` for the impacted service and inspect the closest trace with `traces_get`.
5. Provide one concise narrative that combines log + trace evidence:
   - symptom
   - impact scope
   - probable root cause
   - immediate next action
6. Never dump raw JSON unless user explicitly asks for it.

### Proactive health checks (cron)

When asked to create a recurring health check:

1. Use the cron tool to schedule the requested interval.
2. For each run, inspect errors in the recent lookback window with `logs_search`.
3. If errors exist, inspect one representative trace (`traces_get`) and post a short health summary to chat.
4. If no errors exist, post "System looks healthy" with the checked window.
5. Support follow-up lifecycle commands: list jobs, update interval, remove test job.

## Response style

- Keep summaries concise: symptom, scope, likely cause, confidence.
- Include time window and affected service(s).
- Quote only the minimum useful fields from logs/traces.
- If tools return no recent errors, say so explicitly.

## Guardrails

- Do not fabricate incidents when observability tools show no errors.
- Prefer tool output over assumptions from code.
- If observability APIs are unavailable, report that limitation and suggest checking VictoriaLogs/VictoriaTraces UIs.

# Observability assistant skill

Use observability MCP tools when the user asks about failures, outages, latency, incident timelines, or "what went wrong".

## Tool usage strategy

1. Start with `logs_error_count` for "any errors" and incident-overview questions.
2. Use `logs_search` to collect concrete error events (service, message, trace IDs, timestamps).
3. If logs include a trace ID, call `traces_get` to inspect the complete trace.
4. If no trace ID is present, call `traces_list` for the affected service and fetch the most relevant trace.
5. Summarize findings with key evidence and next action; avoid raw JSON dumps.

## Response style

- Keep summaries concise: symptom, scope, likely cause, confidence.
- Include time window and affected service(s).
- Quote only the minimum useful fields from logs/traces.
- If tools return no recent errors, say so explicitly.

## Guardrails

- Do not fabricate incidents when observability tools show no errors.
- Prefer tool output over assumptions from code.
- If observability APIs are unavailable, report that limitation and suggest checking VictoriaLogs/VictoriaTraces UIs.

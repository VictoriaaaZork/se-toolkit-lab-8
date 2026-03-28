# syntax=docker/dockerfile:1.7
FROM harbor.pg.innopolis.university/docker-hub-cache/astral/uv:python3.14-bookworm-slim

WORKDIR /app/nanobot

COPY pyproject.toml /app/nanobot/pyproject.toml
COPY entrypoint.py /app/nanobot/entrypoint.py
COPY config.json /app/nanobot/config.json
COPY workspace /app/nanobot/workspace
COPY --from=workspace /mcp /app/mcp
COPY --from=workspace /nanobot-websocket-channel /app/nanobot-websocket-channel

RUN --mount=type=cache,target=/root/.cache/uv uv sync --project /app/nanobot --no-dev

ENV PATH="/app/nanobot/.venv/bin:${PATH}"
CMD ["python", "/app/nanobot/entrypoint.py"]

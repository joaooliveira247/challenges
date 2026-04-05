FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv sync --no-dev --frozen

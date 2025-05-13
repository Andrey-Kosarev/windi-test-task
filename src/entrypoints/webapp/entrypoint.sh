#!/bin/bash


uv run alembic upgrade head
uv run uvicorn src.entrypoints.webapp.main:app --host 0.0.0.0 --port 8000
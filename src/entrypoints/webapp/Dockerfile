FROM python:3.12.10-slim-bullseye
WORKDIR /app

RUN python3 -m pip install uv
COPY . /app
RUN uv sync

CMD ["uv", "run", "uvicorn", "src.entrypoints.webapp.main:app", "--host", "0.0.0.0", "--port", "8000"]
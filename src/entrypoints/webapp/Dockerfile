FROM python:3.12.10-slim-bullseye
WORKDIR /app

RUN python3 -m pip install uv

COPY pyproject.toml /app/
COPY uv.lock /app/
RUN uv sync

COPY . /app

RUN chmod +x "./src/entrypoints/webapp/entrypoint.sh"
CMD ["./src/entrypoints/webapp/entrypoint.sh"]
# CMD ["ls", "."]
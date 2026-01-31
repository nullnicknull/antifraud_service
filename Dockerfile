FROM python:3.11-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONPATH=/app

COPY pyproject.toml uv.lock ./ 
RUN uv sync --frozen

COPY app ./app 

RUN ./.venv/bin/python -m pytest app/tests/test_antifraud.py

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY app ./app
COPY main.py ./main.py

RUN pip install "uv>=0.1.0" && uv sync

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
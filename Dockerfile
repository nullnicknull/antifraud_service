FROM python:3.11-slim

WORKDIR /app

# Устанавливаем uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONPATH=/app

COPY pyproject.toml uv.lock ./ 
# Сначала ставим зависимости (кэшируем этот слой)
RUN uv sync --frozen

# Копируем всё приложение
COPY app ./app 

# ЗАПУСК ТЕСТОВ (сборка упадет, если тесты не пройдут)
# Используем прямой путь к python из созданного uv окружения
RUN ./.venv/bin/python -m pytest app/tests/test_antifraud.py

EXPOSE 8000

# Твоя рабочая команда запуска
CMD ["uv", "run", "uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./ 
COPY app ./app 

RUN pip install "uv>=0.1.0" && uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
Anti-Fraud Service
Сервис для проверки клиентов на мошенничество с кэшированием в Redis и мониторингом через Prometheus+Grafana.
Используемые технологии
Python
FastAPI
Pydantic
Redis
Pytest
Prometheus
Grafana
Docker / Docker Compose
Логика работы сервиса
Сервис принимает запрос с данными клиента: дата рождения, номер телефона, история займов.
Перед выполнением проверок сервис проверяет наличие результата в Redis.
Если результат найден в кэше — он сразу возвращается.
Если результата нет, выполняются проверки на стоп-факторы:
Номер телефона начинается не с +7 или 8.
Клиенту меньше 18 лет.
У клиента есть хотя бы один не закрытый займ.
Результат (список стоп-факторов и итоговый флаг true или false) сохраняется в Redis и возвращается клиенту.
Запуск проекта
Требования
Установленный Docker
Установленный Docker Compose
Тестирование
# Запуск тестов
uv run pytest tests/test_antifraud.py

# С покрытием кода
pytest --cov=app --cov-report=html tests/
Запуск
Из корня проекта выполните команду:
bash
docker compose up --build

Доступные адреса
Swagger UI: http://localhost:8000/docs
Метрики сервиса: http://localhost:8000/metrics
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Данные для входа в Grafana:
Логин: admin
Пароль: admin
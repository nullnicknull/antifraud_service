import pytest
from httpx import AsyncClient, ASGITransport
from app.src.main import app

@pytest.mark.asyncio
async def test_check_antifraud_fail_underage():
    """Тест: отказ, если клиенту меньше 18 лет"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/check", json={
            "birth_date": "2015-01-01",
            "phone_number": "+79001112233",
            "loans_history": []
        })
    
    assert response.status_code == 200
    data = response.json()
    assert data["result"] is False
    assert "Клиенту меньше 18 лет" in data["stop_factors"]

@pytest.mark.asyncio
async def test_check_antifraud_success():
    """Тест: успешное прохождение проверок"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/check", json={
            "birth_date": "1990-01-01",
            "phone_number": "+79001112233",
            "loans_history": [
                {"amount": 5000, "loan_data": "2023-01-01", "is_closed": True}
            ]
        })
    
    assert response.status_code == 200
    assert response.json()["result"] is True
    assert len(response.json()["stop_factors"]) == 0
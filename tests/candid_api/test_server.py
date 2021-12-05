from unittest import mock

from fastapi.testclient import TestClient

from src.candid_api.test_fastapi import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200, "Health check failed"
    assert response.json() == {"message": "Hello World"}


def test_politicians():
    with mock.patch(
        "src.candid_api.test_fastapi.get_politicians"
    ) as mock_get_politicians:
        response = client.get("/politicians")

    assert mock_get_politicians.call_count == 1
    assert response.status_code == 200

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_heatlh():
    response = client.get("/health")

    assert response.json()["status"] == "ok"
    assert response.status_code == 200

def test_ask():
    response = client.post("/ask",json = {"question": "what is AI?"})

    assert response.status_code == 200
    assert response.json()["agents_used"] == []

def test_empty_question():
    response = client.post("/ask",json = {"question":""})

    assert response.status_code == 422
import pytest
from fastapi.testclient import TestClient

from main import app  # import your FastAPI app

client = TestClient(app)

# ------------------ TESTS ------------------

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from FastAPI!"}

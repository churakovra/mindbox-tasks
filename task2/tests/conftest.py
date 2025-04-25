from fastapi.testclient import TestClient

from task2.app.main import app

client = TestClient(app)


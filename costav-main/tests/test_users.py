from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_login_api():

    resp = client.post(
        "/login",
        data={
            "username": "admin",
            "password": "admin"
        })
    
    assert resp.status_code == 200

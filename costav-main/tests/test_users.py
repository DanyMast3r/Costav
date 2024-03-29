from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_login_api():

    resp = client.post(
        "/login",
        data={
            "username": "pedropicapiedra",
            "password": "secret"
        })
    
    assert resp.status_code == 200



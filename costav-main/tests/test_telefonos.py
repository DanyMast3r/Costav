from fastapi import FastAPI

from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)

def test_read_index_telefono():

    resp = client.get("/telefonos")

    assert resp.status_code == 200

    assert resp.json() == {
        "status": "Success",
        "data": []
    }


def test_create_telefono():
    resp = client.post(
        "/telefonos/",
        headers={"X-Token": "A"},
        json={
            "id": "1",
            "modelo": "A05",
            "marca": "Samsung",
            "precio": "125",
            "cantidad": "3"

        }
    )

    assert resp.status_code == 200

    assert resp.json() == {
        "id": "1",
        "modelo": "A05",
        "marca": "Samsung",
        "precio": "125",
        "cantidad": "3"
    }

def test_get_telefono():
    resp = client.get(
        "/telefono/1/",
        headers={"X-Token": "A"}
    )

    assert resp.status_code == 200

    assert resp.json() == {
        "id": "1",
        "modelo": "A05",
        "marca": "Samsung",
        "precio": "125",
        "cantidad": "3"
    }
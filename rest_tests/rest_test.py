import requests

base_url = "https://reqres.in/api"


def test_simple():
    req = requests.get("https://jsonplaceholder.typicode.com/users")
    users = req.json()
    user = [user for user in users if user["id"] == 1]
    assert req.status_code == 200
    assert len(users) == 10
    assert "Leanne Graham" in user[0]["name"]


def test_create_user():
    new_user = {"name": "morpheus",
                "job": "leader"}
    req = requests.post(base_url + "/users", data=new_user)
    assert req.status_code == 201
    assert new_user["name"] == req.json()["name"]


def test_register_unsuccessful():
    body = {"email": "yuyiuy@jhfhksf.fg"}
    req = requests.post(base_url + "/register", data=body)
    assert req.status_code == 400
    assert "Missing password" in req.text

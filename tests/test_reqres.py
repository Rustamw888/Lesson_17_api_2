import json

from pytest_voluptuous import S

from schemas.reqres import create_user, login_unsuccessfull
from utils.sessions import reqres


def test_list_users():
    per_page = 6
    total = 12
    total_pages = 2
    response = reqres().get('/users?page=2', params={'per_page': per_page})
    assert response.status_code == 200
    assert response.json()['total'] == total
    assert response.json()['total_pages'] == total_pages
    assert len(response.json()['data']) == per_page


def test_create():
    response = reqres().post("/users", data={
        "name": "morpheus",
        "job": "leader"
    })
    assert response.status_code == 201
    assert str(response.json()['name']) == 'morpheus'
    assert str(response.json()['job']) == 'leader'
    assert S(create_user) == response.json()


def test_not_found():
    response = reqres().get('/users/23')
    assert response.status_code == 404


def test_success_register_user():
    response = reqres().post('/register', data={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })
    assert response.status_code == 200
    assert 'id' and 'token' in response.json()


def test_login_unsuccessfull_validation():
    response = reqres().post('/register', data={
        "email": "sydney@fife"
    })
    assert S(login_unsuccessfull) == response.json()
    assert response.status_code == 400


def test_update():
    payload = json.dumps({
        'name': 'morpheus',
        'job': 'zion resident'
    })
    response = reqres().put('/users/2', data=payload, allow_redirects=False)
    assert response.status_code == 200
    assert 'zion resident' and 'updatedAt' in response.json()

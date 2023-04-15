from . import utils
from .client import client


def test_create_todo(test_db):
    response = utils.create_user_and_create_todo()
    assert response.status_code == 200
    assert response.template.name == "home.html"


def test_home_page(test_db):
    utils.create_user_and_create_todo()

    response = client.get("/todos", follow_redirects=True)
    assert response.status_code == 200
    assert response.template.name == "home.html"


def test_add_page(test_db):
    utils.create_user_and_create_todo()

    response = client.get("/todos/add-todo", follow_redirects=True)
    assert response.status_code == 200
    assert response.template.name == "add-todo.html"


def test_edit_page(test_db):
    utils.create_user_and_create_todo()

    response = client.get("/todos/edit-todo/1", follow_redirects=True)
    assert response.status_code == 200
    assert response.template.name == "edit-todo.html"

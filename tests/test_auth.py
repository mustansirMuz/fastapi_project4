from fastapi import Response

from .client import client
from .utils import create_user, get_all_users, login_user


def test_register(test_db) -> None:
    response = create_user()
    assert response.status_code == 200
    assert response.template.name == "login.html"


def test_login_user(test_db) -> None:
    create_user()
    response = login_user()
    assert response.status_code == 200
    assert response.template.name == "home.html"

    # incorrect credentials
    response = login_user("incorrect")
    assert response.template.name == "login.html"

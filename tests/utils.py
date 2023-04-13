from fastapi import Response

from .client import client

TEST_USER = {
    "username": "testuser",
    "email": "testuser@gmail.com",
    "firstname": "Test",
    "lastname": "User",
    "password": "12345678",
    "password2": "12345678",
}

TEST_TODO = {
    "id": 1,
    "title": "This is a test todo",
    "description": "Testing is important",
    "priority": 3,
    "complete": False,
    "owner_id": 1,
}


def create_user() -> Response:
    return client.post("/auth/register", data=TEST_USER)


def login_user(password="12345678") -> Response:
    auth = {"email": "testuser", "password": password}
    return client.post("/auth/", data=auth, follow_redirects=True)


def login_user_and_get_auth_cookies() -> dict:
    response = login_user()
    cookies = response.cookies.get("access_token")
    return {"access_token": cookies}


def get_all_users() -> Response:
    return client.get("/users")


def equals_test_user(user: dict) -> bool:
    fields_to_check = ["username", "email", "first_name", "last_name"]
    for field in fields_to_check:
        if user[field] != TEST_USER[field]:
            return False
    return True


def create_todo(cookies: dict, todo: dict = TEST_TODO) -> Response:
    client.cookies.set("access_token", cookies.get("access_token"))
    return client.post("/todos/add-todo", data=todo)


def create_user_and_create_todo():
    create_user()
    cookies = login_user_and_get_auth_cookies()
    return create_todo(cookies)

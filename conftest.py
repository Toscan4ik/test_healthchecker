import os

import pytest

from framework.api.models.auth import AuthRequest


@pytest.fixture(scope="session")
def auth_request_body() -> AuthRequest:
    login = os.getenv("login")
    password = int(os.getenv("password"))
    return AuthRequest(login=login, password=password)

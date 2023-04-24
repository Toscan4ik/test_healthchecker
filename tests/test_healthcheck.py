import pytest
from requests.exceptions import ConnectTimeout

from framework.api.models.auth import AuthRequest
from framework.api.service_client import ServiceClient


class TestHealthCheck:
    def test_get_healthcheck(self, auth_request_body):
        service_client = ServiceClient()
        service_client.post_auth(request=auth_request_body)

        try:
            healthcheck = service_client.get_healthcheck(timeout=60)
            assert healthcheck.succes, "Сервис не доступен"
        except ConnectTimeout:
            raise ConnectTimeout("Сервис не доступен")

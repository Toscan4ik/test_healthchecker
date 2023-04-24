from requests import Session

from .models import auth, healthcheck


class ServiceClient:
    def __init__(self, base_url: str = "http://test.ru/api"):
        self.base_url = base_url
        self.session = Session()

    def post_auth(self, request: auth.AuthRequest) -> auth.AuthResponse:
        url = f"{self.base_url}/auth"
        resp = self.session.post(url=url, data=request.json())
        return auth.AuthResponse.parse_raw(resp.text)

    def get_healthcheck(self, timeout: int = 5) -> healthcheck.HealthcheckResponse:
        url = f"{self.base_url}/healthcheck"
        resp = self.session.get(url=url, timeout=timeout)
        return healthcheck.HealthcheckResponse.parse_raw(resp.text)

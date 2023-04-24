from framework.api.service_client import ServiceClient


class TestAuth:
    def test_auth(self, auth_request_body):
        service_client = ServiceClient()
        resp = service_client.post_auth(request=auth_request_body)
        assert resp.result.succes, "Неудачная авторизация, проверьте ваш логин или пароль"

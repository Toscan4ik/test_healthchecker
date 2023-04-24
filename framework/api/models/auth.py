from .common import ConfiguredModel


class AuthRequest(ConfiguredModel):
    login: str
    password: int


class Result(ConfiguredModel):
    meta: str
    succes: bool


class AuthResponse(ConfiguredModel):
    result: Result

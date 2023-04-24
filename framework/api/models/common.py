from pydantic import BaseModel, Extra


class ConfiguredModel(BaseModel):
    class Config:
        allow_mutation = False
        extra = Extra.forbid

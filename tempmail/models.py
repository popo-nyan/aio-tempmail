from pydantic import BaseModel


class DomainBaseModel(BaseModel):
    name: str
    type: str
    forward_available: bool
    forward_max_seconds: int

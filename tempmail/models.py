from pydantic import BaseModel, Field
from typing import Any, List, Optional


class DomainBaseModel(BaseModel):
    name: str
    type: str
    forward_available: bool
    forward_max_seconds: int


class CreateEmailResponseBaseModel(BaseModel):
    email: str
    token: str


class MessageBaseModel(BaseModel):
    attachments: Optional[List[Any]]
    body_html: Optional[str]
    body_text: Optional[str]
    cc: Optional[str]
    created_at: str
    from_email: Optional[str] = Field(..., alias="from")
    id: str
    subject: Optional[str]
    to: Optional[str]

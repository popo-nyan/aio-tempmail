from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class DomainModel:
    name: str
    type: str
    forward_available: str
    forward_max_seconds: str


@dataclass(slots=True)
class CreateEmailResponseModel:
    email: str
    token: str


@dataclass(slots=True)
class MessageResponseModel:
    id: str
    subject: Optional[str]
    cc: Optional[str]
    body_html: Optional[str]
    body_text: Optional[str]
    attachments: Optional[str]
    created_at: str
    email_from: Optional[str]
    email_to: Optional[str]

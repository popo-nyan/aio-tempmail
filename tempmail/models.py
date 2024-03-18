from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class Domain:
    name: str
    type: str
    forward_available: str
    forward_max_seconds: str


@dataclass
class CreateEmail:
    email: str
    token: str


@dataclass
class Message:
    attachments: Optional[list[Any]]
    body_html: Optional[str]
    body_text: Optional[str]
    cc: Optional[str]
    created_at: str
    from_email: Optional[str]
    id: str
    subject: Optional[str]
    to: Optional[str]

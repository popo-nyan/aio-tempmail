from dataclasses import dataclass


@dataclass
class DomainModel:
    name: str
    type: str
    forward_available: str
    forward_max_seconds: str


@dataclass
class CreateEmailResponseModel:
    email: str
    token: str


@dataclass
class MessageResponseModel:
    attachments: list | None
    body_html: str | None
    body_text: str | None
    cc: str | None
    created_at: str
    email_from: str | None
    id: str
    subject: str | None
    email_to: str | None

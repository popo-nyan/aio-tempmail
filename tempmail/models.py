from dataclasses import dataclass


@dataclass(slots=True)
class DomainModel:
    name: str
    type: str
    forward_available: str
    forward_max_seconds: str


@dataclass(slots=True)
class CreateEmailResponseModel:
    address: str
    token: str


@dataclass(slots=True)
class MessageResponseModel:
    id: str
    subject: str | None
    cc: str | None
    body_html: str | None
    body_text: str | None
    attachments: str | None
    created_at: str
    email_from: str | None
    email_to: str | None

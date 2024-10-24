import aiohttp

from .models import CreateEmailResponseModel, DomainModel, MessageResponseModel


class Client:

    def __init__(self):
        self._session = aiohttp.ClientSession(
            base_url="https://api.internal.temp-mail.io",
            headers={
                "Host": "api.internal.temp-mail.io",
                "User-Agent": "okhttp/4.5.0",
                "Connection": "close",
            },
        )

    async def close(self) -> None:
        if not self._session.closed:
            await self._session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self) -> None:
        await self.close()
        return None

    async def get_domains(self) -> list[DomainModel]:
        async with self._session.get("/api/v3/domains") as response:
            response_json = await response.json()
            return [
                DomainModel(
                    domain["name"],
                    domain["type"],
                    domain["forward_available"],
                    domain["forward_max_seconds"],
                )
                for domain in response_json["domains"]
            ]

    async def create_email(
        self, alias: str | None = None, domain: str | None = None
    ) -> CreateEmailResponseModel:
        async with self._session.post(
            "/api/v3/email/new", data={"name": alias, "domain": domain}
        ) as response:
            response_json = await response.json()
            return CreateEmailResponseModel(
                response_json["email"], response_json["token"]
            )

    async def delete_email(self, email: str, token: str) -> bool:
        async with self._session.delete(
            f"/api/v3/email/{email}", data={"token": token}
        ) as response:
            if response.status == 200:
                return True
            else:
                return False

    async def get_messages(self, email: str) -> list[MessageResponseModel] | None:
        async with self._session.get(f"/api/v3/email/{email}/messages") as response:
            response_json = await response.json()
            if len(response_json) == 0:
                return None
            return [
                MessageResponseModel(
                    id=message["id"],
                    subject=message["subject"],
                    cc=message["cc"],
                    body_html=message["body_html"],
                    body_text=message["body_text"],
                    attachments=message["attachments"],
                    created_at=message["created_at"],
                    email_from=message["from"],
                    email_to=message["to"],
                )
                for message in response_json
            ]

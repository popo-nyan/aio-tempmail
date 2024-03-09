import asyncio

import aiohttp
from types import TracebackType
from typing import List, Optional, Type
from .models import DomainBaseModel, CreateEmailResponseBaseModel


class Client:
    
    def __init__(self):
        self._client = aiohttp.ClientSession(base_url="https://api.internal.temp-mail.io",
                                             headers={'Host': 'api.internal.temp-mail.io',
                                                      'User-Agent': 'okhttp/4.5.0',
                                                      'Connection': 'close'})
    
    async def close(self) -> None:
        if not self._client.closed:
            await self._client.close()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType],
                        ) -> Optional[bool]:
        await self.close()
        return None
    
    async def get_domains(self) -> List[DomainBaseModel]:
        async with self._client.get("/api/v3/domains") as response:
            response_json = await response.json()
            return [DomainBaseModel.model_validate(domain) for domain in response_json['domains']]
    
    async def create_email(self,
                           alias: Optional[str] = None,
                           domain: Optional[str] = None
                           ) -> CreateEmailResponseBaseModel:
        async with self._client.post("/api/v3/email/new",
                                     data={'name': alias,
                                           'domain': domain}) as response:
            response_json = await response.json()
            return CreateEmailResponseBaseModel.model_validate(response_json)
    
    async def delete_email(self,
                           email: str,
                           token: str) -> bool:
        async with self._client.delete(f"/api/v3/email/{email}",
                                       data={'token': token}) as response:
            if response.status == 200:
                return True
            else:
                return False

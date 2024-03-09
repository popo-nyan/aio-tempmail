import aiohttp

from typing import List, Optional
from models import DomainBaseModel


class Client:
    
    def __init__(self):
        self.__session = aiohttp.ClientSession(base_url="https://api.internal.temp-mail.io",
                                               headers={'Host': 'api.internal.temp-mail.io',
                                                        'User-Agent': 'okhttp/4.5.0',
                                                        'Connection': 'close'})
    
    async def get_domains(self) -> List[DomainBaseModel]:
        async with self.__session.get("/api/v3/domains") as response:
            response_json = await response.json()
            await self.__session.close()
            return [DomainBaseModel.model_validate(domain) for domain in response_json['domains']]
    
    async def create_email(self,
                           alias: Optional[str],
                           domain: Optional[DomainBaseModel.name],
                           token: Optional[str]
                           ):
        pass

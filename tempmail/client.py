import aiohttp

from typing import List, Optional
from models import DomainBaseModel, CreateEmailResponseBaseModel


class Client:
    
    def __init__(self):
        self.__session = aiohttp.ClientSession(base_url="https://api.internal.temp-mail.io",
                                               headers={'Host': 'api.internal.temp-mail.io',
                                                        'User-Agent': 'okhttp/4.5.0',
                                                        'Connection': 'close'})
    
    async def get_domains(self) -> List[DomainBaseModel]:
        async with self.__session.get("/api/v3/domains") as response:
            response_json = await response.json()
            return [DomainBaseModel.model_validate(domain) for domain in response_json['domains']]
    
    async def create_email(self,
                           alias: Optional[str] = None,
                           domain: Optional[str] = None
                           ) -> CreateEmailResponseBaseModel:
        async with self.__session.post("/api/v3/email/new",
                                       data={'name': alias,
                                             'domain': domain}) as response:
            response_json = await response.json()
            return CreateEmailResponseBaseModel.model_validate(response_json)


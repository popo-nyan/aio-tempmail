import aiohttp


class Client:
    
    def __init__(self):
        self.__session = aiohttp.ClientSession()


    
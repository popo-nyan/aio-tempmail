import asyncio
from tempmail import Client


async def test_client() -> None:
    client = Client()
    await client.get_domains()


if __name__ == "__main__":
    asyncio.run(test_client())

import asyncio
from tempmail import Client


async def main() -> None:
    client = Client()
    domains = await client.get_domains()
    email = await client.create_email(domain=domains[0].name)
    print(email)


if __name__ == "__main__":
    asyncio.run(main())

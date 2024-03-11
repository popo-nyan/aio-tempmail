import asyncio
import tempmail


async def main() -> None:
    client = tempmail.Client()
    domains = await client.get_domains()
    email = await client.create_email(domain=domains[0].name)
    print(email.email, email.token)
    messages = await client.get_messages(email.email)
    for message in messages:
        print(message.from_email, message.body_text)


if __name__ == '__main__':
    asyncio.run(main())

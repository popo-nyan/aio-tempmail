import random
import asyncio

import tempmail


async def main() -> None:
    client = tempmail.Client()
    domains = await client.get_domains()
    email = await client.create_email(domain=random.choice(domains).name)
    print(email.address, email.token)
    while True:
        messages = await client.get_messages(email.address)
        if messages is not None:
            break
    for message in messages:
        print(message.email_from, message.body_text)
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())

# aio-tempmail

Unofficial temp-mail.io async wrapper

# Example

```python
import asyncio
import tempmail


async def main() -> None:
    client = tempmail.Client()
    domains = await client.get_domains()
    email = await client.create_email(domain=domains[0].name)
    print(email.address, email.token)
    while True:
        messages = await client.get_messages(email.address)
        if messages is not None:
            break
    for message in messages:
        print(message.email_from, message.body_text)
    await client.close()


if __name__ == '__main__':
    asyncio.run(main())

```

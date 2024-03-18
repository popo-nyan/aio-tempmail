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
    print(email.email, email.token)
    while True:
        messages = await client.get_messages(email.email)
        if messages is not None:
            break
    for message in messages:
        print(message.from_email, message.body_text)
    await client.close()


if __name__ == '__main__':
    asyncio.run(main())
```
> [!NOTE]
> Be sure to put `await client.close()` at the end.

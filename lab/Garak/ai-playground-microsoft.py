
import asyncio
import httpx

async def main():
    payload = {"name": "demo", "value": 42}
    async with httpx.AsyncClient(timeout=10, http2=True) as client:
        r = await client.post(
            "https://api.example.com/data",
            json=payload,                  # utiliser data=... pour du form-encoded
            params={"q": "demo"},
            headers={"Accept": "application/json"},
        )
        r.raise_for_status()
        print(r.json())

asyncio.run(main())
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def main():
    urls = ["https://youtube.com", "https://google.com"]
    results = await fetch_multiple_urls(urls)
    for i, content in enumerate(results):
        print(f"Ответ от {urls[i]}: {content[:100]}...")  # первые 100 символов

asyncio.run(main())
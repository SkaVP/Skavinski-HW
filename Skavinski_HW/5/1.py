import asyncio

async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = [
        "https://youtube.com",
        "https://google.com",
        "https://onliner.by",
        "https://microsoft.com",
        "https://yandex.com",
    ]

    tasks = [fetch_url(url) for url in urls]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

# без таймера

asyncio.run(main()) 

#с таймером

# if __name__ == "__main__":
#     import time
#     start = time.time()
#     asyncio.run(main())
#     print(f"Total time: {time.time() - start:.2f} seconds")

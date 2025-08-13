import asyncio

async def set_async_timer(seconds, callback):
    await asyncio.sleep(seconds)
    await callback()

async def timer_end():
    print("Таймер сработал")

async def main():
    await set_async_timer(2, timer_end)


asyncio.run(main())
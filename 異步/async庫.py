import asyncio
import time


async def a():
    # print(2)

    print(4)

async def b():
    print(2)
    await asyncio.sleep(10)
    await a()
    print(3)

task = [asyncio.ensure_future(b()),
    asyncio.ensure_future(a()),

]

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(task))
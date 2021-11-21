# await + 可等待的對象 (携程對象, Future, Task對象 - 》 IO等待)

import asyncio


async def funa():
    await asyncio.sleep(4)
    print(4)


async def func():
    print("等等中")

    await funa()
    print("結束")


task = [asyncio.ensure_future(funa()),
        asyncio.ensure_future(func()),

        ]
asyncio.run(asyncio.wait(task))

import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main開始")

    print("main結束")
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    ret1 = await task1

    ret2 = await task2
    print(123)
    print(ret1, ret2)


asyncio.run(main())

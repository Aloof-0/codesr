import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main開始")

    print("main結束")
    task_list = [asyncio.create_task(func()), asyncio.create_task(func())]
    done, pending = await asyncio.wait(task_list, timeout=None)

    c = done
asyncio.run(main())
# 2.1. 동기와 비동기의 차이 (비동기)

import time
import asyncio


async def async_wait(n):
    for i in range(3):
        await asyncio.sleep(1)
        print(f"{n} : {i+1}번째")


async def process_async():
    start = time.time()
    await asyncio.wait([async_wait(3), async_wait(1)])
    end = time.time()
    print("경과시간 : ", end - start)


asyncio.run(process_async())

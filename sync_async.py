from loguru import logger
import asyncio
from random import randint
from time import sleep


async def foo_sync(idx):
    logger.info(f'start job foo_sync {idx}')
    await asyncio.sleep(randint(0,10))
    logger.info(f'end job foo_sync {idx}')


async def bar_sync():
    logger.info('start job bar_sync')
    await asyncio.sleep(1)
    logger.info('end job bar_sync')



loop = asyncio.get_event_loop()

futures = [loop.create_task(foo_sync(i)) for i in range(10)]

tasks = asyncio.wait(futures)
logger.info('start tasks')
loop.run_until_complete(tasks)
logger.info('end tasks')
loop.close()
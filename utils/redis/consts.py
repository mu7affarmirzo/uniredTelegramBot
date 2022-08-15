import asyncio
from typing import Optional

import aioredis

data_pool: Optional[aioredis.Redis] = None


async def create_pools():
    global data_pool
    pool = aioredis.ConnectionPool.from_url("redis://localhost")
    data_pool = aioredis.Redis(connection_pool=pool)


asyncio.get_event_loop().run_until_complete(create_pools())

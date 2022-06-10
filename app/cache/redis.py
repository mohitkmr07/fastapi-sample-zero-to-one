import json
from typing import Optional

import aioredis
from aioredis import Redis
from sqlalchemy_serializer import SerializerMixin

from app.core.config import settings

TWO_MINUTES = 60 + 60

redis: Optional[Redis] = None


async def initialize_redis():
    global redis
    redis = await aioredis.from_url(settings.REDIS_URL, decode_responses=True)


async def set_cache(data, key: str):
    await redis.set(
        key,
        json.dumps(data),
        ex=TWO_MINUTES,
    )


async def get_cache(key: str):
    cache_data = await redis.get(key)
    if cache_data:
        return json.loads(cache_data)


class CacheableEntity(object):
    """Strictly to be used for read only
       It does not return a orm object
       it just returns a json

       """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, fn):
        async def execute_method(*args, **kwargs):
            key: str = ''
            try:
                key = await get_entity_cache_key(args[0].model.__tablename__, self.args, **kwargs)
                print("key=", key)
                data = await get_cache(key)
                if data:
                    print("cache hit", data)
                    return args[0].model(**data)
            except (ConnectionError, TimeoutError, Exception) as e:
                print("Handled exception")
            to_execute: SerializerMixin = await fn(*args, **kwargs)
            try:
                await set_cache(data=to_execute.to_dict(), key=key)
            except (ConnectionError, TimeoutError, Exception) as e:
                print("Handled exception")
            return to_execute

        return execute_method


async def get_entity_cache_key(primary_key: str, *args, **kwargs) -> str:
    key: str = primary_key
    for i in args[0]:
        if i in kwargs:
            key = f'{key}:{str(kwargs[i])}'

    return key

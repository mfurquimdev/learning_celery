import redis

import parameter

redis_backend = redis.StrictRedis(
    host=parameter.get_env("REDIS_HOST"),
    port=parameter.get_env("REDIS_PORT"),
    db=0,
    # decode_responses=True
)

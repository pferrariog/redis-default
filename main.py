"""Commands before your program startup"""
from config.stationary_data import start_data
from models.redis.connection.redis_conn import RedisConnectionHandler
from models.redis.redis_repo import RedisRepository

# default connection and object instance
redis = RedisConnectionHandler().connect()
redis_repo = RedisRepository(redis)

# loading current data in redis to start object
start_data.load(redis.hgetall().decode("utf-8"))


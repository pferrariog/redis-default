"""Commands before your program startup"""
from config.stationary_data import start_data
from models.connection.redis_conn import RedisConnectionHandler
from models.redis_repo import RedisRepository

# default connection and object instance
connection = RedisConnectionHandler().connect()
redis = RedisRepository(connection)

# loading current data in redis to start object
start_data.load(connection.hgetall().decode("utf-8"))

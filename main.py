from models.connection.redis_conn import RedisConnectionHandler
from models.redis_repo import RedisRepository

redis = RedisRepository(RedisConnectionHandler().connect())

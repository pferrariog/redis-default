"""Use case example: redis as cache layer to relational database"""
from models.database.database_repository import DatabaseRepository
from models.redis.connection.redis_conn import RedisConnectionHandler
from models.redis.redis_repo import RedisRepository


redis = RedisConnectionHandler().connect()
redis_repo = RedisRepository(redis)
database_repo = DatabaseRepository()

def get_value(key):
    """Get value from cache or database"""
    value = redis_repo.get(key)
    if not value:
        # could add a try-catch here based on database repo implementation
        value = database_repo.select_by_name(key)
        redis_repo.insert(key, value)

    return value

if __name__ == "__main__":
    get_value("foo")

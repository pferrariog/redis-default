from typing import Any

from redis import Redis


class RedisRepository:
    """Class to manage redis crud operations"""
    def __init__(self, redis_connection: Redis) -> None:
        """Initializer"""
        self.__redis_connection = redis_connection

    def insert(self, key: str, value: Any) -> None:
        """Insert a given key-value pair"""
        self.__redis_connection.set(key, value)

    def get(self, key: str) -> Any:
        """Get value of the given key"""
        return self.__redis_connection.get(key).decode('utf-8')

    def delete(self, key: str) -> None:
        """Delete the key-value pair"""
        delete = self.__redis_connection.delete(key)
        if delete == 0:
            raise Exception(f"Error while deleting {key}")

    def hash_insert(self, key: str, field: str, value: any) -> None:
        """Insert a key-object pair"""
        self.__redis_connection.hset(key, field, value)

    def hash_get(self, key: str, field: str) -> Any:
        """Get the value of a field from the key-object"""
        return self.__redis_connection.hget(key, field)

    def hash_delete(self, key: str, field: str):
        """Delete the specific field from the key-object"""
        delete = self.__redis_connection.hdel(key, field)
        if delete == 0:
            raise Exception(f"Error while deleting {key}")

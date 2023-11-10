from connection.connection import connection
from redis import Redis


class RedisConnectionHandler:
    """Class to manage redis connection"""
    def __init__(self) -> None:
        """Initializer"""
        self.__host = connection["host"]
        self.__db = connection["db"]
        self.__port = connection["port"]
        self.__connection = None

    def connect(self) -> Redis:
        """Set redis connection"""
        self.__connection = Redis(
            self.__host,
            self.__port,
            self.__db
        )
        return self.__connection
    
    def get_connection(self) -> Redis:
        """Return the current connection"""
        return self.__connection

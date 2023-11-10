from connection.connection import connection
from redis import Redis


class RedisConnectionHandler:
    def __init__(self) -> None:
        self.__host = connection["host"]
        self.__db = connection["db"]
        self.__port = connection["port"]
        self.__connection = None

    def connect(self) -> Redis:
        self.__connection = Redis(
            self.__host,
            self.__port,
            self.__db
        )
        return self.__connection
    
    def get_connection(self) -> Redis:
        return self.__connection
    
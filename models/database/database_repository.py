from typing import Any

class DatabaseRepository:
    """Simulate a real relational database"""
    def __init__(self) -> None:
        self.__data = {
            "foo": "bar"
        }

    def select_by_name(self, key: str) -> Any | None:
        """Retrieve data from database"""
        if key in self.__data:
            return self.__data[key]
        return None

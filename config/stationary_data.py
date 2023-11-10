from typing import Any

class _StationaryData:
    """Class to manage existent data in redis"""
    def __init__(self) -> None:
        """Initializer"""
        self.__cached_data = None

    def load(self, data: dict) -> None:
        """Load existent data from redis"""
        self.__cached_data = data

    def get(self, key: str) -> Any | None:
        """Get a speficic data from redis dictionary"""
        if key in self.__cached_data:
            return self.__cached_data[key]
        return None


# singleton pattern
start_data = _StationaryData()

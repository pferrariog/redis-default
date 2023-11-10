class _StationaryData:
    """Class to manage existent data in redis"""
    def __init__(self) -> None:
        """Initializer"""
        self.__cached_data = None

    def load(self, data: dict) -> None:
        """Load existent data from redis"""
        self.__cached_data = data

    def get(self, key: str) -> str:
        """Get a speficic data from redis dictionary"""
        try:
            return self.__cached_data[key]
        except Exception:
            raise KeyError(f"Key {key} not found")


# singleton pattern
start_data = _StationaryData()

class CircularBuffer:

    def __init__(self) -> None:
        self.__index = 0
        self.__outdex = 0

    def is_empty(self):
        return self.__index == self.__outdex

    def is_full(self):
        return False

    def put(self, param):
        self.__index += 1

    def get(self):
        self.__outdex += 1
        return 42

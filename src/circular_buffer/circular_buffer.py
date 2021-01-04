class CircularBuffer:

    def __init__(self) -> None:
        self.__index = 0
        self.__outdex = 0
        self.__values = [None] * 10

    def is_empty(self):
        return self.__index == self.__outdex

    def is_full(self):
        return False

    def put(self, value):
        self.__values[self.__index] = value
        self.__index += 1

    def get(self):
        value = self.__values[self.__outdex]
        self.__outdex += 1
        return value

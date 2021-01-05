class CircularBuffer:

    def __init__(self, capacity) -> None:
        self.__index = 0
        self.__outdex = 0
        self.__values = [None] * (capacity + 1)
        self.__capacity = capacity
        self.__count = 0

    def is_empty(self):
        return self.__index == self.__outdex

    def is_full(self):
        return self.next_index(self.__index) == self.__outdex

    def put(self, value):
        if self.is_full():
            raise Exception
        self.__count += 1
        self.__values[self.__index] = value
        self.__index = self.next_index(self.__index)

    def get(self):
        if self.is_empty():
            raise Exception
        value = self.__values[self.__outdex]
        self.__count -= 1
        self.__outdex = self.next_index(self.__outdex)
        return value

    def next_index(self, index):
        new_index = index + 1
        if new_index >= self.__capacity + 1:
            return 0
        return new_index

    def capacity(self):
        return self.__capacity

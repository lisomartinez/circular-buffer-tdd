class CircularBuffer:

    def __init__(self, capacity) -> None:
        self.__index = 0
        self.__outdex = 0
        self.__values = [None] * capacity
        self.__capacity = capacity
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def is_full(self):
        return self.__count == self.__capacity

    def put(self, value):
        self.__count += 1
        self.__values[self.__index] = value
        self.__index = self.next_index(self.__index)

    def get(self):
        value = self.__values[self.__outdex]
        self.__count -= 1
        self.__outdex = self.next_index(self.__outdex)
        return value

    def next_index(self, index):
        new_index = index + 1
        if new_index >= self.__capacity:
            return 0
        return new_index

    def capacity(self):
        return self.__capacity

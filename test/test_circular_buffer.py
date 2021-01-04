import pytest
from src.circular_buffer import *
from assertpy import assert_that

AN_ELEMENT = 42
FIRST_ELEMENT = 41
SECOND_ELEMENT = 42
THIRD_ELEMENT = 43
CAPACITY = 10

class TestCircularBuffer:

    @pytest.fixture()
    def buffer(self) -> CircularBuffer:
        buffer = CircularBuffer(CAPACITY)
        yield buffer
        buffer = None

    def test_is_empty_after_creation(self, buffer: CircularBuffer):
        assert_that(buffer.is_empty()).is_true()

    def test_is_not_null_after_creation(self, buffer: CircularBuffer):
        assert_that(buffer.is_full()).is_false()

    def test_is_not_empty_after_put(self, buffer: CircularBuffer):
        buffer.put(AN_ELEMENT)
        assert_that(buffer.is_empty()).is_false()

    def test_is_empty_after_put_then_get(self, buffer: CircularBuffer):
        buffer.put(AN_ELEMENT)
        buffer.get()
        assert_that(buffer.is_empty()).is_true()

    def test_get_equals_put_for_one_item(self, buffer: CircularBuffer):
        buffer.put(AN_ELEMENT)
        value = buffer.get()
        assert_that(value).is_equal_to(AN_ELEMENT)

    def test_get_is_fifo(self, buffer: CircularBuffer):
        buffer.put(FIRST_ELEMENT)
        buffer.put(SECOND_ELEMENT)
        buffer.put(THIRD_ELEMENT)
        assert_that(buffer.get()).is_equal_to(FIRST_ELEMENT)
        assert_that(buffer.get()).is_equal_to(SECOND_ELEMENT)
        assert_that(buffer.get()).is_equal_to(THIRD_ELEMENT)

    def test_report_capacity(self, buffer: CircularBuffer):
        assert_that(buffer.capacity()).is_equal_to(CAPACITY)

    def test_capacity_is_adjustable(self):
        buffer = CircularBuffer(CAPACITY + 10)
        assert_that(buffer.capacity()).is_equal_to(CAPACITY + 10)

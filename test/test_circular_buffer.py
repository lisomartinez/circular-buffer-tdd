import pytest
from src.circular_buffer import *
from assertpy import assert_that


class TestCircularBuffer:

    @pytest.fixture()
    def buffer(self) -> CircularBuffer:
        buffer = CircularBuffer()
        yield buffer
        buffer = None

    def test_is_empty_after_creation(self, buffer: CircularBuffer):
        assert_that(buffer.is_empty()).is_true()

    def test_is_not_null_after_creation(self, buffer: CircularBuffer):
        assert_that(buffer.is_full()).is_false()

    def test_is_not_empty_after_put(self, buffer: CircularBuffer):
        buffer.put(42)
        assert_that(buffer.is_empty()).is_false()

    def test_is_empty_after_put_then_get(self, buffer: CircularBuffer):
        buffer.put(42)
        buffer.get()
        assert_that(buffer.is_empty()).is_true()

    def test_get_equals_put_for_one_item(self, buffer: CircularBuffer):
        buffer.put(42)
        value = buffer.get()
        assert_that(value).is_equal_to(42)

    def test_get_is_fifo(self, buffer: CircularBuffer):
        buffer.put(41)
        buffer.put(42)
        buffer.put(43)
        assert_that(buffer.get()).is_equal_to(41)
        assert_that(buffer.get()).is_equal_to(42)
        assert_that(buffer.get()).is_equal_to(43)
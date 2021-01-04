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
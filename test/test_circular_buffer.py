import pytest
from src.circular_buffer import *
from assertpy import assert_that


class TestCircularBuffer:

    @pytest.fixture()
    def buffer(self):
        buffer = CircularBuffer()
        yield buffer
        buffer = None

    def test_is_empty_after_creation(self, buffer):
        buffer_content = buffer.is_empty()
        assert_that(buffer.is_empty()).is_true()

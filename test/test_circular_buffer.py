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

    @pytest.fixture()
    def filled_up_buffer(self) -> CircularBuffer:
        buffer = CircularBuffer(CAPACITY)
        for n in range(0, CAPACITY):
            buffer.put(n)
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

    def test_fill_to_capacity(self, filled_up_buffer: CircularBuffer):
        assert_that(filled_up_buffer.is_full()).is_true()

    def test_is_not_full_after_get_from_full_buffer(self, filled_up_buffer: CircularBuffer):
        filled_up_buffer.get()
        assert_that(filled_up_buffer.is_full()).is_false()

    def test_force_a_buffer_wraparound(self):
        buffer = CircularBuffer(2)
        buffer.put(1)
        buffer.put(2)
        buffer.get()
        buffer.put(3)
        assert_that(buffer.get()).is_equal_to(2)
        assert_that(buffer.get()).is_equal_to(3)
        assert_that(buffer.is_empty()).is_true()

    def test_full_after_wrapping(self):
        buffer = CircularBuffer(2)
        buffer.put(1)
        buffer.put(2)
        buffer.get()
        buffer.put(3)
        assert_that(buffer.is_full()).is_true()

    def test_put_to_full_fails(self):
        buffer = CircularBuffer(1)
        buffer.put(1)
        with pytest.raises(Exception):
            buffer.put(2)

    def test_get_from_empty_returns_default_value(self):
        buffer = CircularBuffer(1)
        with pytest.raises(Exception):
            buffer.get()

    def test_put_to_full_does_not_damage_contents(self):
        buffer = CircularBuffer(1)
        buffer.put(1)
        with pytest.raises(Exception):
            buffer.put(2)
        assert_that(buffer.get()).is_equal_to(1)
        assert_that(buffer.is_empty()).is_true()


"""tests for day 2"""
# pylint: disable=redefined-outer-name
# pylint: disable=import-error

import pytest
from day02 import total_wrapping_needed


@pytest.fixture
def test_input() -> list:
    """sample input"""
    return ['2x3x4', '1x1x10']


def test_part1(test_input: list) -> None:
    """test correct wrapping paper size"""
    assert total_wrapping_needed(test_input, 'paper') == 101


def test_part2(test_input: list) -> None:
    """test correct ribbon size"""
    assert total_wrapping_needed(test_input, 'ribbon') == 48


def test_val_error(test_input: list) -> None:
    """test value error raises"""
    with pytest.raises(ValueError):
        total_wrapping_needed(test_input, 'tape')

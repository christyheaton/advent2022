import pytest
from day02 import total_wrapping_needed


@pytest.fixture
def test_input() -> list:
    return ['2x3x4', '1x1x10']


def test_part1(test_input: list) -> None:
    assert total_wrapping_needed(test_input, 'paper') == 101


def test_part2(test_input: list) -> None:
    assert total_wrapping_needed(test_input, 'ribbon') == 48


def test_val_error(test_input: list) -> None:
    with pytest.raises(ValueError):
        total_wrapping_needed(test_input, 'tape')

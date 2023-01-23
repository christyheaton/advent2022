import pytest
from day9 import Rope, num_positions_occupied_by_tail


@pytest.fixture
def test_input_pt1() -> list:
    return ['R 4',
            'U 4',
            'L 3',
            'D 1',
            'R 4',
            'D 1',
            'L 5',
            'R 2']


@pytest.fixture
def test_input_pt2() -> list:
    return ['R 5',
            'U 8',
            'L 8',
            'D 3',
            'R 17',
            'D 10',
            'L 25',
            'U 20']


def test_part1(test_input_pt1: list) -> None:
    assert num_positions_occupied_by_tail(Rope(2), test_input_pt1) == 13


def test_part2(test_input_pt2: list) -> None:
    assert num_positions_occupied_by_tail(Rope(10), test_input_pt2) == 36

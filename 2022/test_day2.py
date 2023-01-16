import pytest
from day2 import game_summary


@pytest.fixture
def test_input():
    return ['A Y', 'B X', 'C Z']


def test_game_summary_part1(test_input):
    assert game_summary(test_input, 1) == 15


def test_game_summary_part2(test_input):
    assert game_summary(test_input, 2) == 12

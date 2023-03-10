"""tests for day 3"""
import pytest
from day03 import houses_receiving_presents, num_houses


@pytest.mark.parametrize('test_input,expected',
                         [('>', 2),
                          ('^>v<', 4),
                          ('^v^v^v^v^v', 2)])
def test_part1(test_input, expected):
    """test number of houses calculated correctly in part 1"""
    assert num_houses(houses_receiving_presents(test_input)) == expected


@pytest.mark.parametrize('test_input,expected',
                         [('^>', 3),
                          ('^>v<', 3),
                          ('^v^v^v^v^v', 11)])
def test_part2(test_input, expected):
    """test number of houses calculated correctly for part 2"""
    santa_instructions = test_input[::2]
    robo_santa_instructions = test_input[1::2]
    santa_houses = houses_receiving_presents(santa_instructions)
    robo_santa_houses = houses_receiving_presents(robo_santa_instructions)
    assert num_houses(santa_houses+robo_santa_houses) == expected

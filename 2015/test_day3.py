import pytest
from day3 import houses_receiving_presents


@pytest.mark.parametrize('test_input,expected',
                         [('>', 2),
                          ('^>v<', 4),
                          ('^v^v^v^v^v', 2)])
def test_part1(test_input, expected):
    assert houses_receiving_presents(test_input) == expected


@pytest.mark.parametrize('test_input,expected',
                         [('>', 3),
                          ('^>v<', 3),
                          ('^v^v^v^v^v', 11)])
def test_part2(test_input, expected):
    assert houses_receiving_presents_robo(test_input) == expected

import pytest
from day5 import is_nice_part1


@pytest.mark.parametrize('test_input,expected',
                         [('ugknbfddgicrmopn', True),
                          ('aaa', True),
                          ('jchzalrnumimnmhp', False),
                          ('haegwjzuvuyypxyu', False),
                          ('dvszwmarrgswjxmb', False)])
def test_part1(test_input, expected):
    assert is_nice_part1(test_input) == expected

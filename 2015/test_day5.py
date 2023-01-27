import pytest
from day5 import is_nice_part1, is_nice_part2, count_nice


@pytest.mark.parametrize('test_input,expected',
                         [('ugknbfddgicrmopn', True),
                          ('aaa', True),
                          ('jchzalrnumimnmhp', False),
                          ('haegwjzuvuyypxyu', False),
                          ('dvszwmarrgswjxmb', False)])
def test_part1(test_input, expected):
    assert is_nice_part1(test_input) == expected


@pytest.mark.parametrize('test_input,expected',
                         [('qjhvhtzxzqqjkmpb', True),
                          ('xxyxx', True),
                          ('uurcxstgmygtbstg', False),
                          ('ieodomkazucvgmuy', False)])
def test_part2(test_input, expected):
    assert is_nice_part2(test_input) == expected


@pytest.fixture
def test_input_pt1() -> list:
    return ['ugknbfddgicrmopn',
            'aaa',
            'jchzalrnumimnmhp',
            'haegwjzuvuyypxyu',
            'dvszwmarrgswjxmb']


def test_count_nice_pt1(test_input_pt1):
    assert count_nice(test_input_pt1, 1) == 2


@pytest.fixture
def test_input_pt2() -> list:
    return ['qjhvhtzxzqqjkmpb',
            'xxyxx',
            'uurcxstgmygtbstg',
            'ieodomkazucvgmuy']


def test_count_nice_pt2(test_input_pt2):
    assert count_nice(test_input_pt2, 2) == 2

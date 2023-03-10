"""tests for day 5"""
# pylint: disable=redefined-outer-name
# pylint: disable=import-error

import pytest
from day05 import is_nice_part1, is_nice_part2, count_nice


@pytest.mark.parametrize('test_input,expected',
                         [('ugknbfddgicrmopn', True),
                          ('aaa', True),
                          ('jchzalrnumimnmhp', False),
                          ('haegwjzuvuyypxyu', False),
                          ('dvszwmarrgswjxmb', False)])
def test_part1(test_input, expected):
    """test part 1 identifies nice strings correctly"""
    assert is_nice_part1(test_input) == expected


@pytest.mark.parametrize('test_input,expected',
                         [('qjhvhtzxzqqjkmpb', True),
                          ('xxyxx', True),
                          ('uurcxstgmygtbstg', False),
                          ('ieodomkazucvgmuy', False)])
def test_part2(test_input, expected):
    """test part 2 identifies nice strings correctly"""
    assert is_nice_part2(test_input) == expected


@pytest.fixture
def test_input_pt1() -> list:
    """sample input for part 1"""
    return ['ugknbfddgicrmopn',
            'aaa',
            'jchzalrnumimnmhp',
            'haegwjzuvuyypxyu',
            'dvszwmarrgswjxmb']


def test_count_nice_pt1(test_input_pt1):
    """test part 1 calculate count of nice strings correctly"""
    assert count_nice(test_input_pt1, 1) == 2


@pytest.fixture
def test_input_pt2() -> list:
    """sample input for part 2"""
    return ['qjhvhtzxzqqjkmpb',
            'xxyxx',
            'uurcxstgmygtbstg',
            'ieodomkazucvgmuy']


def test_count_nice_pt2(test_input_pt2):
    """test part 2 calculate count of nice strings correctly"""
    assert count_nice(test_input_pt2, 2) == 2

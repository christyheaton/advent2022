import pytest
import string
from day3 import get_item_total, get_badge_total


@pytest.fixture
def alphabet():
    return ''.join([string.ascii_lowercase, string.ascii_uppercase])


@pytest.fixture
def test_input():
    return ['vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw']


def test_get_item_total(alphabet, test_input):
    assert get_item_total(alphabet, test_input) == 157


def test_get_badge_total(alphabet, test_input):
    assert get_badge_total(alphabet, test_input) == 70

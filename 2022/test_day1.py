import pytest
from day1 import get_total_per_elf, get_total_top_elves


@pytest.fixture
def test_input():
    return ['1000',
            '2000',
            '3000',
            '',
            '4000',
            '',
            '5000',
            '6000',
            '',
            '7000',
            '8000',
            '9000',
            '',
            '10000']


def test_get_total_per_elf(test_input):
    assert get_total_per_elf(test_input) == [6000, 4000, 11000, 24000, 10000]


def test_get_total_top_elves(test_input):
    max_per_elf = get_total_per_elf(test_input)
    assert get_total_top_elves(max_per_elf, 3) == 45000

import pytest
from day4 import duplicate_work_id


@pytest.fixture
def test_input():
    return ['2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8']


def test_count_contains(test_input):
    count_contains, count_overlap = duplicate_work_id(test_input)
    assert count_contains == 2


def test_count_overlap(test_input):
    count_contains, count_overlap = duplicate_work_id(test_input)
    assert count_overlap == 4

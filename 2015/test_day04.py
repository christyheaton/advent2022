"""tests for day 4"""
import pytest
from day04 import check_md5_hash


@pytest.mark.parametrize('test_input,expected',
                         [('abcdef', 609043),
                          ('pqrstuv', 1048970)])
def test_part1(test_input, expected):
    """test part 1 returns correct value"""
    assert check_md5_hash(test_input, 5) == expected


@pytest.mark.parametrize('test_input,expected',
                         [('abcdef', 6742839),
                          ('pqrstuv', 5714438)])
def test_part2(test_input, expected):
    """test part 2 returns correct value"""
    assert check_md5_hash(test_input, 6) == expected

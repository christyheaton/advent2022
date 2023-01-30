import pytest
from day01 import floor_count


@pytest.mark.parametrize('test_input,expected',
                         [('(())', 0),
                          ('()()', 0),
                          ('(((', 3),
                          ('(()(()(', 3),
                          ('))(((((', 3),
                          ('())', -1),
                          ('))(', -1),
                          (')))', -3),
                          (')())())', -3)])
def test_floor_count(test_input, expected):
    assert floor_count(test_input) == expected


@pytest.mark.parametrize('test_input,expected',
                         [(')', 1),
                          ('()())', 5)])
def test_floor_count_basement_index(test_input, expected):
    assert floor_count(test_input, 2) == expected

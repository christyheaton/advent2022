"""tests for day 2"""
# pylint: disable=import-error

import pytest
from day02_2016 import CodeFinder


@pytest.fixture
def test_input():
    return ['ULL', 'RRDDD', 'LURDL', 'UUUUD']


def test_part1(test_input):
    """test part 1"""
    result = ''
    code_finder = CodeFinder()
    for inst in test_input:
        code_finder.execute_instruction_line(inst)
        result = result + code_finder.current_value()
    assert result == '1985'


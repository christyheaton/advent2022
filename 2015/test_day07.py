"""tests for day 7"""
# pylint: disable=redefined-outer-name
import pytest
from day07 import circuit_switch


@pytest.fixture
def test_input() -> list:
    """sample input"""
    return ['123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i']


def test_switches(test_input) -> None:
    """test circuits calculated correctly"""
    res = circuit_switch(test_input)
    assert res == {'x': 123,
                   'y': 456,
                   'd': 72,
                   'e': 507,
                   'f': 492,
                   'g': 114,
                   'h': 65412,
                   'i': 65079}

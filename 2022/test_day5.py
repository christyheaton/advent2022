import pytest
from day5 import format_container_data, perform_instructions, get_message


@pytest.fixture
def test_input() -> list:
    return ['    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 ',
            '',
            'move 1 from 2 to 1',
            'move 3 from 1 to 3',
            'move 2 from 2 to 1',
            'move 1 from 1 to 2']


@pytest.fixture
def instructions(test_input: list) -> str:
    return test_input[5:]


@pytest.fixture
def formatted_data(test_input: list) -> dict:
    stack_data = test_input[:3]
    return format_container_data(stack_data)


def test_part1(instructions: str, formatted_data: dict):
    shuffled = perform_instructions(instructions, formatted_data, 1)
    assert get_message(shuffled) == 'CMZ'


def test_part2(instructions: str, formatted_data: dict):
    shuffled = perform_instructions(instructions, formatted_data, 2)
    assert get_message(shuffled) == 'MCD'

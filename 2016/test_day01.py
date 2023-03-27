"""tests for day 1"""
# pylint: disable=import-error

import pytest
import copy
from day01 import Walker


@pytest.mark.parametrize('test_input,expected',
                         [(['R2', 'L3'], 5),
                          (['R2', 'R2', 'R2'], 2),
                          (['R5', 'L5', 'R5', 'R3'], 12)])
def test_part1(test_input, expected):
    """test part 1"""
    walker = Walker()
    for instruction in test_input:
        turn_direction = instruction[0]
        distance = int(instruction[1:])
        walker.turn(turn_direction)
        walker.move(distance)
    pt1_solution = abs(walker.position.x) + abs(walker.position.y)
    assert pt1_solution == expected


@pytest.mark.parametrize('test_input,expected',
                         [(['R8', 'R4', 'R4', 'R8'], 4)])
def test_part2(test_input, expected):
    """test part 2"""
    walker = Walker()
    for instruction in test_input:
        turn_direction = instruction[0]
        distance = int(instruction[1:])
        walker.turn(turn_direction)
        walker.move(distance)
    first_duplicate = [x for n, x in enumerate(walker.visited) if x in walker.visited[:n]][0]
    pt2_solution = abs(first_duplicate.x) + abs(first_duplicate.y)
    assert pt2_solution == expected


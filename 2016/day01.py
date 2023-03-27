# pylint: disable=import-error
"""advent of code 2016 day 1 https://adventofcode.com/2016/day/1"""
import copy
from dataclasses import dataclass
from aocd import get_data
# TODO: add logging


DIRECTIONS = ['N', 'E', 'S', 'W']

# TODO: replace with named tuple


@dataclass()
class Point:
    x: int
    y: int


class Walker:
    def __init__(self):
        self.position = Point(0, 0)
        self.facing = 'N'
        self.visited = []

    def turn(self, direction):
        dir_index = DIRECTIONS.index(self.facing)
        if direction == 'L':
            if dir_index == 0:
                new_facing = 'W'
            else:
                new_facing = DIRECTIONS[dir_index - 1]
        else:
            if dir_index == 3:
                new_facing = 'N'
            else:
                new_facing = DIRECTIONS[dir_index + 1]
        self.facing = new_facing

    def move(self, distance):
        for i in range(1, distance+1):
            match self.facing:
                case 'N':
                    self.position.y = self.position.y + 1
                case 'E':
                    self.position.x = self.position.x + 1
                case 'S':
                    self.position.y = self.position.y - 1
                case 'W':
                    self.position.x = self.position.x - 1
            self.visited.append(copy.deepcopy(self.position))


def main() -> None:
    """part 1 and 2 solutions"""
    instructions = get_data(day=1, year=2016).split(', ')
    walker = Walker()
    for instruction in instructions:
        turn_direction = instruction[0]
        distance = int(instruction[1:])
        walker.turn(turn_direction)
        walker.move(distance)
    pt1_solution = abs(walker.position.x) + abs(walker.position.y)
    print(f'Part 1 solution: {pt1_solution}')
    first_duplicate = [x for n, x in enumerate(walker.visited) if x in walker.visited[:n]][0]
    pt2_solution = abs(first_duplicate.x) + abs(first_duplicate.y)
    print(f'Part 2 solution: {pt2_solution}')


if __name__ == '__main__':
    main()

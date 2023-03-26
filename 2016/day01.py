# pylint: disable=import-error
"""advent of code 2016 day 1 https://adventofcode.com/2016/day/1"""
from dataclasses import dataclass
from aocd import get_data


DIRECTIONS = ['N', 'E', 'S', 'W']


@dataclass()
class Point:
    x: int
    y: int


class Walker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = Point(0, 0)
        self.facing = 'N'

    def turn(self, direction):
        pass

    def move(self):
        pass


def main() -> None:
    """start on part 1"""
    data = get_data(day=1, year=2016)
    print(data)


if __name__ == '__main__':
    main()

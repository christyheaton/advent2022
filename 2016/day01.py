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
        dir_index = DIRECTIONS.index(self.facing)
        if direction == 'L':
            if dir_index == 0:
                new_facing = 'W'
            else:
                new_facing = DIRECTIONS[dir_index - 1]
        else:
            if dir_index == 3:
                new_facing = 'S'
            else:
                new_facing = DIRECTIONS[dir_index + 1]
        self.facing = new_facing

    def move(self, distance):
        match self.facing:
            case 'N':
                self.position.y = self.position.y + distance
            case 'E':
                self.position.x = self.position.x + distance
            case 'S':
                self.position.y = self.position.y - distance
            case 'W':
                self.position.x = self.position.x - distance

            
def main() -> None:
    """start on part 1"""
    data = get_data(day=1, year=2016)
    print(data)


if __name__ == '__main__':
    main()

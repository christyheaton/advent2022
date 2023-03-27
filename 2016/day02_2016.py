# pylint: disable=import-error
"""advent of code 2016 day 1 https://adventofcode.com/2016/day/1"""

from aocd import get_data
import numpy as np


class CodeFinder:
    def __init__(self):
        self.num_pad = np.arange(1, 10).reshape(3, 3)
        self.vertical = 1
        self.horizontal = 1

    def execute_instruction_line(self, line):
        for instruction in line:
            self.move(instruction)

    def move(self, direction):
        if direction == 'U' and self.vertical > 0:
            self.vertical -= 1
        elif direction == 'D' and self.vertical < 2:
            self.vertical += 1
        elif direction == 'L' and self.horizontal > 0:
            self.horizontal -= 1
        elif direction == 'R' and self.horizontal < 2:
            self.horizontal += 1

    def current_value(self):
        return str(self.num_pad[self.vertical, self.horizontal])


def main() -> None:
    """part 1 start"""
    data = get_data(day=2, year=2016).split('\n')
    result = ''
    code_finder = CodeFinder()
    for inst in data:
        code_finder.execute_instruction_line(inst)
        result = result + code_finder.current_value()
    print(result)


if __name__ == '__main__':
    main()

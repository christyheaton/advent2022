# pylint: disable=import-error
"""advent of code 2016 day 2 https://adventofcode.com/2016/day/2"""

from aocd import get_data
import numpy as np


class CodeFinder:
    def __init__(self, part: int):
        self.part = part
        if part == 1:
            self.num_pad = np.arange(1, 10).reshape(3, 3)
        elif part == 2:
            self.num_pad = self.create_num_pad_pt2()
        else:
            raise ValueError("Part must be '1' or '2'")
        self.vertical = 1
        self.horizontal = 1

    @staticmethod
    def create_num_pad_pt2() -> np.array:
        num_pad = np.zeros((5, 5), dtype=str)
        num_pad[0, 2] = "1"
        num_pad[1, 1], num_pad[1, 2], num_pad[1,3] = "2", "3", "4"
        num_pad[2, 0], num_pad[2, 1], num_pad[2,2], num_pad[2,3], num_pad[2,4] = "5", "6", "7", "8", "9"
        num_pad[3, 1], num_pad[3, 2], num_pad[3,3] = "A", "B", "C"
        num_pad[4, 2] = "D"
        return num_pad

    def execute_instruction_line(self, line: list) -> None:
        if self.part == 1:
            for instruction in line:
                self.move_pt1(instruction)
        else:
            for instruction in line:
                self.move_pt2(instruction)

    def move_pt1(self, direction: str) -> None:
        if direction == 'U' and self.vertical > 0:
            self.vertical -= 1
        elif direction == 'D' and self.vertical < 2:
            self.vertical += 1
        elif direction == 'L' and self.horizontal > 0:
            self.horizontal -= 1
        elif direction == 'R' and self.horizontal < 2:
            self.horizontal += 1


    def move_pt2(self, direction: str) -> None:
        if direction == 'U' and self.vertical > 0:
            if self.num_pad[self.horizontal, self.vertical -1]:
                self.vertical -= 1
        elif direction == 'D' and self.vertical < 4:
            if self.num_pad[self.horizontal, self.vertical +1]:
                self.vertical += 1
        elif direction == 'L' and self.horizontal > 0:
            if self.num_pad[self.horizontal - 1, self.vertical]:
                self.horizontal -= 1
        elif direction == 'R' and self.horizontal < 4:
            if self.num_pad[self.horizontal + 1, self.vertical]:
                self.horizontal += 1


    def current_value(self) -> str:
        return str(self.num_pad[self.vertical, self.horizontal])


def main() -> None:
    data = get_data(day=2, year=2016).split('\n')

    for part in range(1, 3):
        result = ''
        code_finder = CodeFinder(part)
        for inst in data:
            code_finder.execute_instruction_line(inst)
            result = result + code_finder.current_value()
        print(f'Part {part} solution: {result}')


if __name__ == '__main__':
    main()

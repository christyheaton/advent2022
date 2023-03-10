"""advent of code 2015 day 1 https://adventofcode.com/2015/day/1"""
from aocd import get_data


def floor_count(input_data: str, part: int = 0) -> int:
    """calculate final floor to deliver presents"""
    floor = 0
    for i in enumerate(input_data, 1):
        if i[1] == '(':
            floor += 1
        elif i[1] == ')':
            floor -= 1
        else:
            raise ValueError('Instruction must be either "(" or ")".')
        if part == 2:
            if floor < 0:
                return i[0]
    return floor


def main() -> None:
    """solutions for parts 1 and 2"""
    input_data: str = get_data(day=1, year=2015)
    try:
        print(f'Part 1: {floor_count(input_data)}')
        print(f'Part 2: {floor_count(input_data, 2)}')
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    main()

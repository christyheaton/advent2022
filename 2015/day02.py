"""advent of code 2015 day 2 https://adventofcode.com/2015/day/2"""

from ast import literal_eval
from aocd import get_data


def total_wrapping_needed(input_data: list, wrapping_type: str) -> int:
    """calculate amount of wrapping paper needed"""
    sizes = []
    for dims in input_data:
        dims = dims.split('x')
        dims = sorted([literal_eval(i) for i in dims])
        length, width, height = dims[0], dims[1], dims[2]
        if wrapping_type == 'paper':
            slack = dims[0] * dims[1]
            sizes.append(((2 * length * width) +
                          (2 * width * height) +
                          (2 * height * length)) +
                         slack)
        elif wrapping_type == 'ribbon':
            sizes.append(length + length + width + width + (length * width * height))
        else:
            raise ValueError('That wrapping type is not available')
    return sum(sizes)


def main() -> None:
    """solutions for parts 1 and 2"""
    input_data: list = get_data(day=2, year=2015).splitlines()
    print(f"Part 1: {total_wrapping_needed(input_data, 'paper')}")
    print(f"Part 2: {total_wrapping_needed(input_data, 'ribbon')}")


if __name__ == '__main__':
    main()

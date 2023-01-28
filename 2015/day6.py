from aocd import get_data
import numpy as np


def create_grid(size: int) -> dict:
    grid = {}
    for x in range(size):
        for y in range(size):
            grid[(x, y)] = False
    return grid


def create_npgrid(size):
    return np.full((size, size), False)


def parse_instructions(instruction: str) -> tuple:
    i_sp = instruction.split()
    if i_sp[0] == 'turn':
        i_sp = i_sp[1:]
    inst = i_sp[0]
    start_x, start_y = i_sp[1].split(',')
    end_x, end_y = i_sp[3].split(',')
    return inst, int(start_x), int(start_y), int(end_x), int(end_y)


def perform_instructions(instructions: list, grid: dict) -> dict:
    for i in instructions:
        inst, start_x, start_y, end_x, end_y = parse_instructions(i)
        for k, v in grid.items():
            if start_x <= k[0] <= end_x and start_y <= k[1] <= end_y:
                if inst == 'on':
                    grid[k] = True
                elif inst == 'off':
                    grid[k] = False
                else:
                    grid[k] = not grid[k]
    return grid


def perform_inst_npgrid(instructions, npgrid):
    for i in instructions:
        inst, start_x, start_y, end_x, end_y = parse_instructions(i)
        if inst == 'on':
            npgrid[start_x:end_x + 1, start_y:end_y + 1] = True
        elif inst == 'off':
            npgrid[start_x:end_x + 1, start_y:end_y + 1] = False
        else:
            npgrid[start_x:end_x + 1,
                   start_y:end_y + 1] = np.invert(npgrid[start_x:end_x + 1,
                                                         start_y:end_y + 1])
    return npgrid


def main() -> None:
    input_data: list = get_data(day=6, year=2015).splitlines()
    # grid = create_grid(1_000)
    # perform_instructions(input_data, grid)
    # print(f'Part 1: {sum(grid.values())}')
    grid = create_npgrid(1_000)
    grid = perform_inst_npgrid(input_data, grid)
    print(f'Part 1: {np.sum(grid)}')


if __name__ == '__main__':
    main()

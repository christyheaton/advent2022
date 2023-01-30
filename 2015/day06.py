from aocd import get_data
import numpy as np


def create_npgrid_pt1(size):
    return np.full((size, size), False)


def create_npgrid_pt2(size):
    return np.zeros((size, size))


def parse_instructions(instruction: str) -> tuple:
    i_sp = instruction.split()
    if i_sp[0] == 'turn':
        i_sp = i_sp[1:]
    inst = i_sp[0]
    start_x, start_y = i_sp[1].split(',')
    end_x, end_y = i_sp[3].split(',')
    return inst, int(start_x), int(start_y), int(end_x), int(end_y)


def perform_instructions_pt1(instructions, npgrid):
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


def perform_instructions_pt2(instructions, npgrid):
    for i in instructions:
        inst, start_x, start_y, end_x, end_y = parse_instructions(i)
        if inst == 'on':
            npgrid[start_x:end_x + 1, start_y:end_y + 1] += 1
        elif inst == 'off':
            npgrid[start_x:end_x + 1, start_y:end_y + 1] -= 1
            npgrid[npgrid < 0] = 0
        else:
            npgrid[start_x:end_x + 1, start_y:end_y + 1] += 2
    return npgrid


def main() -> None:
    input_data: list = get_data(day=6, year=2015).splitlines()
    grid1 = create_npgrid_pt1(1_000)
    perform_instructions_pt1(input_data, grid1)
    print(f'Part 1: {np.sum(grid1)}')

    grid2 = create_npgrid_pt2(1_000)
    perform_instructions_pt2(input_data, grid2)
    print(f'Part 2: {int(np.sum(grid2))}')


if __name__ == '__main__':
    main()

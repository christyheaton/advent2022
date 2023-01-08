from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Cycle:
    count: int
    x: int
    instruction: str


def add_cycle(instruction_line: str) -> None:
    """

    :param instruction_line:
    :return:
    """
    return cycles.append(Cycle(count=cycle, x=x, instruction=instruction_line))


def draw(x_val, draw_position):
    if x_val in [draw_position-1, draw_position, draw_position+1]:
        draw_char = '#'
    else:
        draw_char = '.'
    if draw_position %  == 0 and draw_position:
        print(f'{draw_char}\n', end='')
        draw_position = 0
    else:
        print(draw_char, end='')
    draw_position += 1
    return draw_position


if __name__ == '__main__':
    input_data = get_data(day=10, year=2022).splitlines()
    cycles = []
    cycle = 0
    x = 1
    draw_pos = 0

    for line in input_data:
        cycle += 1
        draw_pos = draw(x, draw_pos)
        if line == 'noop':
            add_cycle(line)
            continue
        instruction, increment = line.split()
        add_cycle(line)
        cycle += 1
        draw_pos = draw(x, draw_pos)
        add_cycle(line)
        x += int(increment)

    part1 = 0
    for c in cycles:
        if c.count in [20, 60, 100, 140, 180, 220]:
            part1 += (c.count * c.x)
    print()
    print(f'Part 1 answer is {part1}.')

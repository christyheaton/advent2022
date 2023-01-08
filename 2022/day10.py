from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Cycle:
    count: int
    x: int
    instruction: str


def add_cycle(instruction_line: str, cycles: list, cycle: int, x: int) -> None:
    """
    Appends a new cycle to the cycles list
    :param instruction_line: the current instruction line
    :param cycles: the list of cycles
    :param cycle: the current cycle
    :param x: the value of x in the cycle
    :return: the cycles list with a new cycle appended
    """
    return cycles.append(Cycle(count=cycle, x=x, instruction=instruction_line))


def draw(x_val: int, draw_position: int) -> int:
    """
    Draws a # if the sprite is visible, a . if not.
    Starts a new line every 40 characters.
    :param x_val: the x value in the cycle
    :param draw_position: the current pixel on the line
    :return: the draw_position to use next time this function is called
    """
    if x_val in [draw_position-1, draw_position, draw_position+1]:
        draw_char = '#'
    else:
        draw_char = '.'
    if draw_position == 39:
        print(f'{draw_char}\n', end='')
        draw_position = 0
    else:
        print(draw_char, end='')
        draw_position += 1
    return draw_position


def generate_cycles(input_data: list) -> list[Cycle]:
    """
    Generates a list of cycles from the input_data
    and draws the output as it goes
    :param input_data: the provided input data
    :return: a list of Cycles
    """
    cycles = []
    cycle = 0
    x = 1
    draw_pos = 0
    for line in input_data:
        cycle += 1
        draw_pos = draw(x, draw_pos)
        if line == 'noop':
            add_cycle(line, cycles, cycle, x)
            continue
        instruction, increment = line.split()
        add_cycle(line, cycles, cycle, x)
        cycle += 1
        draw_pos = draw(x, draw_pos)
        add_cycle(line, cycles, cycle, x)
        x += int(increment)
    return cycles


def main() -> None:
    input_data = get_data(day=10, year=2022).splitlines()
    print('Part 2 answer is:')
    cycles = generate_cycles(input_data)
    part1 = 0
    for c in cycles:
        if c.count in [20, 60, 100, 140, 180, 220]:
            part1 += (c.count * c.x)
    print()
    print(f'Part 1 answer is {part1}.')


if __name__ == '__main__':
    main()

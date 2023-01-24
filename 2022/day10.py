from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Cycle:
    count: int
    x: int
    instruction: str


def add_cycle(instruction_line: str, cycles: list, cycle: int, x: int) -> None:
    return cycles.append(Cycle(count=cycle, x=x, instruction=instruction_line))


def draw(x_val: int, draw_position: int) -> int:
    if x_val in (draw_position-1, draw_position, draw_position+1):
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


def sum_signal_strengths(cycle_list: list, intervals: tuple) -> int:
    total = 0
    for c in cycle_list:
        if c.count in intervals:
            total += (c.count * c.x)
    return total


def main() -> None:
    input_data = get_data(day=10, year=2022).splitlines()
    print('Part 2 answer is:')
    cycles = generate_cycles(input_data)
    print()
    intervals = (20, 60, 100, 140, 180, 220)
    print(f'Part 1 answer is {sum_signal_strengths(cycles, intervals)}.')


if __name__ == '__main__':
    main()

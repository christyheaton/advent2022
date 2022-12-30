from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Cycle:
    count: int
    x: int
    instruction: str


def add_cycle(instruction_line):
    return cycles.append(Cycle(count=cycle, x=x, instruction=instruction_line))


if __name__ == '__main__':
    input_data = get_data(day=10, year=2022).splitlines()
    cycles = []
    cycle = 0
    x = 1
    
    for line in input_data:
        cycle += 1
        if line == 'noop':
            add_cycle(line)
            continue
        instruction, increment = line.split()
        add_cycle(line)
        cycle += 1
        add_cycle(line)
        x += int(increment)

    part1 = 0
    for c in cycles:
        if c.count in [20, 60, 100, 140, 180, 220]:
            part1 += (c.count * c.x)
    print(f'Part 1 answer is {part1}.')

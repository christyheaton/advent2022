from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Cycle:
    count: int
    x: int
    instruction: str


if __name__ == '__main__':
    input_data = get_data(day=10, year=2022).splitlines()
    cycles = []
    cycle = 0
    x = 1
    for line in input_data:
        cycle += 1
        if line == 'noop':
            cycles.append(Cycle(count=cycle, x=x, instruction=line))
            continue
        instruction, increment = line.split()
        cycles.append(Cycle(count=cycle, x=x, instruction=f'{instruction} {increment}'))
        cycle += 1
        x += int(increment)
        cycles.append(Cycle(count=cycle, x=x, instruction=f'{instruction} {increment}'))

    part1 = 0
    for c in cycles:
        if c.count in [20, 60, 100, 140, 180, 220]:
            print(f'Adding {c.count} * {c.x} = {c.count * c.x}')
            part1 += (c.count * c.x)

    print(part1)
    print(cycles)

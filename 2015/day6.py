from aocd import get_data


def create_grid(size: int) -> dict:
    grid = {}
    for x in range(size):
        for y in range(size):
            grid[(x, y)] = False
    return grid


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


def main() -> None:
    input_data: list = get_data(day=6, year=2015).splitlines()
    grid = create_grid(1_000)
    perform_instructions(input_data, grid)
    print(f'Part 1: {sum(grid.values())}')


if __name__ == '__main__':
    main()

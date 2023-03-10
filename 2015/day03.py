"""advent of code 2015 day 3 https://adventofcode.com/2015/day/3"""
# pylint: disable=import-error

from aocd import get_data


def move(coordinates: tuple, direction: str) -> tuple:
    """return new coordinates after move"""
    x_coord = coordinates[0]
    y_coord = coordinates[1]
    match direction:
        case '^':
            y_coord += 1
        case 'v':
            y_coord -= 1
        case '>':
            x_coord += 1
        case '<':
            x_coord -= 1
    return x_coord, y_coord


def houses_receiving_presents(input_data: str) -> list:
    """calculate record of houses receiving presents"""
    x_loc = 0
    y_loc = 0
    house_record = [(x_loc, y_loc)]
    for direction in input_data:
        x_loc, y_loc = move((x_loc, y_loc), direction)
        house_record.append((x_loc, y_loc))
    return house_record


def num_houses(visited_houses: list) -> int:
    """calculate number of houses"""
    return len(list(set(visited_houses)))


def main() -> None:
    """solutions for parts 1 and 2"""
    data: str = get_data(day=3, year=2015)
    print(f'Part 1: {num_houses(houses_receiving_presents(data))}')

    santa_instructions = data[::2]
    robo_santa_instructions = data[1::2]
    santa_houses = houses_receiving_presents(santa_instructions)
    robo_santa_houses = houses_receiving_presents(robo_santa_instructions)

    print(f'Part 2: {num_houses(santa_houses+robo_santa_houses)}')


if __name__ == '__main__':
    main()

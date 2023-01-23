from aocd import get_data


def move(coordinates: tuple, direction: str) -> tuple:
    x = coordinates[0]
    y = coordinates[1]
    match direction:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '>':
            x += 1
        case '<':
            x -= 1
    return x, y


def houses_receiving_presents(input_data: str) -> list:
    x = 0
    y = 0
    house_record = [(x, y)]
    for direction in input_data:
        x, y = move((x, y), direction)
        house_record.append((x, y))
    return house_record


def num_houses(visited_houses: list) -> int:
    return len(list(set(visited_houses)))


def main() -> None:
    data: str = get_data(day=3, year=2015)
    print(f'Part 1: {num_houses(houses_receiving_presents(data))}')

    santa_instructions = data[::2]
    robo_santa_instructions = data[1::2]
    santa_houses = houses_receiving_presents(santa_instructions)
    robo_santa_houses = houses_receiving_presents(robo_santa_instructions)

    print(f'Part 2: {num_houses(santa_houses+robo_santa_houses)}')


if __name__ == '__main__':
    main()

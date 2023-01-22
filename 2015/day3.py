from aocd import get_data


def houses_receiving_presents(input_data: str) -> int:
    x = 0
    y = 0
    house_record = [(x, y)]
    for direction in input_data:
        match direction:
            case '^':
                y += 1
            case 'v':
                y -= 1
            case '>':
                x += 1
            case '<':
                x -= 1
        if (x, y) not in house_record:
            house_record.append((x, y))
    return len(house_record)


def main() -> None:
    data: str = get_data(day=3, year=2015)
    print(houses_receiving_presents(data))


if __name__ == '__main__':
    main()

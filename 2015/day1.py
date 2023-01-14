from aocd import get_data


def floor_count(input_data: str, part: int = 0) -> int:
    floor = 0
    for i in enumerate(input_data):
        if part == 2:
            if floor < 0:
                return i[0]
        if i[1] == '(':
            floor += 1
        elif i[1] == ')':
            floor -= 1
        else:
            raise ValueError('Instruction must be either "(" or ")".')
    return floor


def main() -> None:
    input_data: str = get_data(day=1, year=2015)
    try:
        floor_num = floor_count(input_data)
        index_at_basement = floor_count(input_data, 2)
        print(f'Part 1: {floor_num}')
        print(f'Part 2: {index_at_basement}')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()

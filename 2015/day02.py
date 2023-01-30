from aocd import get_data


def total_wrapping_needed(input_data: list, wrapping_type: str) -> int:
    sizes = []
    for dims in input_data:
        dims = dims.split('x')
        dims = sorted([eval(i) for i in dims])
        l, w, h = dims[0], dims[1], dims[2]
        if wrapping_type == 'paper':
            slack = dims[0] * dims[1]
            sizes.append(((2 * l * w) + (2 * w * h) + (2 * h * l)) + slack)
        elif wrapping_type == 'ribbon':
            sizes.append(l+l+w+w + (l*w*h))
        else:
            raise ValueError('That wrapping type is not available')
    return sum(sizes)


def main() -> None:
    input_data: list = get_data(day=2, year=2015).splitlines()
    print(f"Part 1: {total_wrapping_needed(input_data, 'paper')}")
    print(f"Part 2: {total_wrapping_needed(input_data, 'ribbon')}")


if __name__ == '__main__':
    main()

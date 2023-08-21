
def main() -> None:
    f = open("data/adventofcode.com_2016_day_3_input.txt", "r")
    lines = f.readlines()

    # part 1
    counter = 0
    for line in lines:
        a, b, c = [int(x) for x in line.split()]
        if a + b > c and a + c > b and b + c > a:
            counter += 1
    print(f"Part 1 solution: {counter}")

    #part 2
    old_format = []
    for line in lines:
        row = [int(x) for x in line.split()]
        old_format.append(row)
    new_format = [item[0] for item in old_format] + [item[1] for item in old_format] + [item[2] for item in old_format]

    counter = 0
    while new_format:
        a, b, c = [new_format.pop() for _ in range(3)]
        if a + b > c and a + c > b and b + c > a:
            counter += 1
    print(f"Part 2 solution: {counter}")


if __name__ == "__main__":
    main()
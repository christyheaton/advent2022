from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Monkey:
    monkey_id: int
    starting_items: list
    operation: str
    test_divisible_by: int
    test_response: list


def main() -> None:
    input_data = get_data(day=11, year=2022).splitlines()
    monkeys = []
    my_data = ''.join(input_data)
    my_data = my_data.split('Monkey')
    for line in my_data:
        line = line.strip()
        if line:
            monkey_id = int(line[0])
            line = line.split('  ')
            starting_items = line[1].split('Starting items: ')[1].split(', ')
            operation = line[2].split('Operation: ')[1]
            test = int(line[3].split('Test: ')[1][-1])
            test_response = line[-3:]
            monkeys.append(Monkey(monkey_id=monkey_id,
                                  starting_items=starting_items,
                                  operation=operation,
                                  test_divisible_by=test,
                                  test_response=test_response))
    for monkey in monkeys:
        print(monkey)


if __name__ == '__main__':
    main()

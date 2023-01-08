from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Monkey:
    monkey_id: int
    starting_items: list
    operation: str
    test_divisible_by: int
    if_true_throw_to: int
    if_false_throw_to: int


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
            if_true_throw_to = int(test_response[0][-1])
            if_false_throw_to = int(test_response[2][-1])
            monkeys.append(Monkey(monkey_id=monkey_id,
                                  starting_items=starting_items,
                                  operation=operation,
                                  test_divisible_by=test,
                                  if_true_throw_to=if_true_throw_to,
                                  if_false_throw_to=if_false_throw_to))
    for monkey in monkeys:
        print(monkey)


if __name__ == '__main__':
    main()

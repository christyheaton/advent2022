from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Monkey:
    monkey_id: int
    items: list
    operation: str
    test_divisible_by: int
    if_true_throw_to: int
    if_false_throw_to: int


def gen_monkey_list(input_data: str) -> list[Monkey]:
    """
    Generates a list of monkeys given the input data
    :param input_data: a string with monkey information
    :return: a list of monkey objects
    """
    monkeys = []
    my_data = input_data.split('Monkey ')
    for monkey in my_data:
        monkey = monkey.strip()
        if not monkey:
            continue
        monkey_id = int(monkey[0])
        monkey = monkey.splitlines()
        items = monkey[1].split('  Starting items: ')[1].split(', ')
        items = [eval(i) for i in items]
        operation = monkey[2].split('  Operation: new = ')[1]
        test = int(monkey[3].split('  Test: ')[1][-1])
        test_response = monkey[-2:]
        if_true_throw_to = int(test_response[0][-1])
        if_false_throw_to = int(test_response[1][-1])
        monkeys.append(Monkey(monkey_id=monkey_id,
                              items=items,
                              operation=operation,
                              test_divisible_by=test,
                              if_true_throw_to=if_true_throw_to,
                              if_false_throw_to=if_false_throw_to))
    return monkeys


def inspect(monkey: Monkey) -> None:
    """
    Changes the monkey's items according to the monkey's operation
    :param monkey: a monkey
    :return: None
    """
    monkey.items = [eval(monkey.operation) for old in monkey.items]


def throw(monkeys) -> None:
    """
    Tests divisibility and throws item to the appropriate monkey
    :param monkeys: a lit of monkeys
    :return: None
    """
    for monkey in monkeys:
        for item in monkey.items:
            if item % monkey.test_divisible_by == 0:
                print(f'Throw to monkey {monkey.if_true_throw_to}')
            else:
                print(f'Throw to monkey {monkey.if_false_throw_to}')


def main() -> None:
    input_data = get_data(day=11, year=2022)
    monkeys = gen_monkey_list(input_data)

    for monkey in monkeys:
        inspect(monkey)

    throw(monkeys)


if __name__ == '__main__':
    main()

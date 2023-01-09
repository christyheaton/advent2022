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
    monkey_business_factor: int = 0


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
        test = int(monkey[3].split('  Test: ')[1].split()[-1])
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
    monkey.items = [int(eval(monkey.operation) / 3) for old in monkey.items]


def throw(monkeys) -> None:
    """
    Tests divisibility and throws item to the appropriate monkey
    :param monkeys: a list of monkeys
    :return: None
    """
    for monkey in monkeys:
        inspect(monkey)
        print(f'Monkey {monkey.monkey_id} has {len(monkey.items)} items: {monkey.items}.')
        while monkey.items:
            monkey.monkey_business_factor += 1
            item = monkey.items[0]
            print(f'Current item is {item}')
            if item % monkey.test_divisible_by == 0:
                print(f'{item} is divisible by {monkey.test_divisible_by}')
                print(f'Monkey {monkey.monkey_id} throws item {item} to monkey {monkey.if_true_throw_to}')
                monkeys[monkey.if_true_throw_to].items.append(monkey.items.pop(0))
            else:
                print(f'{item} is not divisible by {monkey.test_divisible_by}')
                print(f'Monkey {monkey.monkey_id} throws item {item} to monkey {monkey.if_false_throw_to}')
                monkeys[monkey.if_false_throw_to].items.append(monkey.items.pop(0))
            print(f'Monkey {monkey.monkey_id} now has {len(monkey.items)} items: {monkey.items}.')


def main() -> None:
    input_data = get_data(day=11, year=2022)
    monkeys = gen_monkey_list(input_data)

    for r in range(20):
        print(f'Round {r}')
        throw(monkeys)

    print(monkeys)
    monkey_business_factors = sorted([m.monkey_business_factor for m in monkeys])
    print(f'Part 1 solution: {monkey_business_factors[-1] * monkey_business_factors[-2]}')


if __name__ == '__main__':
    main()

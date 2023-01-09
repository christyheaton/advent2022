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
    monkeys: list[Monkey] = []
    my_data: list = input_data.split('Monkey ')
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


def inspect(monkey: Monkey, trick) -> None:
    """
    Changes the monkey's items according to the monkey's operation
    :param monkey: a monkey
    :param trick: all the test numbers multiplied together for
                  use in part 2. for part 1 use 0
    :return: None
    """
    if trick == 0:
        monkey.items = [eval(monkey.operation) // 3 for old in monkey.items]
    else:
        monkey.items = [eval(monkey.operation) % trick for old in monkey.items]


def throw(monkeys, trick) -> None:
    """
    Tests divisibility and throws item to the appropriate monkey
    :param monkeys: a list of monkeys
    :param trick: all the test numbers multiplied together for
                  use in part 2. for part 1 use 0
    :return: None
    """
    for monkey in monkeys:
        inspect(monkey, trick)
        while monkey.items:
            monkey.monkey_business_factor += 1
            item = monkey.items[0]
            if item % monkey.test_divisible_by == 0:
                monkeys[monkey.if_true_throw_to].items.append(monkey.items.pop(0))
            else:
                monkeys[monkey.if_false_throw_to].items.append(monkey.items.pop(0))


def monkey_business(monkeys: list[Monkey]) -> int:
    """
    Calculates the solution for part 1 and 2
    :param monkeys: a list of Monkeys
    :return: the highest 2 monkey business factors multiplied together
    """
    monkey_business_factors = sorted([m.monkey_business_factor for m in monkeys])
    return monkey_business_factors[-1] * monkey_business_factors[-2]


def main() -> None:
    input_data: str = get_data(day=11, year=2022)

    # Part 1
    monkeys: list[Monkey] = gen_monkey_list(input_data)
    for r in range(20):
        throw(monkeys, 0)
    print(f'Part 1 solution: {monkey_business(monkeys)}')

    # Part 2
    monkeys: list[Monkey] = gen_monkey_list(input_data)
    test_nums: list[int, ...] = [m.test_divisible_by for m in monkeys]
    trick = 1
    for num in test_nums:
        trick *= num
    for r in range(10_000):
        throw(monkeys, trick)
    print(f'Part 2 solution: {monkey_business(monkeys)}')


if __name__ == '__main__':
    main()

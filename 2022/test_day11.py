import pytest
from day11 import Monkey, monkey_business, gen_monkey_list
from collections import deque


@pytest.fixture
def test_input() -> str:
    return 'Monkey 0:\n'
'  Starting items: 79, 98\n'
'  Operation: new = old * 19\n'
'  Test: divisible by 23\n'
'    If true: throw to monkey 2\n'
'    If false: throw to monkey 3\n'
''
'Monkey 1:\n'
'  Starting items: 54, 65, 75, 74\n'
'  Operation: new = old + 6\n'
'  Test: divisible by 19\n'
'    If true: throw to monkey 2\n'
'    If false: throw to monkey 0\n'
''
'Monkey 2:\n'
'  Starting items: 79, 60, 97\n'
'  Operation: new = old * old\n'
'  Test: divisible by 13\n'
'    If true: throw to monkey 1\n'
'    If false: throw to monkey 3\n'
''
'Monkey 3:\n'
'  Starting items: 74\n'
'  Operation: new = old + 3\n'
'  Test: divisible by 17\n'
'    If true: throw to monkey 0\n'
'    If false: throw to monkey 1\n'


@pytest.mark.skip(reason="working on this")
def test_part1(test_input: str) -> None:
    monkeys: deque[Monkey] = gen_monkey_list(test_input)
    assert monkey_business(monkeys) == 10605

from aocd import get_data
import string


def get_item_total(alphabet: str, contents: list) -> int:
    total = 0
    for d in contents:
        half = int(len(d) / 2)
        item = ''.join(list(set(d[0:half]) & set(d[half:])))
        total += alphabet.index(item) + 1
    return total


def get_badge_total(alphabet: str, contents: list) -> int:
    group = list(zip(*[iter(contents)] * 3))
    total = 0
    for g in group:
        shared_item = ''.join(list(set(g[0]) & set(g[1]) & set(g[2])))
        total += alphabet.index(shared_item) + 1
    return total


if __name__ == '__main__':
    data = get_data(day=3, year=2022).splitlines()
    letters: str = ''.join([string.ascii_lowercase, string.ascii_uppercase])

    print(f'Part 1: Shared item in rucksack total is {get_item_total(letters, data)}.')
    print(f'Part 2: Badge total is {get_badge_total(letters, data)}.')

from aocd import get_data


def count_nice(data: list, part) -> int:
    if part == 1:
        return len([s for s in data if is_nice_part1(s)])


def is_nice_part1(s: str) -> bool:
    not_allowed = ('ab', 'cd', 'pq', 'xy')
    if any(seq in s for seq in not_allowed):
        return False

    count_vowels = 0
    three_vowels = False
    vowels = ('a', 'e', 'i', 'o', 'u')
    for v in vowels:
        count_vowels += s.count(v)
    if count_vowels >= 3:
        three_vowels = True

    double_letters = False
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            double_letters = True

    if all((three_vowels, double_letters)):
        return True
    else:
        return False


def main() -> None:
    input_data: list = get_data(day=5, year=2015).splitlines()
    print(f'Part 1: {count_nice(input_data, 1)}')


if __name__ == '__main__':
    main()

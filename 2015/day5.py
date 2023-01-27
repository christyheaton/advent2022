from aocd import get_data


def count_nice(data: list, part) -> int:
    if part == 1:
        return len([s for s in data if is_nice_part1(s)])
    elif part == 2:
        return len([s for s in data if is_nice_part2(s)])


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
            break

    return all((three_vowels, double_letters))


def is_nice_part2(s: str) -> bool:
    double_letters_separated = False
    for i in range(2, len(s)):
        if s[i-2] == s[i]:
            double_letters_separated = True
            break

    repeated_letters = False
    for i in range(1, len(s)):
        subset = s[i-1:i+1]
        if len(s.split(subset)) == 3:
            repeated_letters = True
            break
    return all((double_letters_separated, repeated_letters))


def main() -> None:
    input_data: list = get_data(day=5, year=2015).splitlines()
    print(f'Part 1: {count_nice(input_data, 1)}')
    print(f'Part 2: {count_nice(input_data, 2)}')


if __name__ == '__main__':
    main()

"""advent of code 2015 day 5 https://adventofcode.com/2015/day/5"""
# pylint: disable=import-error

from aocd import get_data


def count_nice(data: list, part) -> int:
    """count nice strings"""
    if part == 1:
        return len([s for s in data if is_nice_part1(s)])
    return len([s for s in data if is_nice_part2(s)])


def is_nice_part1(string: str) -> bool:
    """check if string is nice according to part 1 logic"""
    not_allowed = ('ab', 'cd', 'pq', 'xy')
    if any(seq in string for seq in not_allowed):
        return False

    count_vowels = 0
    three_vowels = False
    vowels = ('a', 'e', 'i', 'o', 'u')
    for vowel in vowels:
        count_vowels += string.count(vowel)
    if count_vowels >= 3:
        three_vowels = True

    double_letters = False
    for index in range(1, len(string)):
        if string[index - 1] == string[index]:
            double_letters = True
            break

    return all((three_vowels, double_letters))


def is_nice_part2(string: str) -> bool:
    """check if string is nice according to port 2 logic"""
    double_letters_separated = False
    for i in range(2, len(string)):
        if string[i - 2] == string[i]:
            double_letters_separated = True
            break

    repeated_letters = False
    for i in range(1, len(string)):
        subset = string[i - 1:i + 1]
        if len(string.split(subset)) == 3:
            repeated_letters = True
            break
    return all((double_letters_separated, repeated_letters))


def main() -> None:
    """solutions for parts 1 and 2"""
    input_data: list = get_data(day=5, year=2015).splitlines()
    print(f'Part 1: {count_nice(input_data, 1)}')
    print(f'Part 2: {count_nice(input_data, 2)}')


if __name__ == '__main__':
    main()

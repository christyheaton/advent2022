import collections


def decode_message(message_signals: list[str], part: int) -> str:
    """
    Decodes a message given a list of coded messages.
    Combines the letters at each index in each signal in message_signals, and
    creates a new message using the most or least common character at each index.
    :param message_signals: The message signals.
    :param part: Part 1 for most common, part 2 for least common.
    :return: The decoded message.
    """
    final_message = ''
    for i in range(len(message_signals[0])):
        chars_at_index = ''
        for coded_message in message_signals:
            chars_at_index += coded_message[i]
        if part == 1:
            final_message += get_most_common_letter(chars_at_index)
        elif part == 2:
            final_message += get_least_common_letter(chars_at_index)
        else:
            raise ValueError(f'Part must be 1 or 2, not {part}.')
    return final_message


def get_most_common_letter(word: str) -> str:
    """
    Finds the most common letter in a word.
    :param word: A word.
    :return: The most common character in the word.
    """
    return collections.Counter(word).most_common(1)[0][0]


def get_least_common_letter(word: str) -> str:
    """
    Finds the least common letter in a word.
    :param word: A word.
    :return: The least common letter in the word.
    """
    return list(collections.Counter(word).most_common())[-1][0]

def main():
    with open("data/adventofcode.com_2016_day_6_input.txt", "r") as f:
        message = f.read().splitlines()
    print(f'Part 1: {decode_message(message, 1)}')
    print(f'Part 2: {decode_message(message, 2)}')

if __name__ == '__main__':
    main()

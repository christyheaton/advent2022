from string import ascii_lowercase


def parse(input: str) -> tuple:
    """

    :param input:
    :return:
    """
    encrypted_name = input[:input.rfind("-")]
    sector = input[-10:-7]
    checksum = input[input.rfind("[")+1:-1]
    return encrypted_name, int(sector), checksum


def get_letter_counts(cypher_text: str) -> dict:
    """

    :param cypher_text:
    :return:
    """
    letters = {}
    for char in cypher_text:
        if letters.get(char):
            letters[char] += 1
        else:
            letters[char] = 1
    return letters


def calc_checksum(letter_counts: dict) -> str:
    """
    Calculates a checksum
    :param letter_counts:
    :return: the checksum
    """
    ordered = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    checksum = ""
    for i in range(5):
        checksum += ordered[i][0]
    return checksum


def shift(message, offset):
    """
    A shift cypher algorithm
    :param message: an encrypted room name
    :param offset: the number of characters to shift
    :return: a deciphered room name
    """

    trans = str.maketrans(ascii_lowercase,
                          ascii_lowercase[offset:] + ascii_lowercase[:offset])
    return message.lower().translate(trans)


if __name__ == "__main__":
    f = open("data/adventofcode.com_2016_day_4_input.txt", "r")
    data = f.read().splitlines()

    # part 1
    sector_total = 0
    real_rooms = []
    for d in data:
        name, sector_id, csum = parse(d)
        sorted_d = ''.join(sorted(name)).replace("-", "")
        my_letter_counts = get_letter_counts(sorted_d)
        if csum == calc_checksum(my_letter_counts):
            sector_total += sector_id
            real_rooms.append(f"{name}-{sector_id}")
    print(f"Part 1 solution: {sector_total}")

    # part 2
    decrypted_rooms = [shift(real_room, int(real_room[-3:])%26) for real_room in real_rooms]
    north_pole_room = [room for room in decrypted_rooms if "northpole" in room][0]
    print(f"Part 2 solution: {north_pole_room[-3:]}")

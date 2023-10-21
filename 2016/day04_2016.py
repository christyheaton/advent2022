from string import ascii_lowercase


def parse(room_name: str) -> tuple[str, int, str]:
    """
    Parse a code into encrypted name, sector, and checksum
    :param room_name: The code to parse
    :return: encrypted name, sector, and checksum as a tuple
    """
    encrypted_name = room_name[:room_name.rfind("-")]
    sector = room_name[-10:-7]
    checksum = room_name[room_name.rfind("[") + 1:-1]
    return encrypted_name, int(sector), checksum


def get_letter_counts(encrypted_name: str) -> dict:
    """
    Counts the number of times a letter appears in the encrypted_name
    in order to calculate the checksum later
    :param encrypted_name:
    :return: a dictionary where the key is a letter in the encrypted_name and the value
    is the number of times it appears in the encrypted_name
    """
    letter_counts = {}
    for char in encrypted_name:
        if letter_counts.get(char):
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts


def calc_checksum(letter_counts: dict) -> str:
    """
    Calculates the checksum, i.e. the five most common letters in the encrypted name,
    in order, with ties broken by alphabetization.
    :param letter_counts: a dictionary of letters and the number times they appear in a string
    :return: the checksum
    """
    ordered = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    checksum = ""
    for i in range(5):
        checksum += ordered[i][0]
    return checksum


def shift(message: str, offset: int) -> str:
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

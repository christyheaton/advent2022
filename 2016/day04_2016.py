

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

    :param letter_counts:
    :return:
    """
    ordered = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    checksum = ""
    for i in range(5):
        checksum += ordered[i][0]
    return checksum



if __name__ == "__main__":
    # data = ["aaaaa-bbb-z-y-x-123[abxyz]",
    #         "a-b-c-d-e-f-g-h-987[abcde]",
    #         "not-a-real-room-404[oarel]",
    #         "totally-real-room-200[decoy]"]
    f = open("data/adventofcode.com_2016_day_4_input.txt", "r")
    data = f.read().splitlines()

    sector_total = 0
    for d in data:
        name, sector_id, csum = parse(d)
        sorted_d = ''.join(sorted(name)).replace("-", "")
        letter_counts = get_letter_counts(sorted_d)
        if csum == calc_checksum(letter_counts):
            sector_total += sector_id
    print(f"Part 1 solution: {sector_total}")

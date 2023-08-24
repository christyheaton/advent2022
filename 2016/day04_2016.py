
def parse(input):
    encrypted_name = input[:input.rfind("-")]
    print(f"encrypted name: {encrypted_name}")
    checksum = input[input.rfind("[")+1:-1]
    print(f"Checksum: {checksum}")

if __name__ == "__main__":
    data = ["aaaaa-bbb-z-y-x-123[abxyz]",
            "a-b-c-d-e-f-g-h-987[abcde]",
            "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"]

    for d in data:
        parse(d)

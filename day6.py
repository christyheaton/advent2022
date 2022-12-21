from aocd import get_data


if __name__ == '__main__':
    data = get_data(day=6, year=2022)
    packet_length = 4  # use 4 for part 1, 14 for part 2
    index = 0
    while index < len(data):
        sub_set = set(data[index:index + packet_length])
        if len(sub_set) == packet_length:
            print(f'First unique set of {packet_length} characters is {"".join(sub_set)}')
            print(f'Found ending at index {index + packet_length}')
            break
        index += 1

from aocd import get_data


def get_start_of_packet_marker(input_data: str, packet_length: int) -> int:
    index = 0
    while index < len(input_data):
        sub_set = set(input_data[index:index + packet_length])
        if len(sub_set) == packet_length:
            return index + packet_length
        index += 1


if __name__ == '__main__':
    data = get_data(day=6, year=2022)
    print(f'Part 1: {get_start_of_packet_marker(data, 4)}')
    print(f'Part 2: {get_start_of_packet_marker(data, 14)}')

from aocd import get_data


if __name__ == '__main__':
    data = get_data(day=6, year=2022)
    unique_count = 4  # use 4 for part 1, 14 for part 2
    index = 0
    while index < len(data):
        sub = data[index:index + unique_count]
        sub_set = set(sub)
        if len(sub_set) == unique_count:
            print(f'First unique set of {unique_count} characters is {"".join(sub_set)}')
            print(f'Found ending at index {index + unique_count}')
            break
        index += 1

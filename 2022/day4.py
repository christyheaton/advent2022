from aocd import get_data


def duplicate_work_id(input_data):
    contains = 0
    overlap = 0
    for i in input_data:
        r1 = i.split(',')[0].split('-')
        r2 = i.split(',')[1].split('-')
        s1 = set(range(int(r1[0]), int(r1[1])+1))
        s2 = set(range(int(r2[0]), int(r2[1])+1))
        if s1.issubset(s2) or s2.issubset(s1):
            contains += 1
        if bool(set(s1) & set(s2)):
            overlap += 1
    return contains, overlap


if __name__ == '__main__':
    data = get_data(day=4, year=2022).splitlines()
    count_contains, count_overlap = duplicate_work_id(data)
    print(f'Part 1: Count of assignments that contain another: {count_contains}')
    print(f'Part 2: Count of assignments that overlap each other: {count_overlap}')

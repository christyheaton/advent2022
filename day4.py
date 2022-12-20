from aocd import get_data


if __name__ == '__main__':
    data = get_data(day=4, year=2022).splitlines()
    count = 0
    for i in data:
        r1 = i.split(',')[0].split('-')
        r2 = i.split(',')[1].split('-')
        s1 = set(range(int(r1[0]), int(r1[1])+1))
        s2 = set(range(int(r2[0]), int(r2[1])+1))
        if s1.issubset(s2) or s2.issubset(s1):
            count += 1
    print(count)

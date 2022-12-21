from aocd import get_data


if __name__ == '__main__':
    data = get_data(day=5, year=2022).splitlines()
    stacks = {key: [] for key in range(1, 10)}
    container_info = data[0:8][::-1]
    container_info_split = []
    for cont in container_info:
        cont = cont.replace('    ', ' ')
        cont = cont.split(' ')
        container_info_split.append(cont)
    count = 0
    while count < len(container_info_split):
        for k in stacks.keys():
            for d in container_info_split:
                stacks[k].append(d[count])
            count += 1
    print(stacks)
    for i in data[0:8]:
        print(i)

    instructions = data[10:]
    print(instructions)



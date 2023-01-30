from aocd import get_data


def not_int(integer):
    b = f'{integer:016b}'
    inv_b = ''.join(['1' if i == '0' else '0' for i in b])
    return int(inv_b, 2)


def circuit_switch(instructions):
    res = {}
    for i in instructions:
        i_sp = i.split()
        if i_sp[0].isdigit():
            res[i_sp[-1]] = int(i_sp[0])
        elif 'AND' in i_sp:
            res[i_sp[-1]] = int(res[i_sp[0]]) & int(res[i_sp[2]])
        elif 'OR' in i_sp:
            res[i_sp[-1]] = int(res[i_sp[0]]) | int(res[i_sp[2]])
        elif 'LSHIFT' in i_sp:
            res[i_sp[-1]] = int(res[i_sp[0]]) << int(i_sp[2])
        elif 'RSHIFT' in i_sp:
            res[i_sp[-1]] = int(res[i_sp[0]]) >> int(i_sp[2])
        elif 'NOT' in i_sp:
            res[i_sp[-1]] = not_int(int(res[i_sp[1]]))
    return res


def main() -> None:
    # data = get_data(day=7, year=2015).splitlines()
    data = ['123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i']
    print(data)
    results = circuit_switch(data)
    print(results)


if __name__ == '__main__':
    main()

"""advent of code 2015 day 5 https://adventofcode.com/2016/day/5"""

import hashlib


def check_md5_hash(input_data, zeros):
    """find md5 hash that starts with a configurable number of zeros"""
    password = ''
    count = 1
    while True:
        test = f'{input_data}{count}'
        result = hashlib.md5(test.encode())
        if result.hexdigest().startswith(zeros*'0'):
            password = f'{password}{result.hexdigest()[5]}'
            print(f'test: {test}')
            print(f'result: {result.hexdigest()}')
            print(f'password: {password}')
        if len(password) == 8:
            return password
        count += 1


def main() -> None:
    """solutions for parts 1 and 2"""
    input_data = 'cxdnnyjw'
    res = check_md5_hash(input_data, 5)
    print(res)


if __name__ == '__main__':
    main()

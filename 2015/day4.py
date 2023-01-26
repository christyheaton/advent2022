from aocd import get_data
import hashlib


def check_md5_hash(input_data, zeros):
    count = 1
    while True:
        test = f'{input_data}{count}'
        result = hashlib.md5(test.encode())
        if result.hexdigest().startswith(zeros*'0'):
            return count
        else:
            count += 1


def main() -> None:
    input_data: str = get_data(day=4, year=2015)
    print(f'Part 1: {check_md5_hash(input_data, 5)}')
    print(f'Part 2: {check_md5_hash(input_data, 6)}')


if __name__ == '__main__':
    main()

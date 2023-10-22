"""advent of code 2015 day 5 https://adventofcode.com/2016/day/5"""

import hashlib


class PasswordFinder:
    def __init__(self, door_id: str):
        """
        Finds the password for a given door id.
        :param door_id: The door id.
        """
        self.door_id = door_id

    def get_md5_hash(self, count: int):
        """
        Get the md5 hash of the door id with count appended.
        :param count: the increment to append to the door id.
        :return: the md5 hash.
        """
        test = f'{self.door_id}{count}'
        return hashlib.md5(test.encode())

    @staticmethod
    def check_interesting(hash_value) -> bool:
        """
        Check if the hash value is interesting, i.e. starts with 5 0s.
        :param hash_value: The hash value
        :return: True if interesting, otherwise False.
        """
        return hash_value.hexdigest().startswith(5 * '0')

    def find_password_pt1(self) -> str:
        """
        Find password using Part 1 logic.
        :return: The password.
        """
        password = ''
        count = 0
        while len(password) < 8:
            hash_result = self.get_md5_hash(count)
            if self.check_interesting(hash_result):
                password += hash_result.hexdigest()[5]
            count += 1
        return password

    def find_password_pt2(self) -> str:
        """
        Find password using Part 2 logic.
        :return: The password.
        """
        password = ''
        placements = {}
        count = 0
        while len(placements) < 8:
            hash_result = self.get_md5_hash(count)
            if self.check_interesting(hash_result):
                hex_result = hash_result.hexdigest()
                if (hex_result[5].isnumeric()
                        and int(hex_result[5]) < 8
                        and not placements.get(hex_result[5])):
                    placements[hex_result[5]] = hex_result[6]
            count += 1
        for item in sorted(placements.items()):
            password += str(item[1])
        return password


def main() -> None:
    """
    Print solutions for parts 1 and 2.
    """
    # input_data = 'abc' # test data
    input_data = 'cxdnnyjw'
    pw_finder = PasswordFinder(input_data)
    print(f'Part 1: {pw_finder.find_password_pt1()}')
    print(f'Part 2: {pw_finder.find_password_pt2()}')


if __name__ == '__main__':
    main()
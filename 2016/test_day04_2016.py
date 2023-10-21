"""tests for day 4"""

from day04_2016 import parse, get_letter_counts, calc_checksum, shift


def test_parse() -> None:
    """
    Test parse parses correctly.
    """
    assert parse('aaaaa-bbb-z-y-x-123[abxyz]') == ('aaaaa-bbb-z-y-x', 123, 'abxyz')


def test_get_letter_counts() -> None:
    """
    Test get_letter_counts returns the correct dict.
    """
    assert get_letter_counts('a-b-c-d-e-f-g-h-987[abcde]') == {'-': 8,
                                                '7': 1,
                                                '8': 1,
                                                '9': 1,
                                                '[': 1,
                                                ']': 1,
                                                'a': 2,
                                                'b': 2,
                                                'c': 2,
                                                'd': 2,
                                                'e': 2,
                                                'f': 1,
                                                'g': 1,
                                                'h': 1}


def test_calc_checksum() -> None:
    """
    Test calc_checksum returns the correct checksum.
    """
    letter_counts = {'a': 5, 'c': 3, 'd': 2, 'x': 8, '[': 1}
    assert calc_checksum(letter_counts) == 'xacd['


def test_shift() -> None:
    """
    Test shift returns the right message.
    """
    assert shift('my_message', 4) == 'qc_qiwweki'

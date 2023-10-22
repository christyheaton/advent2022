"""tests for day 5"""

import pytest
from day05_2016 import PasswordFinder


@pytest.fixture()
def pw_finder() -> PasswordFinder:
    """
    An instance of PasswordFinder to use for testing.
    :return: An instance of PasswordFinder with test input.
    """
    return PasswordFinder('abc')

def test_get_md5_hash(pw_finder: PasswordFinder) -> None:
    """
    Test get_md5_hash returns the correct hash.
    :param pw_finder: The test instance of PasswordFinder.
    :return:
    """
    assert pw_finder.get_md5_hash(15).hexdigest() == '9fd92d6b274f07e0926408eb5903cd58'
    assert pw_finder.get_md5_hash(3231929).hexdigest() == '00000155f8105dff7f56ee10fa9b9abd'


def test_check_interesting(pw_finder: PasswordFinder) -> None:
    """
    Test check_interesting returns the correct bool.
    :param pw_finder: The test instance of PasswordFinder.
    :return:
    """
    hash_val_not_interesting = pw_finder.get_md5_hash(15)
    hash_val_interesting = pw_finder.get_md5_hash(3231929)
    assert not pw_finder.check_interesting(hash_val_not_interesting)
    assert pw_finder.check_interesting(hash_val_interesting)

def test_find_password_pt1(pw_finder: PasswordFinder) -> None:
    """
    Test find_password_pt1 returns the correct password.
    :param pw_finder: The test instance of PasswordFinder.
    :return:
    """
    assert pw_finder.find_password_pt1() == '18f47a30'

def test_find_password_pt2(pw_finder: PasswordFinder) -> None:
    """
    Test find_password_pt2 returns the correct password.
    :param pw_finder: The test instance of PasswordFinder.
    :return:
    """
    assert pw_finder.find_password_pt2() == '05ace8e3'

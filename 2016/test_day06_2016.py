import pytest
from day06_2016 import decode_message, get_least_common_letter, get_most_common_letter

@pytest.fixture()
def test_data() -> list[str]:
    """
    Provided test data.
    :return: Test data.
    """
    return ['eedadn',
            'drvtee',
            'eandsr',
            'raavrd',
            'atevrs',
            'tsrnev',
            'sdttsa',
            'rasrtv',
            'nssdts',
            'ntnada',
            'svetve',
            'tesnvt',
            'vntsnd',
            'vrdear',
            'dvrsen',
            'enarar']


def test_decode_message(test_data: list[str]) -> None:
    """
    Test decode message returns correct result.
    :param test_data: Test data.
    :return:
    """
    assert decode_message(test_data, 1) == 'easter'
    assert decode_message(test_data, 2) == 'advent'


def test_get_most_common_letter(test_data: list[str]) -> None:
    """
    Test get_most_common_letter returns correct result.
    :param test_data: Test data.
    :return:
    """
    assert get_most_common_letter('zappy') == 'p'


def test_get_least_common_letter(test_data: list[str]) -> None:
    """
    Test get_least_common_letter returns correct result.
    :param test_data: Test data.
    :return:
    """
    assert get_least_common_letter('rainy day') == 'd'

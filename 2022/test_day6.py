import pytest
from day6 import get_start_of_packet_marker


@pytest.mark.parametrize('test_input,expected',
                         [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
                          ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
                          ('nppdvjthqldpwncqszvftbrmjlhg', 6),
                          ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
                          ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)])
def test_part1(test_input, expected):
    assert get_start_of_packet_marker(test_input, 4) == expected


@pytest.mark.parametrize('test_input,expected',
                         [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
                          ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
                          ('nppdvjthqldpwncqszvftbrmjlhg', 23),
                          ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
                          ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)])
def test_part2(test_input, expected):
    assert get_start_of_packet_marker(test_input, 14) == expected

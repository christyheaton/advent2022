import pytest
from day7 import get_sum_total_sizes, get_smallest_large_dir, FileSystem


@pytest.fixture
def test_input() -> FileSystem:
    return FileSystem('$ cd /\n'
                      '$ ls\n'
                      'dir a\n'
                      '14848514 b.txt\n'
                      '8504156 c.dat\n'
                      'dir d\n'
                      '$ cd a\n'
                      '$ ls\n'
                      'dir e\n'
                      '29116 f\n'
                      '2557 g\n'
                      '62596 h.lst\n'
                      '$ cd e\n'
                      '$ ls\n'
                      '584 i\n'
                      '$ cd ..\n'
                      '$ cd ..\n'
                      '$ cd d\n'
                      '$ ls\n'
                      '4060174 j\n'
                      '8033020 d.log\n'
                      '5626152 d.ext\n'
                      '7214296 k')


def test_part1(test_input: FileSystem):
    assert get_sum_total_sizes(test_input) == 95437


def test_part2(test_input: FileSystem):
    assert get_smallest_large_dir(test_input) == 24933642

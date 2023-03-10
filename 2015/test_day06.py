"""tests for day 6"""
# pylint: disable=redefined-outer-name
import pytest
import numpy as np
from day06 import create_npgrid_pt1, create_npgrid_pt2, parse_instructions, \
    perform_instructions_pt1, perform_instructions_pt2


@pytest.mark.parametrize('test_input,expected',
                         [('turn on 887,9 through 959,629', ('on', 887, 9, 959, 629)),
                          ('turn on 454,398 through 844,448', ('on', 454, 398, 844, 448)),
                          ('turn off 539,243 through 559,965', ('off', 539, 243, 559, 965)),
                          ('toggle 720,196 through 897,994', ('toggle', 720, 196, 897, 994))])
def test_parse_instructions(test_input, expected):
    """test instructions parsed correctly"""
    assert parse_instructions(test_input) == expected


@pytest.fixture
def test_instructions() -> list:
    """sample instructions"""
    return ['turn on 1,2 through 3,4',
            'turn on 0,0 through 1,3',
            'toggle 4,2 through 5,3',
            'turn on 2,1 through 4,3']


def test_perform_instructions_pt1(test_instructions):
    """test instructions performed correctly for part 1"""
    grid = create_npgrid_pt1(5)
    grid = perform_instructions_pt1(test_instructions, grid)
    assert np.array_equal(grid, np.array([[True, True, True, True, False],
                                          [True, True, True, True, True],
                                          [False, True, True, True, True],
                                          [False, True, True, True, True],
                                          [False, True, True, True, False]]))


def test_perform_instructions_pt2(test_instructions):
    """test instructions performed correctly for part 2"""
    grid = create_npgrid_pt2(5)
    grid = perform_instructions_pt2(test_instructions, grid)
    assert np.array_equal(grid, np.array([[1., 1., 1., 1., 0.],
                                          [1., 1., 2., 2., 1.],
                                          [0., 1., 2., 2., 1.],
                                          [0., 1., 2., 2., 1.],
                                          [0., 1., 3., 3., 0.]]))

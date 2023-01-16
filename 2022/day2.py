import sys
from enum import Enum
from aocd import get_data


class Scores(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    Win = 6
    Tie = 3


def game1(their_play: str, your_play: str) -> int:
    """Takes in two strings, one for their play, one for your play
    Returns an integer of your score"""
    your_score = 0

    if your_play == 'X':
        your_score += Scores.Rock.value
        if their_play == 'A':
            your_score += Scores.Tie.value
        elif their_play == 'C':
            your_score += Scores.Win.value

    elif your_play == 'Y':
        your_score += Scores.Paper.value
        if their_play == 'B':
            your_score += Scores.Tie.value
        elif their_play == 'A':
            your_score += Scores.Win.value

    elif your_play == 'Z':
        your_score += Scores.Scissors.value
        if their_play == 'C':
            your_score += Scores.Tie.value
        elif their_play == 'B':
            your_score += Scores.Win.value

    return your_score


def game2(their_play: str, your_play: str) -> int:
    """Takes in two strings, one for their play, one for your play
    Returns an integer of your score"""
    your_score = 0

    if their_play == 'A':
        if your_play == 'X':
            your_score += Scores.Scissors.value
        elif your_play == 'Y':
            your_score += Scores.Tie.value + Scores.Rock.value
        elif your_play == 'Z':
            your_score += Scores.Win.value + Scores.Paper.value

    elif their_play == 'B':
        if your_play == 'X':
            your_score += Scores.Rock.value
        elif your_play == 'Y':
            your_score += Scores.Tie.value + Scores.Paper.value
        elif your_play == 'Z':
            your_score += Scores.Win.value + Scores.Scissors.value

    elif their_play == 'C':
        if your_play == 'X':
            your_score += Scores.Paper.value
        elif your_play == 'Y':
            your_score += Scores.Tie.value + Scores.Scissors.value
        elif your_play == 'Z':
            your_score += Scores.Win.value + Scores.Rock.value

    return your_score


def play_round(game_round: str, game_part: int) -> int:
    """Takes in a string of a single game round and game part logic
    Returns an integer of your score for the round
    """
    their_play = game_round[0]
    your_play = game_round[2]

    if their_play not in ['A', 'B', 'C'] or your_play not in ['X', 'Y', 'Z']:
        print('An unexpected play was entered.')
        print(f"Their play must be one of 'A', 'B', 'C'. Their play was {their_play}.")
        print(f"Your play must be one of 'X', 'Y', 'Z'. Your play was {your_play}.")
        sys.exit()

    if game_part == 1:
        your_score = game1(their_play, your_play)
    elif game_part == 2:
        your_score = game2(their_play, your_play)
    else:
        print('The game has two ways to play. Please enter 1 or 2.')
        sys.exit()

    return your_score


def game_summary(game_input: list, game_part: int) -> list:
    """Takes in list of a full game and an int of the game part logic
    Returns a list of scores, one for each round"""
    return [play_round(game_round, game_part) for game_round in game_input]


if __name__ == '__main__':
    data = get_data(day=2, year=2022).splitlines()
    print('Your total scores:')
    print(f'   Part 1: {sum(game_summary(data, 1))}')
    print(f'   Part 2: {sum(game_summary(data, 2))}')

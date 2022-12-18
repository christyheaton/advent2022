import sys
from aocd import get_data

# Point designations
ROCK = 1
PAPER = 2
SCISSORS = 3
WIN = 6
DRAW = 3


def game1(their_play, your_play):
    """Takes in two strings, one for their play, one for your play
    Returns an integer of your score"""
    your_score = 0

    if your_play == 'X':
        your_score += ROCK
        if their_play == 'A':
            your_score += DRAW
        elif their_play == 'C':
            your_score += WIN

    elif your_play == 'Y':
        your_score += PAPER
        if their_play == 'B':
            your_score += DRAW
        elif their_play == 'A':
            your_score += WIN

    elif your_play == 'Z':
        your_score += SCISSORS
        if their_play == 'C':
            your_score += DRAW
        elif their_play == 'B':
            your_score += WIN

    return your_score


def game2(their_play, your_play):
    """Takes in two strings, one for their play, one for your play
    Returns an integer of your score"""
    your_score = 0

    if their_play == 'A':
        if your_play == 'X':
            your_score += SCISSORS
        elif your_play == 'Y':
            your_score += DRAW + ROCK
        elif your_play == 'Z':
            your_score += WIN + PAPER

    elif their_play == 'B':
        if your_play == 'X':
            your_score += ROCK
        elif your_play == 'Y':
            your_score += DRAW + PAPER
        elif your_play == 'Z':
            your_score += WIN + SCISSORS

    elif their_play == 'C':
        if your_play == 'X':
            your_score += PAPER
        elif your_play == 'Y':
            your_score += DRAW + SCISSORS
        elif your_play == 'Z':
            your_score += WIN + ROCK

    return your_score


def play_round(game_round, game_part):
    """Takes in a string of a single game round and game part logic
    Returns an integer of your score for the round
    """
    their_play = game_round[0]
    your_play = game_round[2]

    if their_play not in ['A', 'B', 'C'] or your_play not in ['X', 'Y', 'Z']:
        print('An unexpected play was entered.')
        print(f"Their play must be one of 'A', 'B', 'C'. Their play was {their_play}.")
        print(f"Your play must be one of 'X', 'Y', 'Z'. Their play was {your_play}.")
        sys.exit()

    if game_part == 1:
        your_score = game1(their_play, your_play)
    elif game_part == 2:
        your_score = game2(their_play, your_play)
    else:
        print('The game has two ways to play. Please enter 1 or 2.')
        sys.exit()

    return your_score


def game_summary(game_input, game_part):
    """Takes in list of a full game and an int of the game part logic
    Returns a list of scores, one for each round"""
    return [play_round(game_round, game_part) for game_round in game_input]


if __name__ == '__main__':
    data = get_data(day=2, year=2022).splitlines()
    print('Your total scores:')
    print(f'   Part 1: {sum(game_summary(data, 1))}')
    print(f'   Part 2: {sum(game_summary(data, 2))}')

import sys
from aocd import get_data


def get_values():
    rock = 1
    paper = 2
    scissors = 3
    win = 6
    draw = 3

    return rock, paper, scissors, win, draw


def game1(their_play, your_play):
    """Takes in two strings, one for their play, one for your play
    Returns an integer of your score"""
    r, p, s, w, d = get_values()
    your_score = 0

    if your_play == 'X':
        your_score += r
        if their_play == 'A':
            your_score += d
        elif their_play == 'C':
            your_score += w

    elif your_play == 'Y':
        your_score += p
        if their_play == 'B':
            your_score += d
        elif their_play == 'A':
            your_score += w

    elif your_play == 'Z':
        your_score += s
        if their_play == 'C':
            your_score += d
        elif their_play == 'B':
            your_score += w

    else:
        print(f'{their_play} is not a valid entry. Exiting...')
        exit()

    return your_score


def game2(their_play, your_play):
    """Takes in two strings, one for their play, one for your play
    Returns an integer of your score"""
    r, p, s, w, d = get_values()
    your_score = 0

    if their_play == 'A':
        if your_play == 'X':
            your_score += s
        elif your_play == 'Y':
            your_score += d + r
        elif your_play == 'Z':
            your_score += w + p

    elif their_play == 'B':
        if your_play == 'X':
            your_score += r
        elif your_play == 'Y':
            your_score += d + p
        elif your_play == 'Z':
            your_score += w + s

    elif their_play == 'C':
        if your_play == 'X':
            your_score += p
        elif your_play == 'Y':
            your_score += d + s
        elif your_play == 'Z':
            your_score += w + r

    else:
        print(f'{their_play} is not a valid entry. Exiting...')
        exit()

    return your_score


def play_round(game_round, game_part):
    """Takes in a string of a single game round and game part logic
    Returns an integer of your score for the round
    """
    their_play = game_round[0]
    your_play = game_round[2]

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

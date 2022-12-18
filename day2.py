import sys
from aocd import get_data


def game_logic(game_round, game_part):
    """Takes in a string of a single game round and game part logic
    Returns an integer of your score for the round

    Part 1:
    Your game logic is:
    X: rock
    Y: paper
    X: scissors

    Part 2:
    Your game logic is:
    X: you lose
    Y: draw
    Z: you win
    """
    rock = 1
    paper = 2
    scissors = 3

    win = 6
    draw = 3

    their_play = game_round[0]
    your_play = game_round[2]

    your_score = 0

    if game_part == 1:
        if your_play == 'X':
            your_score += rock
            if their_play == 'A':
                your_score += draw
            elif their_play == 'C':
                your_score += win

        elif your_play == 'Y':
            your_score += paper
            if their_play == 'B':
                your_score += draw
            elif their_play == 'A':
                your_score += win

        elif your_play == 'Z':
            your_score += scissors
            if their_play == 'C':
                your_score += draw
            elif their_play == 'B':
                your_score += win

    elif game_part == 2:
        if their_play == 'A':
            if your_play == 'X':
                your_score += scissors
            elif your_play == 'Y':
                your_score += draw
                your_score += rock
            elif your_play == 'Z':
                your_score += win
                your_score += paper

        elif their_play == 'B':
            if your_play == 'X':
                your_score += rock
            elif your_play == 'Y':
                your_score += draw
                your_score += paper
            elif your_play == 'Z':
                your_score += win
                your_score += scissors

        elif their_play == 'C':
            if your_play == 'X':
                your_score += paper
            elif your_play == 'Y':
                your_score += draw
                your_score += scissors
            elif your_play == 'Z':
                your_score += win
                your_score += rock

    else:
        print('The game has two ways to play. Please enter 1 or 2.')
        sys.exit()

    return your_score


def game(game_input, game_part):
    """Takes in list of a full game and an int of the game part logic
    Returns a list of scores, one for each round"""
    your_scores = []
    for game_round in game_input:
        your_scores.append(game_logic(game_round, game_part))
    return your_scores


if __name__ == '__main__':
    print('Getting input data...')
    data = get_data(day=2, year=2022).splitlines()
    print(f'Your total score based on part 1 logic is ***{sum(game(data, 1))}***!')
    print(f'Your total score based on part 2 logic is ***{sum(game(data, 2))}***!')

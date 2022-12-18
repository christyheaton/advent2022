import sys


def get_input_data(file):
    """Takes in a file, returns its contents as a list"""
    try:
        with open(file) as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print('File not found.')
        sys.exit()
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        sys.exit()


def game_logic(game_round):
    rock = 1  # A and X
    paper = 2  # B and Y
    scissors = 3  # C and Z

    win = 6
    draw = 3

    their_play = game_round[0]
    your_play = game_round[2]

    your_score = 0

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

    else:
        print(f'{your_play} is not a valid move')
        sys.exit()

    return your_score


def game(game_input):
    your_scores = []
    for game_round in game_input:
        your_scores.append(game_logic(game_round))
    return your_scores


if __name__ == '__main__':
    print('Getting input data...')
    data = get_input_data('data/day2_input.txt')
    print(f'Your total score based on part 1 logic is ***{sum(game(data))}***!')

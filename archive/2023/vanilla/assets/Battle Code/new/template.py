import random


def play(your_moves, opponent_moves):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    '''
    your_moves: List[int]
    contains the list of your previous moves.

    opponent_moves: List[int]
    contains the list of opponent's previous moves.

    Return either 0, 1, or 2
    indicating ROCK, PAPER or SCISSORS respectively.
    '''
    return random.choice((ROCK, PAPER, SCISSORS))

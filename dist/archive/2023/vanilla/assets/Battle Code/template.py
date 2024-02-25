from battlecode import BattleCodeTeam
import random

ROCK = 0
PAPER = 1
SCISSORS = 2


class AI(BattleCodeTeam):
    def __init__(self) -> None:
        super().__init__()
        self.team_name = "Your Awesome Team Name Here"
        self.round = 0
        self.opponent_move = None
        self.stocks = {
            ROCK: 10,
            PAPER: 10,
            SCISSORS: 10
        }

    def round_over(self, opponent_move: int, result: str) -> None:
        '''
        This method is called automatically when the round ends.
        You can add logic to update your internal game state here.

        `opponent_move` is one of 0, 1, or 2 indicating if your
        opponent team played a ROCK, PAPER or SCISSORS respectively.

        `result` is one of "WIN", "LOSE", "DRAW" indicating if you
        won or lost or tied the previous round.
        '''
        self.round += 1

    def play(self) -> int:
        '''
        This method is called once each round (total of 30 times per match)
        where you return the move you'd like to make.

        Return value MUST be one of 0, 1, or 2 indicating if you'd
        like to play ROCK, PAPER, or SCISSORS respectively.

        Remember, you can play each type of move only for a limited
        number of times during one match. If the method returns an invalid
        value, your opponent team would win all the remaining rounds.
        '''

        # -------- replace this code with your logic --------
        move = ROCK
        self.stocks[move] -= 1
        # return move
        return random.choice((ROCK, PAPER, SCISSORS))

        # ---------------------------------------------------

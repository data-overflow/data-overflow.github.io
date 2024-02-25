ROCK = 0
PAPER = 1
SCISSORS = 2


class BattleCodeTeam:
    def __init__(self) -> None:
        self.team_name = "A"
        self.round = 0
        self.opponent_move = None
        self.stocks = {
            ROCK: 10,
            PAPER: 10,
            SCISSORS: 10
        }

    def round_over(self, opponent_move: int, result: str) -> None:
        self.round += 1

    def play(self) -> int:
        return 0

from timeit import default_timer as timer
from template import play

ROCK = 0
PAPER = 1
SCISSORS = 2
A_WIN = 1
B_WIN = 2
DRAW = 0
NUM_ROUNDS = 30


class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None) -> None:
        self.value: int = value
        self.next: Node = next


class BattleCodeMatch:
    def __init__(self) -> None:
        self.rounds = []
        rock = Node(ROCK)
        paper = Node(PAPER)
        scissors = Node(SCISSORS)
        rock.next = paper
        paper.next = scissors
        scissors.next = rock
        self.RPS = [rock, paper, scissors]
        self.a_wins = 0
        self.b_wins = 0
        self.a_time = 0
        self.b_time = 0

    def add_round(self, moveA: int, moveB: int) -> int:
        if moveA == moveB:  # match is draw
            self.rounds.append((moveA, moveB, DRAW))
            return DRAW
        if self.RPS[moveA].next.value == moveB:
            self.rounds.append((moveA, moveB, B_WIN))
            self.b_wins += 1
            return B_WIN
        else:
            self.rounds.append((moveA, moveB, A_WIN))
            self.a_wins += 1
            return A_WIN

    def compete(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        for _ in range(NUM_ROUNDS):
            time1 = timer()
            moveA = teamA([a for a, b, c in self.rounds],
                          [b for a, b, c in self.rounds]
                          )
            time2 = timer()
            moveB = teamB([b for a, b, c in self.rounds],
                          [a for a, b, c in self.rounds])
            time3 = timer()
            self.a_time += (time2 - time1)
            self.b_time += (time3 - time2)
            result = self.add_round(moveA, moveB)
            # if result == A_WIN:
            #     teamA.round_over(moveB, 'WIN')
            #     teamB.round_over(moveA, 'LOSE')
            # elif result == B_WIN:
            #     teamA.round_over(moveB, 'LOSE')
            #     teamB.round_over(moveA, 'WIN')
            # else:
            #     teamA.round_over(moveB, 'DRAW')
            #     teamB.round_over(moveA, 'DRAW')
        return self

    def statistics(self) -> dict:
        teamA = "Team Red"  # self.teamA.team_name
        teamB = "Team Blue"  # self.teamB.team_name
        if teamA == teamB:
            teamB += '2'
        moveref = ['Rock', 'Paper', 'Scissor']
        winref = ['Draw', 'Red Win', 'Blue Win']
        return {
            'Teams': [teamA, teamB],
            'Rounds': [(moveref[a], moveref[b], winref[r]) for a, b, r in self.rounds],
            'Wins': [self.a_wins, self.b_wins],
            'Execution Times': [self.a_time, self.b_time]
        }


result = BattleCodeMatch().compete(play, play)
print(result.statistics())

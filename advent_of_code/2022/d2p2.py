ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

ROCK_BONUS = 1
PAPER_BONUS = 2
SCISSORS_BONUS = 3

WIN_BONUS = 6
DRAW_BONUS = 3
LOSS_BONUS = 0

with open("advent_of_code2022/d2p1input.txt") as file:
    line = file.readline()
    score = 0
    while line != '':
        opp, me = line[0], line[2]

        if opp == ROCK and me == LOSE:
            score += SCISSORS_BONUS + LOSS_BONUS
        elif opp == ROCK and me == DRAW:
            score += ROCK_BONUS + DRAW_BONUS
        elif opp == ROCK and me == WIN:
            score += PAPER_BONUS + WIN_BONUS
        elif opp == PAPER and me == LOSE:
            score += ROCK_BONUS + LOSS_BONUS
        elif opp == PAPER and me == DRAW:
            score += PAPER_BONUS + DRAW_BONUS
        elif opp == PAPER and me == WIN:
            score += SCISSORS_BONUS + WIN_BONUS
        elif opp == SCISSORS and me == LOSE:
            score += PAPER_BONUS + LOSS_BONUS
        elif opp == SCISSORS and me == DRAW:
            score += SCISSORS_BONUS + DRAW_BONUS
        elif opp == SCISSORS and me == WIN:
            score += ROCK_BONUS + WIN_BONUS
        
        line = file.readline()
        
    print(score)
ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSORS = ['C', 'Z']

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

        if opp in ROCK and me in PAPER:
            score += PAPER_BONUS + WIN_BONUS
        elif opp in ROCK and me in SCISSORS:
            score += SCISSORS_BONUS + LOSS_BONUS
        elif opp in PAPER and me in ROCK:
            score += ROCK_BONUS + LOSS_BONUS
        elif opp in PAPER and me in SCISSORS:
            score += SCISSORS_BONUS + WIN_BONUS
        elif opp in SCISSORS and me in ROCK:
            score += ROCK_BONUS + WIN_BONUS
        elif opp in SCISSORS and me in PAPER:
            score += PAPER_BONUS + LOSS_BONUS
        elif opp in ROCK and me in ROCK:
            score += ROCK_BONUS + DRAW_BONUS
        elif opp in PAPER and me in PAPER:
            score += PAPER_BONUS + DRAW_BONUS
        elif opp in SCISSORS and me in SCISSORS:
            score += SCISSORS_BONUS + DRAW_BONUS

        
        line = file.readline()
        
    print(score)
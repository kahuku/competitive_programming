cases = int(input())
for i in range(cases):
    _, all_problems = input(), input()
    solved_problems = set()
    balloons = len(all_problems)
    for problem in all_problems:
        if problem not in solved_problems:
            solved_problems.add(problem)
            balloons += 1
    print(balloons)
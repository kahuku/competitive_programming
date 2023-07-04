def maximumIndex(steps, badIndex):
    furthest = 0
    starting_steps = steps
    for i in range(1, steps + 1): furthest += i
    index = furthest
    while True:
        while index > 0 and steps > 0:
            if index - steps != badIndex:
                index -= steps
            steps -= 1
        if index <= 0: return furthest
        else:
            steps = starting_steps
            furthest -= 1
            index = furthest
            if index == badIndex:
                index = furthest - 1
                furthest -= 1

if __name__ == "__main__":
    maximumIndex(5, 2)

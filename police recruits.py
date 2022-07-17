_ = input()
events = [int(i) for i in input().split()]

unsolved = 0
cops = 0
for event in events:
    if event > 0:
        cops += event
    else:
        if cops > 0:
            cops -= 1
        else:
            unsolved += 1

print(unsolved)

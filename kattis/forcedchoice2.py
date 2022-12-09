num_cards, special, steps = [int(i) for i in input().split()]
for i in range(steps):
    selection = [int(i) for i in input().split()]
    selection.pop(0)
    if special in selection:
        print("KEEP")
    else:
        print("REMOVE")
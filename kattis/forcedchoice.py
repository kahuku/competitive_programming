#forcedchoice
inp = input().split()
num_cards = int(inp[0])
prediction = int(inp[1])
num_steps = int(inp[2])

for i in range(num_steps):
    cards = [int(j) for j in input().split()]
    num_selected = cards.pop(0)
    if prediction in cards:
        print("KEEP")
    else:
        print("REMOVE")

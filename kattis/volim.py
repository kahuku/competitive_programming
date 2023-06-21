start_player = int(input())
n = int(input())
time = 0
for _ in range(n):
    t, answer = input().split()
    time += int(t)
    if time >= 210:
        break
    if answer == "T":
        start_player = (start_player % 8) + 1
print(start_player)
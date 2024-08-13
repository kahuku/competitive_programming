for _ in range(int(input())):
    n = int(input())
    seats = [0] * (n + 2)
    entries = list(map(int, input().split()))
    seats[entries[0]] = 1
    valid = True
    for entry in entries[1:]:
        if seats[entry - 1] + seats[entry + 1] == 0:
            valid = False
            break
        seats[entry] = 1
    print("YES" if valid else "NO")
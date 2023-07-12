n, k = map(int, input().split())
d, s = map(int, input().split())
total_difficulty = d * n
solved_difficulty = k * s
remaining_difficulty = (total_difficulty - solved_difficulty) / (n - k)
print(remaining_difficulty if remaining_difficulty >= 0 and remaining_difficulty <= 100 else "impossible")
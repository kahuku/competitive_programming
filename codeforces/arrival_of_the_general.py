n = int(input())
s = [int(i) for i in input().split()]
max_index, min_rindex = s.index(max(s)), s[::-1].index(min(s))
moves = max_index + min_rindex
print(moves) if moves < n else print(moves - 1)
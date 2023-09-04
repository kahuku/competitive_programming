n, a = map(int, input().split())
print("Jebb" if sum([int(input()) for _ in range(n)]) <= a else "Neibb")
input(); x = list(map(int, input().split()))
print("yes" if not sum(x) % 3 else "no")
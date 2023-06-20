r, f = map(int, input().split())
print("up" if not round(f / r) % 2 else "down")
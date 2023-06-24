input(); trees = sorted(map(int, input().split()), reverse=True)
print(max(trees[i] + i + 2 for i in range(len(trees))))
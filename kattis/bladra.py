nProbs, n = map(int, input().split())
probs = [0] * nProbs
for _ in range(n):
    probs[int(input().split()[1]) - 1] += 1
print(min(probs))
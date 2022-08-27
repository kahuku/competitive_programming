n, k = [int(i) for i in input().split()]
scores = [int(i) for i in input().split()]
min_score = scores[k - 1]
advanced = 0
for score in scores:
    if score >= min_score and score > 0:
        advanced += 1
print(advanced)
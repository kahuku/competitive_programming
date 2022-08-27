"""
def calc_score(scores_list):
    score = 0.0
    for i in range(scores_list):
        score += (.2 * (scores_list[i]) * (.8 ** i))
    score
"""

num_scores = int(input())
initial_score = 0.0
all_scores = []
for i in range(num_scores):
    all_scores.append(int(input()))
    initial_score += (.2 * (all_scores[i]) * (.8 ** i))
print(initial_score)
#print()

avgs = []
for i in range(num_scores):
    avg = 0
    used = 0
    for j in range(num_scores):
        if (i != j):
            avg += (.2 * (all_scores[j]) * (.8 ** used))
            used += 1
    #print(avg)
    avgs.append(avg)

s = 0.0
for avg in avgs:
    s += avg
#print()
print(s / len(avgs))

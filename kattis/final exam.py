num_q = int(input())
score = 0
prev_ans = 'x'
for i in range(num_q):
    curr_ans = input()
    if (curr_ans == prev_ans):
        score += 1
    prev_ans = curr_ans
print(score)

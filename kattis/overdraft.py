num_transactions = int(input())
transactions = [int(input()) for _ in range(num_transactions)]
overdraft = 0
total = 0
for i in range(len(transactions)):
    total += transactions[i]
    overdraft = min(total, overdraft)
print(-1 * overdraft)
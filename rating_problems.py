judges, voted = [int(i) for i in input().split()]
votes, not_voted = [], judges - voted
[votes.append(int(input())) for i in range(voted)]
print((sum(votes) + -3 * not_voted) / judges, (sum(votes) + 3 * not_voted) / judges)
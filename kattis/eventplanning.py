n_participants, budget, n_hotels, n_weeks = list(map(int, input().split()))

hotel_costs = []
capacity = []
for i in range(n_hotels):
    hotel_costs.append(int(input()))
    capacity.append(list(map(int, input().split())))

cheapest = float('inf')
for i in range(n_hotels):
    for j in range(len(capacity[i])):
        if capacity[i][j] >= n_participants:
            rate = hotel_costs[i] * n_participants
            cheapest = min(rate, cheapest)
            
print(cheapest if cheapest <= budget else "stay home")
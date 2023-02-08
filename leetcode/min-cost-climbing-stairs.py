class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            dp.append(cost[i] + min(dp[i - 2], dp[i - 1]))
        print(dp)
        return min(dp[-1], dp[-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            new = min(first, second) + cost[i]
            first = second
            second = new
        return min(first, second)
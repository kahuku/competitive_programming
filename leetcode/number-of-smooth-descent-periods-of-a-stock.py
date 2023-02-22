class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        streak = 0
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                streak += 1
            else:
                streak = 0
            count += 1 + streak
        return count
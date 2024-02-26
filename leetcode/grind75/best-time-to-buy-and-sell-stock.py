# Array, Dynamic Programming

class Solution:
    # O(n) time | O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        profit = float('-inf')
        for num in prices[1:]:
            mi = min(mi, num)
            profit = max(profit, num - mi)
        return profit if profit != float('-inf') else 0
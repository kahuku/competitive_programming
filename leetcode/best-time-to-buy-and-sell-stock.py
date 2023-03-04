class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        m = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > m:
                m = profit
            elif prices[r] <= prices[l]:
                l = r
        return m

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, m = prices[0], 0
        for i in range(len(prices)):
            r = prices[i]
            if r - l > m:
                m = r - l
            if l > r:
                l = r
        return m
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 0
        for i in range(len(prices)):
            r = i
            potential_profit = prices[r] - prices[l]
            profit = max(profit, potential_profit)
            if potential_profit < 0:
                l = r
        return profit
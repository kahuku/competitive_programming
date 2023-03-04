class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, s = prices[0], 0
        for i in range(1, len(prices)):
            r = prices[i]
            if r - l > 0:
                s += r - l
            l = r
        return s

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0
        return profit
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1]])
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(b-a, 0) for a, b in zip(prices, prices[1:])])

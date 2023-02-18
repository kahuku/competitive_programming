class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, s = prices[0], 0
        for i in range(1, len(prices)):
            r = prices[i]
            if r - l > 0:
                s += r - l
            l = r
        return s
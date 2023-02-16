from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(maxsize=50000)
        def cutCost(l, r):
            cost = float('inf')
            for cut in cuts:
                if l < cut < r:
                    cost = min(cost, cutCost(l, cut) + cutCost(cut, r) + r - l)
            return cost if cost != float('inf') else 0
        return cutCost(0, n)
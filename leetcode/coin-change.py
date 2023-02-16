from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=amount)
        def getCoins(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            return min([1 + getCoins(amount - coin) for coin in coins])
        numCoins = getCoins(amount)
        return numCoins if numCoins != float('inf') else -1
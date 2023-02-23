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
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0]
        for i in range(1, amount + 1):
            dp.append(float('inf'))
            for coin in coins:
                if i - coin < 0:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
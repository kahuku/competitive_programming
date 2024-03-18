class Solution:
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @cache
        def search(rolls, targetLeft):
            if rolls == 0 and targetLeft == 0:
                return 1
            elif rolls == 0 or targetLeft < 0:
                return 0
            return sum([search(rolls - 1, targetLeft - i) for i in range(1, k + 1)])

        ways = search(n, target)
        return ways % (10 ** 9 + 7)
    
class Solution:
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        cache = {}
        
        def search(rolls, targetLeft):
            if (rolls, targetLeft) in cache:
                return cache[(rolls, targetLeft)]
            if rolls == 0 and targetLeft == 0:
                return 1
            elif rolls == 0 or targetLeft < 0:
                return 0
            cache[(rolls, targetLeft)] = sum([search(rolls - 1, targetLeft - i) for i in range(1, k + 1)])
            return cache[(rolls, targetLeft)]

        ways = search(n, target)
        return ways % (10 ** 9 + 7)
    
class Solution(object):
    def numRollsToTarget(self, n, k, target):
        dp = []
        constant = 10**9 + 7
        for i in range(n + 1):
            dp.append([0] * (target + 1))
        for j in range(target + 1):
            if j < k:
                dp[0][j] = 1
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                res = 0
                for z in range(1, k + 1):
                    if j - z < 0:
                        continue
                    res += dp[i - 1][j - z]
                dp[i][j] = res % constant
        return dp[n - 1][target - 1]
    
print(Solution().numRollsToTarget(3, 6, 7))
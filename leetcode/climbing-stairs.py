class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []
        for i in range(0, n + 1):
            if i <= 3:
                steps.append(i)
            else:
                steps.append(steps[i - 1] + steps[i - 2])
        return steps[n]

# too slow
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n - 1]
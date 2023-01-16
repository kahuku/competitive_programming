class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []
        for i in range(0, n + 1):
            if i <= 3:
                steps.append(i)
            else:
                steps.append(steps[i - 1] + steps[i - 2])
        return steps[n]
# botom-up DP

class Solution:
    # O(n) time | O(n) space
    def climbStairs(self, n: int) -> int:
        d = [0, 1, 2]
        while len(d) - 1 < n:
            d.append(d[-1] + d[-2])
        return d[n]
    
class Solution:
    # O(n) time | O(1) space
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b
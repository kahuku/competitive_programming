class Solution:
    def numSquares(self, n: int) -> int:
        self.squares = []
        for i in range(1, 101):
            self.squares.append(i ** 2)

        dp = [0]
        for i in range(1, n + 1):
            m = float('inf')
            for j in range(len(self.squares)):
                if self.squares[j] > i:
                    break
                m = min(m, dp[i - self.squares[j]] + 1)
            dp.append(m)
        print(dp)
        return dp[n]
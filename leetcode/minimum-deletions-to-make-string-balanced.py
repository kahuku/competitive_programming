class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0]
        bs = 0
        for i in range(len(s)):
            if s[i] == 'b':
                bs += 1
                dp.append(dp[i])
            else:
                dp.append(min(dp[i] + 1, bs))
        return dp[len(s)]
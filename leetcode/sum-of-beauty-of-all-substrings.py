from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        n = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                sub = s[i:j+1]
                c = Counter(sub)
                n += max(c.values()) - min(c.values())
        return n
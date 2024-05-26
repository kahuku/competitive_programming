# strings

from collections import defaultdict

class Solution:
    # O(n) time | O(n) space
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        n = 0
        plusOne = False
        for _, v in d.items():
            n += (v // 2) * 2
            if v % 2 != 0:
                plusOne = True
        return n + 1 if plusOne else n
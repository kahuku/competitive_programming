from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        l = 0
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        vals = d.values()
        one_used = False
        for val in vals:
            if not one_used:
                if val % 2 == 1:
                    l += 1
                    one_used = True
            l += val // 2 * 2
        return l
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        p_freqs = Counter(p)
        out = []

        for i in range(len(s) - lp + 1):
            if Counter(s[i:i+lp]) == p_freqs:
                out.append(i)

        return out
            
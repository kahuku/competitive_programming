class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted([c for c in s]))
        t = ''.join(sorted([c for c in t]))
        for cs, ct in zip(s, t):
            if cs != ct:
                return ct
        return t[-1]
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        s_i = 0
        for letter in t:
            if s_i < len(s) and s[s_i] == letter:
                s_i += 1
        return s_i == len(s)
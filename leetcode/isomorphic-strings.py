class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapping = {}
        for s1, s2 in zip(s[::1], t[::1]):
            if s1 in mapping.keys():
                if mapping[s1] != s2: return False
            else:
                if s2 not in mapping.values(): 
                    mapping[s1] = s2
                else: 
                    return False
        return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(zip(s,t)))==len(set(t))
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
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        p1, p2 = [], []
        sd, td = {}, {}
        n1, n2 = 1, 1

        for c in s:
            if c not in sd:
                sd[c] = n1
                n1 += 1
            p1.append(sd[c])
        
        for c in t:
            if c not in td:
                td[c] = n2
                n2 += 1
            p2.append(td[c])

        for a, b in zip(p1, p2):
            if a != b: return False
        return True
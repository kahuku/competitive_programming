class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1, d2 = {}, {}
        for char in string.ascii_lowercase:
            d1[char], d2[char] = 0, 0
        for char in s:
            d1[char] += 1
        for char in t:
            d2[char] += 1

        for k1, k2 in zip(d1.keys(), d2.keys()):
            if d1[k1] != d2[k2]:
                return False

        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted([*s])) == ''.join(sorted([*t])) if len(s) == len(t) else False
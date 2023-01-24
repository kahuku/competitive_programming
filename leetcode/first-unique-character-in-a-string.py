class Solution:
    def firstUniqChar(self, s: str) -> int:
        d_pos = {}
        d_count = {}
        for i, char in enumerate(s):
            if char not in d_pos:
                d_pos[char] = i
            if char not in d_count:
                d_count[char] = 0
            d_count[char] += 1
        counts = sorted(d_count.items(), key=lambda x: x[1])
        return -1 if counts[0][1] != 1 else d_pos[counts[0][0]]

import string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        for char in string.ascii_lowercase:
            try:
                i, i2 = s.index(char), s.rindex(char)
                if i == i2:
                    ans = min(ans, i)
            except:
                pass
        return ans if ans != len(s) else -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
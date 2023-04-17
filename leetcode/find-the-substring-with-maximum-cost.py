# DOES NOT WORK -- TLE
import string
from functools import lru_cache

alphabet = list(string.ascii_lowercase)

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        costs = [i + 1 for i in range(26)]
        for i, char in enumerate(chars):
            ind = alphabet.index(char)
            costs[ind] = vals[i]
        
        @lru_cache
        def get_substring_cost(substr):
            cost = 0
            for char in substr:
                cost += costs[alphabet.index(char)]
            return cost
        
        m = 0
        se = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub in se: continue
                se.add(sub)
                m = max(m, get_substring_cost(sub))
        return m
    

import string

alphabet = list(string.ascii_lowercase)

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        costs = [i + 1 for i in range(26)] #it would be better as a dictionary but hey it works lol
        for i, char in enumerate(chars):
            ind = alphabet.index(char)
            costs[ind] = vals[i]

        ans = [0]
        m = 0
        for i in range(len(s)):
            ind = alphabet.index(s[i])
            ans1 = ans[-1] + costs[ind]
            ans2 = costs[ind]
            ans.append(max(ans1, ans2))
            m = max(m, ans[-1])

        return m
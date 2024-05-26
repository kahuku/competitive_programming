# dictionaries

from collections import defaultdict

class Solution:
    # O(n) time | O(n) space
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        for letter in ransomNote:
            d1[letter] += 1
        for letter in magazine:
            d2[letter] += 1
        return all(d1[l] <= d2[l] for l in d1.keys())
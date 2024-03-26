# String

class Solution:
    # O(nlogn) time | O(1) space
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
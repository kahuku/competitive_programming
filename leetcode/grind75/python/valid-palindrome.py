# String
class Solution:
    # O(n) time | O(1) space
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])
        return s == s[::-1]
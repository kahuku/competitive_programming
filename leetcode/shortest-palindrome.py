class Solution:
    def shortestPalindrome(self, s: str) -> str:
        indices = [i + 1 for i in range(len(s)) if s[i] == s[0]][1:][::-1]
        for i in indices:
            sub = s[:i]
            if sub == sub[::-1]:
                return s[i:][::-1] + s
        return s[::-1] + s[1:]
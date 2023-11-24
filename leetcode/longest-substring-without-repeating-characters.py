class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        for i in range(len(s)):
            used = set()
            for j in range(i, len(s)):
                if s[j] in used:
                    break
                else:
                    used.add(s[j])
            m = max(m, len(used))
        return m
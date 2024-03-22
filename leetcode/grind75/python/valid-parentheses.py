# Stack

class Solution:
    # O(n) time | O(n) space
    def isValid(self, s: str) -> bool:
        opens = '{(['
        closes = '})]'
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                i = closes.index(c)
                if len(stack) == 0 or stack[-1] != opens[i]: return False
                stack.pop()
        return len(stack) == 0
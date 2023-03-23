class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        m = 0
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == ')':
                stack.pop()
            m = max(len(stack), m)
        return m
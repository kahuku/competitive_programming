class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
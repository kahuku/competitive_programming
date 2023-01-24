class Solution:
    def isValid(self, s: str) -> bool:
        s = s.replace("\"", "")
        stack = []
        opening = ['(', '[', '{']
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if char == ')':
                    if len(stack) and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif char == ']':
                    if len(stack) and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif char == '}':
                    if len(stack) and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if not len(stack):
            return True
        else:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []
        opening = set(['(', '[', '{'])
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not len(stack):
                    return False
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        return True if not len(stack) else False
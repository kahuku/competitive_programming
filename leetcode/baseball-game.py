class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                x = stack.pop()
                stack.append(x)
                stack.append(x * 2)
            elif op == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(y)
                stack.append(x)
                stack.append(x + y)
            else:
                stack.append(int(op))
        return sum(stack)
class MinStack:

    def __init__(self):
        self.stack = None

    def push(self, val: int) -> None:
        if self.stack is None:
            self.stack = self.Node(val, val, None)
        else:
            self.stack = self.Node(val, min(val, self.stack.min), self.stack)

    def pop(self) -> None:
        self.stack = self.stack.next

    def top(self) -> int:
        return self.stack.val

    def getMin(self) -> int:
        return self.stack.min

    class Node:

        def __init__(self, val, m, n):
            self.val = val
            self.min = m
            self.next = n

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# Queues, stacks

class MyStack:
    def __init__(self):
        self.stack = []
    
    def add(self, x: int) -> None:
        self.stack = [x] + self.stack

    def pop(self) -> int:
        x = self.stack.pop(0)
        return x

    # def peek(self) -> int:
    #     return self.stack[0]
    
    def size(self) -> int:
        return len(self.stack)
    
    # def isEmpty(self) -> bool:
    #     return len(self.stack) == 0

class MyQueue:

    def __init__(self):
        self.q = MyStack()
        self.helper = MyStack()

    def push(self, x: int) -> None:
        # O(1) time | O(1) space
        self.q.add(x)

    def pop(self) -> int:
        # O(n) time | O(n) space
        for _ in range(self.q.size() - 1):
            self.helper.add(self.q.pop())
        x = self.q.pop()
        for _ in range(self.helper.size()):
            self.q.add(self.helper.pop())
        return x

    def peek(self) -> int:
        # O(1) time | O(1) space
        # Should be n/n like the previous method, just used a shortcut here
        return self.q.stack[-1]

    def empty(self) -> bool:
        # O(1) time | O(1) space
        return self.q.size() == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
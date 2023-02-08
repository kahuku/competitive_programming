class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range(2, n + 1):
            f.append(f[i-1] + f[i-2])
        return f[n]

class Solution:
    def fib(self, n: int) -> int:
        prevprev = 0
        prev = 1
        for i in range(2, n + 1):
            curr = prevprev + prev
            prevprev = prev
            prev = curr
        return curr if n > 1 else n
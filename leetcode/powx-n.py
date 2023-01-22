class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        elif x == 0:
            return 0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x, n - 1)

class Solution:
    myPow = pow
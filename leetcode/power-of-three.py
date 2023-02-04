class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n / 3)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (3 ** 19) % n == 0
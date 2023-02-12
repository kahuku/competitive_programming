import numpy as np
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            s = str(np.base_repr(n, base=i))
            if s != s[::-1]:
                return False
        return True

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
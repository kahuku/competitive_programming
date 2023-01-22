class Solution:
    def isHappy(self, n: int) -> bool:
        def squareDigits(n):
            n = str(n)
            r = 0
            for dig in n:
                r += int(dig) ** 2
            return r
        
        prev = set()
        while n not in prev:
            prev.add(n)
            n = squareDigits(n)
        return True if n == 1 else False
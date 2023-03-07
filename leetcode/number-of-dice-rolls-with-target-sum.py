class Solution:
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @cache
        def search(rolls, targetLeft):
            if rolls == 0 and targetLeft == 0:
                return 1
            elif rolls == 0 or targetLeft < 0:
                return 0
            return sum([search(rolls - 1, targetLeft - i) for i in range(1, k + 1)])

        ways = search(n, target)
        return ways % (10 ** 9 + 7)
    
class Solution:
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        cache = {}
        
        def search(rolls, targetLeft):
            if (rolls, targetLeft) in cache:
                return cache[(rolls, targetLeft)]
            if rolls == 0 and targetLeft == 0:
                return 1
            elif rolls == 0 or targetLeft < 0:
                return 0
            cache[(rolls, targetLeft)] = sum([search(rolls - 1, targetLeft - i) for i in range(1, k + 1)])
            return cache[(rolls, targetLeft)]

        ways = search(n, target)
        return ways % (10 ** 9 + 7)
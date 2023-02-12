class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(dig) for dig in str(n)]
        prod = reduce((lambda a, b: a * b), nums)
        su = reduce((lambda a, b: a + b), nums)
        return prod - su
class Solution:
    def numberOfWays(self, s: str) -> int:
        zero_ones, one_zeros, count, ones, zeros = 0, 0, 0, 0, 0
        for building in s:
            if building == "0":
                zeros += 1
                zero_ones += ones
                count += one_zeros
            if building == "1":
                ones += 1
                one_zeros += zeros
                count += zero_ones
        return count
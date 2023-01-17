class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n + 1):
            out.append(bin(i)[2:].count('1'))
        return out
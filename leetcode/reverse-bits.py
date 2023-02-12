class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n)).split("b")[1]
        n = n[::-1]
        n += '0' * (32 - len(n))
        n = int(n, base=2)
        return n

class Solution:
    def reverseBits(self, n: int) -> int:
        return int((str(bin(n)).split("b")[1])[::-1] + ('0' * (32 - len(str(bin(n)).split("b")[1]))), base=2)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set([char for char in jewels])
        c = 0
        for stone in stones:
            if stone in s:
                c += 1
        return c
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum([int(i) for i in person]) for person in accounts])
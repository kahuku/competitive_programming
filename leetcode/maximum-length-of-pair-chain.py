class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        chain = 0
        num = float('-inf')
        for i in range(len(pairs)):
            if num < pairs[i][0]:
                num = pairs[i][1]
                chain += 1
        return chain
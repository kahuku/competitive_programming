class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m, s = 0, 0
        for i in range(len(gain)):
            s += gain[i]
            if s > m:
                m = s
        return m

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = max(list(accumulate(gain, operator.add)))
        return m if m > 0 else 0

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(list(accumulate(gain, operator.add))) if max(list(accumulate(gain, operator.add))) > 0 else 0

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = [0, gain[0]]
        for i in range(1, len(gain)):
            pre.append(gain[i] + pre[i])
        return max(pre) if max(pre) > 0 else 0
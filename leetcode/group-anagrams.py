class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            t = str(sorted([char for char in s]))
            if t in d:
                d[t].append(s)
            else:
                d[t] = [s]
        return d.values()
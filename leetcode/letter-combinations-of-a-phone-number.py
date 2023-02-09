class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        lists = [d[digit] for digit in digits]
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return lists[0]
        out = []
        if len(digits) == 2:
            for d1 in lists[0]:
                for d2 in lists[1]:
                    out.append(d1 + d2)
        if len(digits) == 3:
            for d1 in lists[0]:
                for d2 in lists[1]:
                    for d3 in lists[2]:
                        out.append(d1 + d2 + d3)
        if len(digits) == 4:
            for d1 in lists[0]:
                for d2 in lists[1]:
                    for d3 in lists[2]:
                        for d4 in lists[3]:
                            out.append(d1 + d2 + d3 + d4)
        return out
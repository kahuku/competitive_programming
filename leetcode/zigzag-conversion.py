class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arrs = [[]for _ in range(numRows)]
        row = 0
        increasing = True

        if numRows == 1:
            return s

        for i, char in enumerate(s):
            arrs[row].append(char)
            if increasing:
                if row == numRows - 1:
                    increasing = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    increasing = True
                    row += 1
                else:
                    row -= 1

        return ''.join([''.join(arr) for arr in arrs])
            
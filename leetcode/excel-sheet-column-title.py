class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ''
        while columnNumber > 0:
            columnNumber -= 1
            i = columnNumber % 26
            c = chr(i + ord('A'))
            columnNumber //= 26
            out += c
        return out[::-1]
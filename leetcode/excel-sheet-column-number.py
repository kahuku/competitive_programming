class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        i = 0
        for letter in columnTitle[::-1]:
            dig = ord(letter) - 64 # because ascii A is 65
            n += dig * (26 ** i)
            i += 1
        return n
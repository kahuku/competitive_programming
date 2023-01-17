class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i = 0
        total = 0
        while i < len(s):
            if s[i:i+2] in numerals.keys() and i != len(s) - 1:
                total += numerals[s[i:i+2]]
                i += 2
            else:
                total += numerals[s[i]]
                i += 1

        return total

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            total += numerals[char]
        return total

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if numerals[s[i]] < numerals[s[i+1]]:
                total -= numerals[s[i]]
            else:
                total += numerals[s[i]]
        total += numerals[s[-1]]
        return total
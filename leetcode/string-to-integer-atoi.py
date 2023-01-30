class Solution:
    def myAtoi(self, s: str) -> int:
        new_s = ''
        sign_used = False
        valid_used = False
        for i, char in enumerate(s.strip()):
            if char in set(['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                if sign_used and char in set(['-', '+']) or char in set(['-', '+']) and i > 0:
                    break
                else:
                    new_s += char
                    valid_used = True
                if char in set(['-', '+']):
                    sign_used = True
            else:
                if valid_used or not i:
                    break
        num = 0
        negative = False
        for i in range(len(new_s)):
            char = new_s[::-1][i]
            if char == '-':
                negative = True
            elif char == '+':
                pass
            else:
                num += int(char) * 10 ** i
        if num < 2 ** 31:
            return num if not negative else -1 * num
        else:
            return 2 ** 31 - 1 if not negative else -2 ** 31
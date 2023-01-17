class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_i, b_i = len(a) - 1, len(b) - 1
        out = ''
        carry = 0
        while a_i >= 0 or b_i >= 0:
            s = carry
            if a_i >= 0: s += ord(a[a_i]) - ord('0')
            if b_i >= 0: s += ord(b[b_i]) - ord('0')
            carry = 1 if s > 1 else 0
            out += str(s % 2)
            a_i -= 1; b_i -= 1
        if carry: out += '1'
        return out[::-1]

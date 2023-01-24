class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for pair in knowledge:
            d[pair[0]] = pair[1]

        out = ''
        s = s.split(')')
        for word in s:
            key = ''
            for i, char in enumerate(word):
                if char == '(':
                    key = word[i+1:]
                    break
                out += char
            if key in d:
                out += d[key]
            elif key != '':
                out += '?'
        return out

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        s = s.split('(')
        out = s[0]
        for i in range(1, len(s)):
            key, text = s[i].split(')')
            out = out + d.get(key, '?') + text
        return out
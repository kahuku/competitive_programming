import collections
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        for letter in s:
            if letter != "#":
                stack_s.append(letter)
            else:
                try:
                    stack_s.pop()
                except Exception:
                    pass
        
        for letter in t:
            if letter != "#":
                stack_t.append(letter)
            else:
                try:
                    stack_t.pop()
                except Exception:
                    pass
        string_s, string_t = ''.join(stack_s), ''.join(stack_t)
        print(string_s, string_t)
        
        if string_s == string_t:
            print("HERE")
            return True
        return False
            
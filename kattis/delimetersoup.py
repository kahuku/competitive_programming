input(); l = input()
s = []
for i, c in enumerate(l):
    if c == " ":
        continue
    elif c == "(" or c == "[" or c == "{":
        s.append(c)
    elif c == ")":
        if len(s) == 0 or s.pop() != "(":
            print(c, i)
            exit()
    elif c == "]":
        if len(s) == 0 or s.pop() != "[":
            print(c, i)
            exit()
    elif c == "}":
        if len(s) == 0 or s.pop() != "{":
            print(c, i)
            exit()
if len(s) == 0 or all(c in {"(", "[", "{"} for c in s):
    print("ok so far")
else:
    print(s.pop(), len(l))
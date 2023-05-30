input(); inp = input()
stack = []
for char in inp:
    if (char == ")" or char == "]" or char == "}") and not len(stack):
        print("Invalid")
        exit(0)
    if char == ")" and stack[-1] == "(" or char == "]" and stack[-1] == "[" or char == "}" and stack[-1] == "{":
        stack.pop()
    elif char == ")" or char == "]" or char == "}":
        print("Invalid")
        exit(0)
    else:
        stack.append(char)
print("Valid" if not len(stack) else "Invalid")
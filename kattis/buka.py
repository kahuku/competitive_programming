a, op, b = int(input()), input(), int(input())
print(a + b if op == "+" else a * b)

# solution 2
a, op, b = int(input()), input(), int(input())
print(eval(f"{a}{op}{b}"))
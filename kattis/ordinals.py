def recurse(n):
    if n == 0: return '{}'
    s = '{'
    for i in range(n):
        s += recurse(i)
        if i != n - 1: s += ','
    s += '}'
    return s

print(recurse(int(input())))

# solution 2
def f(n):
    if n == 0: return '{}'
    return '{' + ','.join(f(i) for i in range(n)) + '}'
print(f(int(input())))
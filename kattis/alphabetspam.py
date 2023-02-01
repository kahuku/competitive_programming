import string
upper, lower = set(string.ascii_uppercase), set(string.ascii_lowercase)
underscores, symbols = set('_'), list('! @ # $ % ^ & * ( ) - { } [ ] | \\ : ; \' \" ~ ` < , > . ? / + ='.split())
symbols.extend(list(string.digits))
symbols = set(symbols)
u_c, l_c, un_c, s_c = 0, 0, 0, 0
s = input()
for char in s:
    if char in upper:
        u_c += 1
    elif char in lower:
        l_c += 1
    elif char in underscores:
        un_c += 1
    elif char in symbols:
        s_c += 1
    else:
        print("Not found:", char)
print(un_c / len(s))
print(l_c / len(s))
print(u_c / len(s))
print(s_c / len(s))
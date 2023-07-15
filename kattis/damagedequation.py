# passed half of test cases
a, b, c, d = map(int, input().split())
operators = ['+', '-', '*', '//']
flag = False
options = []
for op1 in operators:
    for op2 in operators:
        if op1 == '//' and b == 0 or op2 == '//' and d == 0:
            continue
        if eval(f'{a}{op1}{b}=={c}{op2}{d}'):
            if op1 == '//':
                op1 = '/'
            if op2 == '//':
                op2 = '/'
            options.append(f'{a} {op1} {b} = {c} {op2} {d}')
            flag = True
if not flag:
    print('problems ahead')
else:
    for option in sorted(options):
        print(option)
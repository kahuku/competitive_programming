def ones(num):
    m = 0
    for i in range(len(num)):
        sub = num[0:i + 1]
        m = max(m, bin(int(sub)).count('1'))
    return m

for _ in range(int(input())):
    num = input()
    print(ones(num))
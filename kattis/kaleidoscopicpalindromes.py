def num_to_base(num, base):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return ''.join(map(str, digits[::-1]))

a, b, k = map(int, input().split())
count = 0
for i in range(a, b + 1):
    valid = True
    for j in range(2, k + 1):
        num = num_to_base(i, j)
        if num != num[::-1]:
            valid = False
            break
    count += 1 if valid else 0
print(count)
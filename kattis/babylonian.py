def sexagesimal_to_decimal(sexagesimal):
    decimal = 0
    for i, digit in enumerate(sexagesimal.split(',')):
        if digit == '': continue
        decimal += int(digit) * (60 ** (len(sexagesimal.split(',')) - i - 1))
    return decimal

for _ in range(int(input())):
    print(sexagesimal_to_decimal(input()))
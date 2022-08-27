def get_digits(num):
    for digit in num:
        if (int(digit) != 0):
            digits.append(int(digit))

num = input()

digits = []
get_digits(num)

while (len(digits) != 1):
    #print(digits)
    prod = 1;
    for digit in digits:
        prod *= digit
    digits = []
    get_digits(str(prod))
print(digits[0])

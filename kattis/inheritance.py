# TLE
def check_valid_number(num):
    while num > 0:
        digit = num % 10
        if digit != 4 and digit != 2:
            return False
        num //= 10
    return True

def possible_number_of_kids(n):
    kids = []
    for i in range(1, n + 1):
        if n % i == 0 and check_valid_number(i):
            kids.append(i)
    return kids

p = int(input())
kids = possible_number_of_kids(p)
for num_kids in sorted(kids):
    print(num_kids)
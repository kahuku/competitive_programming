def findPrime (num):
    flag = True
    for i in range (2, num-1):
        if num % i == 0:
            flag = False
    return flag

while True:
    inp = int(input("Enter a number to check prime\n"))
    print(findPrime(inp))

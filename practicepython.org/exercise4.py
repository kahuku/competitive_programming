num = int(input("What's your number?"))

x = range(2,num)
a = []

for elem in x:
    if (num % elem == 0):
        a.append(elem)

print("Your divisors are: ", a)

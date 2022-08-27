inp = input().split()
inp = [int(i) for i in inp]
x = inp[0]
y = inp[1]
n = inp[2]

i = 1
while i <= n:
    if (i % x == 0) and (i % y == 0):
        print("FizzBuzz")
    elif (i % x == 0):
        print("Fizz")
    elif (i % y == 0):
        print("Buzz")
    else:
        print(i)
    i += 1
    

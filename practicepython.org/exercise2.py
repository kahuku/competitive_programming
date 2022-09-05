print("Welcome to the odd/even tester! Input a number to begin")
inp = int(input())

if (inp%2 == 0):
    print("Your number is even")
else:
    print("Your number is odd")
      
if (inp%4 == 0):
    print("Also divisible by 4")
    
print("Enter a second number")
inp2 = int(input())

if(inp%inp2 == 0):
    print("Those are divisible")
else:
    print("Those are not divisible")

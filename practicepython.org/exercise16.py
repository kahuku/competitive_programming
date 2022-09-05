import random
import string

def genW():
    passList = ["qwerty","1111","password","password1","123456"]
    return random.choice(passList)

def genM():
    length = int(input("Length: "))
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(0,length))

def genS():
    while True:
        length = int(input("Length: "))
        if length >= 10:
            break
        else:
            print("too short")
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(0,length))

while 1 == 1:
    print("Password strength level [1/2/3]:")
    option = input()
    if option == 'x':
        break
    if int(option) == 1:
        password = genW()
    if int(option) == 2:
        password = genM()
    if int(option) == 3:
        password = genS()
    print(password)
    again = input("Make another? Y/n:")
    if again != 'Y':
        break

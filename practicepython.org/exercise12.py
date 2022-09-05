import random

def splice(lis):
    b = [lis[0]]
    b.append(lis[len(lis)-1])
    return (b)
while 1 == 1:
    inp = input("Hit Enter to generate a list")
    if inp == "":
        a = random.sample(range(0,101),10)
        print(a)
        print(splice(a))
        
        

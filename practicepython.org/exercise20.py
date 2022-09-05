import random

def genList():
    ordered_list = []
    ordered_list.append(random.randint(0, 10))
    for i in range(5):
        ordered_list.append(random.randint(ordered_list[i],(ordered_list[i]+15)))
    return ordered_list

def checkIn(n,l):
    start = 1
    end = len(l)-1
    flag = True
    while flag == True:
        mI = (end-start)/2
        mE = l[mI]
        if mE == n:
            print(True)
            flag = False
        elif mE < n:
            end = m
        else:
            start = mI
        
if __name__=="__main__":
    l = genList()
    print(l)
    num = random.randint(0,100)
    checkIn(num,l)

""" #doesn't work
nums = []
with open('happynumbers.txt','r') as happyF:
    primeF = open('primenumbers.txt','r')
    happyNum = int(happyF.readline())
    primeNum = int(primeF.readline())
    for happyNum in happyF:
        for primeNum in primeF:
            if (primeNum == happyNum):
                nums.append(primeNum)
            primeNum = int(primeF.readline())
    happyNum = int(happyF.readline())
for num in nums:
    print(num)
"""

sharedNums = []
happyNums = []
primeNums = []

with open('primenumbers.txt') as prime:
    line = prime.readline()
    while line:
        primeNums.append(int(line))
        line = prime.readline()

with open('happynumbers.txt') as happy:
    line = happy.readline()
    while line:
        happyNums.append(int(line))
        line = happy.readline()

for elem in primeNums:
    if elem in happyNums:
        sharedNums.append(elem)

for n in sharedNums:
    print(n)

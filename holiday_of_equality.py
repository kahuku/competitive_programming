_ = input()
people = [int(i) for i in input().split()]
high = max(people)
charge = 0
for person in people:
    charge += high - person
print(charge)
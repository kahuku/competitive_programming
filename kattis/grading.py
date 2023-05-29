a, b, c, d, e = [int(i) for i in input().split()]
g = int(input())
if g >= a:
    print("A")
elif g >= b:
    print("B")
elif g >= c:
    print("C")
elif g >= d:
    print("D")
elif g >= e:
    print("E")
else:
    print("F")

# solution 2
values = [int(i) for i in input().split()]
g = int(input())
grades = ['A', 'B', 'C', 'D', 'E', 'F']
result = next((grade for grade, value in zip(grades, values) if g >= value), 'F')
print(result)
a, b, year = map(int, input().split('/'))
if a <= 12 and b <= 12:
    print("either")
elif a <= 12:
    print("US")
else:
    print("EU")
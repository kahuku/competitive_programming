def happy(angry_mins, happy_mins, x):
    cycle_mins = happy_mins + angry_mins
    after = x % cycle_mins

    if after <= angry_mins and after > 0:
        return False
    else:
        return True

def func(a, b, c, d, x):
    dog1_happy = happy(a, b, x)
    dog2_happy = happy(c, d, x)
    if dog1_happy and dog2_happy:
        return "none"
    elif not dog1_happy and not dog2_happy:
        return "both"
    else:
        return "one"

a, b, c, d = [int(i) for i in input().split()]
p, m, g = [int(i) for i in input().split()]
print(func(a, b, c, d, p))
print(func(a, b, c, d, m))
print(func(a, b, c, d, g))
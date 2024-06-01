#1811A

# Wrong answer: example test case last 2 examples

def find_num(old, new):
    for i, dig in enumerate(old):
        if new >= int(dig):
            return old[:i] + str(new) + old[i:]
    return old + str(new)

for _ in range(int(input())):
    _, new = map(int, input().split())
    old = input()

    print("ANS:", find_num(old, new))
cases = int(input())
for _ in range(cases):
    toys = int(input())
    toys_dict = {}
    for _ in range(toys):
        toy, amount = input().split()
        if toy not in toys_dict:
            toys_dict[toy] = int(amount)
        else:
            toys_dict[toy] += int(amount)
    print(len(toys_dict))
    for key, value in sorted(toys_dict.items(), key=lambda x: (-x[1], x[0])):
        print(key, value)
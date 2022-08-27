def subtract(number, num_subs):
    if num_subs == 0:
        return number
    elif str(number)[-1] == '0':
        return subtract(int(number / 10), num_subs - 1)
    else:
        return subtract(number - 1, num_subs - 1)

number, num_subs = [int(i) for i in input().split()]
print(subtract(number, num_subs))

inp = [int(i) for i in input().split()]
n, serves = inp[0], inp[1] + inp[2]

if (serves // n) % 2 == 0:
    print('paul')
else:
    print('opponent')


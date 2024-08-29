import string

N, t = map(int, input().split())
a = list(map(int, input().split()))
match t:
    case 1:
        print(7)
    case 2:
        if a[0] > a[1]:
            print("Bigger")
        elif a[1] > a[0]:
            print("Smaller")
        else:
            print("Equal")
    case 3:
        print(sorted(a[:3])[1])
    case 4:
        print(sum(a))
    case 5:
        print(sum([num for num in a if num % 2 == 0]))
    case 6:
        print(''.join([string.ascii_lowercase[num % 26] for num in a]))
    case 7:
        i = 0
        s = set([0])
        while True:
            i = a[i]
            if i in s:
                print("Cyclic")
                break

            s.add(i)
            if i < 0 or i >= N:
                print("Out")
                break
            elif i == N - 1:
                print("Done")
                break
            else:
                continue

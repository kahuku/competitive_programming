def hail(input, currSum):
    if input == 1:
        print(1 + currSum)
    elif not input % 2:
        hail(input // 2, currSum + input)
    else:
        hail(3 * input + 1, currSum + input)

n = int(input())
hail(n, 0)
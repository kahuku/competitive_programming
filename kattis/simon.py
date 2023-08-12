for _ in range(int(input())):
    words = input().split()
    if len(words) >= 2 and words[0] == 'simon' and words[1] == 'says':
        print(' '.join(words[2:]))
    else:
        print()
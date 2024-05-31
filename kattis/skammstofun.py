import string
input();print(''.join([word[0] for word in input().split() if word[0] in string.ascii_uppercase]))
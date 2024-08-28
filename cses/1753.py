def kmpPreprocess(pattern):
    b = [None] * (len(pattern) + 1)
    b[0] = -1
    i = 0
    j = -1
    while i < len(pattern):
        while j >= 0 and pattern[i] != pattern[j]:
            j = b[j]
        i += 1
        j += 1
        b[i] = j
    return b

def kmpSearch(searchString, pattern, resetTable):
    c = 0
    i = 0
    j = 0
    while i < len(searchString):
        while j >= 0 and searchString[i] != pattern[j]:
            j = resetTable[j]
        i += 1
        j += 1
        if j == len(pattern):
            c += 1
            j = resetTable[j]
    return c

searchString = input()
pattern = input()
resetTable = kmpPreprocess(pattern)
print(kmpSearch(searchString, pattern, resetTable))
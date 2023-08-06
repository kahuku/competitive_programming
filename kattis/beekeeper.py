# doesn't work, no clue why
n = int(input())
while n != 0:
    words = []
    for i in range(n):
        words.append(input())
    max_count = 0
    max_word = ""
    for word in words:
        count = 0
        for i in range(len(word)-1):
            if word[i] in "aeiouy" and word[i] == word[i+1]:
                count += 1
        if count > max_count:
            max_count = count
            max_word = word
    print(max_word)
    n = int(input())
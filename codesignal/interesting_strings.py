# Databricks Summer intern 2024 app
# count interesting strings
# string is interesting if it has substring of len n of the same letter
# no continuation (n = 3, aaaa is not valid)
def solution(words, n):
    count = 0
    for word in word:
        count += int(interesting(word, n))
    return count

def interesting(word, n):
    word = '*' + word + '*'
    for i in range(1, len(word) - n + 1):
        sub = word[i:i+n]
        if len(set([letter for letter in sub])) == 1 and word[i - 1] != sub[0] and word[i+n] != sub[0]:
            return True
    return False
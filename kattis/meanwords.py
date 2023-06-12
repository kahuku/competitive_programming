words = [input() for _ in range(int(input()))]
new_word = ''
max_len = max(len(word) for word in words)
for i in range(max_len):
    val = 0
    count = 0
    for word in words:
        if i < len(word):
            val += ord(word[i]) - ord('a')
            count += 1
    new_word += chr(ord('a') + (val // count))
print(new_word)
import string
import operator

num_inputs = int(input())

for i in range(num_inputs):
    sentence = input()
    d = dict.fromkeys(string.ascii_lowercase, 0)
    
    for character in sentence:
        if character.lower() in d:
            d[character.lower()] += 1

    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    if sorted_d[0][1] > 0:
        print("pangram")
    else:
        missing = [key for key in d.keys() if d[key] == 0]
        print("missing", ''.join(missing))

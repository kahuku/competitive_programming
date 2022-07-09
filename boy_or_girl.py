username = input()

d = {}
for char in username:
    if char not in d:
        d.update({char: 0})
    d[char] += 1

print("CHAT WITH HER!" if len(d.keys()) % 2 == 0 else "IGNORE HIM!")

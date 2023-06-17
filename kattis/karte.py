s = input()
for i in range(0, len(s), 3):
    if s.count(s[i:i+3]) > 1:
        print("GRESKA")
        exit()
p = s.count("P")
k = s.count("K")
h = s.count("H")
t = s.count("T")
print(13-p, 13-k, 13-h, 13-t)
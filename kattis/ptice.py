a_seq = ['A', 'B', 'C']
b_seq = ['B', 'A', 'B', 'C']
g_seq = ['C', 'C', 'A', 'A', 'B', 'B']

n = int(input())
answers = input()
a = 0
b = 0
g = 0
for i in range(n):
    if answers[i] == a_seq[i % 3]:
        a += 1
    if answers[i] == b_seq[i % 4]:
        b += 1
    if answers[i] == g_seq[i % 6]:
        g += 1
m = max(a, b, g)
print(m)
if a == m:
    print("Adrian")
if b == m:
    print("Bruno")
if g == m:
    print("Goran")
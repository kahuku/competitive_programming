form = [int(input()) for _ in range(int(input()))]
passes = 1
for i in range(len(form) - 1):
    if form[i + 1] < form[i]: passes+=1
print(passes)
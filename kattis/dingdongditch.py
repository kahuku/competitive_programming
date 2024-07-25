input(); anger = sorted(list(map(int, input().split()))); friends = list(map(int, input().split()))
pre = [0, anger[0]]
for i in range(1, len(anger)):
    pre.append(anger[i] + pre[i])
for friend in friends:
    print(pre[friend])
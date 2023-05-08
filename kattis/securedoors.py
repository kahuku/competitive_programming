n = int(input())
d = {}
for i in range(n):
    action, name = input().split()
    if name not in d:
        d[name] = 0
    if action == "entry":
        if d[name] == 1:
            print(f"{name} entered (ANOMALY)")
        else:
            print(f"{name} entered")
        d[name] = 1
    else:
        if d[name] == 0:
            print(f"{name} exited (ANOMALY)")
        else:
            print(f"{name} exited")
        d[name] = 0
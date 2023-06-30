input(); l = input().split()
print("makes sense" if all(l[i] == "mumble" or int(l[i]) == i + 1 for i in range(len(l))) else "something is fishy")
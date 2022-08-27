friends = [input().split() for _ in range(int(input()))]
friends.sort(key=lambda x: int(x[1]), reverse=True)
names = []
birthdays = set()
for friend in friends:
    name, birthday = friend[0], friend[2]
    if birthday not in birthdays:
        birthdays.add(birthday)
        names.append(name)
print(len(names))
[print(name) for name in list(sorted(names))]
d = set([input().lower() for _ in range(int(input()))])
for word in input().split():
    if word.lower() not in d:
        print("Thore has left the chat")
        exit(0)
print("Hi, how do I look today?")
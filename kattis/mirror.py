for i in range(int(input())):
    lines, _ = map(int, input().split())
    print('Test', i + 1)
    image = []
    for _ in range(lines):
        image.append(input())
    for line in reversed(image):
        print(line[::-1])
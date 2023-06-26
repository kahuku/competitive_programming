rows = int(input())
board = []
for i in range(rows):
    row = input()
    if row.find('BBB') != -1 or row.find('WWW') != -1 or row.count('B') != row.count('W'):
        print(0)
        exit()
    board.append(row)
for i in range(rows):
    col = ''
    for j in range(rows):
        col += board[j][i]
    if col.find('BBB') != -1 or col.find('WWW') != -1 or col.count('B') != col.count('W'):
        print(0)
        exit()
print(1)
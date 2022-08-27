def transpose(board):
    transposed = []
    for i in range(len(board[0])):
        transposed.append([])

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            transposed[j].append(board[i][j])
    return transposed

def getWords(board, wordlist):
    for row in board:
        rowText = ''.join(row)
        words = [word for word in rowText.split('#') if word != '']
        for word in words:
            if len(word) > 1:
                wordlist.add(word)

inp = [int(i) for i in input().split()]
rows, cols = inp[0], inp[1]

board = []
for row in range(rows):
    board.append([char for char in input()])

wordlist = set()

getWords(board, wordlist)

boardTranspose = transpose(board)
getWords(boardTranspose, wordlist)

print(sorted(wordlist)[0])

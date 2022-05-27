import numpy as np

def getWords(board, wordlist):
    for row in board:
        word = ''
        for i, char in enumerate(row, start=1):
            if char != '#' and i != len(row):
                word += char
            if i == len(row) and char != '#':
                word += char
                if len(word) > 1:
                    wordlist.add(word)
            if i == len(row) and char == '#':
                if len(word) > 1:
                    wordlist.add(word)
            if i != len(row) and char == '#':
                if len(word) > 1:
                    wordlist.add(word)
                word = ''
        if word != '':
            if len(word) > 1:
                wordlist.add(word)    

inp = [int(i) for i in input().split()]
rows, cols = inp[0], inp[1]

#get board into memory
board = []
for row in range(rows):
    board.append([char for char in input()])

wordlist = set()

#get horizontal words
getWords(board, wordlist)

#get vertical words
boardTranspose = np.transpose(board)
getWords(boardTranspose, wordlist)

print(sorted(wordlist)[0])

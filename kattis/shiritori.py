player1, player2 = set(), set()
last_word = None
turn = 1
for i in range(int(input())):
    word = input()
    if word in player1 or word in player2:
        print('Player', turn, 'lost')
        exit(0)
    if last_word is not None and last_word[-1] != word[0]:
        print('Player', turn, 'lost')
        exit(0)
    if turn == 1:
        player1.add(word)
        turn = 2
    else:
        player2.add(word)
        turn = 1
    last_word = word
print('Fair Game')
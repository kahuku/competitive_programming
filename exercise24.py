def drawBoard ():
    #draws whole board
    drawRow()
    print('')
    for x in range(0,3):
        drawColumn()
        print('')
        drawRow()
        print('')

def drawRow():
    print(' ',end='')
    for x in range(0,3):
        for y in range(0,3):
            print("-",end='')
        print(" ",end='')

def drawColumn():
    for x in range(0,4):
        print("|",end='')
        for y in range(0,3):
            print(" ",end='')

drawBoard()

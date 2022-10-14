import sys
import heapq

def ds(moves):
    boolQueue = True
    boolStack = True
    boolPQueue = True

    queue = []
    stack = []
    pQueue = []

    for move in moves:
        op = move[0]
        if op == 1:
            queue.append(move[1])
            stack.append(move[1])
            heapq.heappush(pQueue, -1 * move[1])
        else:
            try:
                q = queue.pop(0)
                if q != move[1]:
                    boolQueue = False
            except Exception:
                boolQueue = False

            try:
                s = stack.pop()
                if s != move[1]:
                    boolStack = False
            except Exception:
                boolStack = False

            try:
                p = -1 * heapq.heappop(pQueue)
                if p != move[1]:
                    boolPQueue = False
            except Exception:
                boolPQueue = False
    
    if boolQueue and not boolStack and not boolPQueue:
        print("queue")
    elif not boolQueue and boolStack and not boolPQueue:
        print("stack")
    elif not boolQueue and not boolStack and boolPQueue:
        print("priority queue")
    elif not boolQueue and not boolStack and not boolPQueue:
        print("impossible")
    else:
        print("not sure")
    

inp = sys.stdin.read().split('\n')

i = inp.pop(0)
while i != '':
    i = int(i)

    moves = []
    for _ in range(i):
        moves.append([int(i) for i in inp.pop(0).split()])
    ds(moves)

    i = inp.pop(0)
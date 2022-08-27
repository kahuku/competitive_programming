n = int(input())
for i in range(n):
    inp = [float(i) for i in input().split()]
    beats = inp[0]
    sec = inp[1]
    bpm = 60 * beats / sec
    var = 60 / sec
    print(bpm - var, " ", bpm, " ", bpm + var)
    

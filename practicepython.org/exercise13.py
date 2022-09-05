def fib(length):
    a1 = 0
    a2 = 1
    seq = [1]
    for i in range(0, length-1):
        z = a1+a2
        seq.append(z)
        a1 = a2
        a2 = z
    print(seq)
    
while 1 == 1:
    inp = int(input("Enter the number of fibonnaci numbers to generate: "))
    fib(inp)

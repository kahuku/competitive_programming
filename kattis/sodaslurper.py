inp = input().split()
num_empty = int(inp[0])
num_found = int(inp[1])
num_reqd = int(inp[2])

bottles = num_empty + num_found

drank = 0
while bottles >= num_reqd:
    purchased = bottles // num_reqd
    bottles %= num_reqd
    bottles += purchased
    #print("Bottles: ", bottles)
    drank += purchased
    #print("Drank: ", drank)


print(drank)

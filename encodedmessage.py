num_cases = int(input())

for i in range(num_cases):
    encoded_message = input()
    square_dim = int(len(encoded_message) ** 0.5)
    encoded_grid = []
    for j in range(square_dim):
        encoded_grid.append(encoded_message[0 + square_dim * j : square_dim + square_dim * j])
    #print(encoded_grid)
    #print(square_dim)
    decoded_grid = []
    y = 0
    while y < square_dim:
        to_append = ''
        z = 0
        while z < square_dim:
            #print(encoded_grid[z][y])
            to_append += encoded_grid[z][y]
            z += 1
        #print(to_append)
        decoded_grid.append(to_append)
        y += 1
        
    decoded_grid.reverse()
    #print()
    #print(decoded_grid)
    s = ''
    for m in decoded_grid:
        s += m
    print(s)

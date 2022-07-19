def make_pyramid(layers, num_cubes):
    cubes_this_layer = sum(range(layers)) + layers
    # print("This layer", cubes_this_layer, "cubes")
    if num_cubes > cubes_this_layer:
        num_cubes -= cubes_this_layer
        return make_pyramid(layers + 1, num_cubes)
    elif num_cubes == cubes_this_layer:
        return layers
    else:
        return layers - 1

num_cubes = int(input())
layers = make_pyramid(0, num_cubes)
print(layers)
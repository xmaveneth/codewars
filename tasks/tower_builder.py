def tower_builder(n_floors):
    size = n_floors * 2 - 1
    return [('*' * (i * 2 - 1)).center(size) for i in range(1, n_floors + 1)]

# https://www.codewars.com/kata/576757b1df89ecf5bd00073b

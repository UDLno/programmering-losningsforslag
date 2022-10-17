def print_as_matrix(list):
    for row in list:
        print(" ".join([str(e) for e in row]))

# a)
my_list = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

print_as_matrix(my_list)

print("-----------")

# b)
sliced_list = my_list[1:3]
print_as_matrix(sliced_list)
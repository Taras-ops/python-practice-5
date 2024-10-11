def find_max(a, b):
    if a >= b:
        return a

    return b


def find_max_of_three(x, y, z):
    c = find_max(x, y)
    return find_max(z, c)


print(find_max(1, 3))
print(find_max_of_three(1, 2, 3))

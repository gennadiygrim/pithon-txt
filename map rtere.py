def rectangle_area(a, b):
    return a * b


print(rectangle_area(17, 45))
print((lambda a, b: a + b)(29, 38))


def maximum(a, b):
    if a < b:
        return a
    else:
        return b


print(maximum(8, 10))
print((lambda a, b: a if a > b else b)(30, 45))

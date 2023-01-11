from functools import reduce

print(reduce(lambda a, b: a * b, (4, 4, 3, 5, 6, 9, 8)))

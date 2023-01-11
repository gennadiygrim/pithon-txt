numbers = {1, 2, 3, 4, 5, 6, 7, 8}
numbers2 = {1, 54, 545, 5455, 6, 7, 66, 777}
numbers3 = numbers.union(numbers2)
numbers4 = numbers | numbers2
print(numbers3, "union")
print(numbers3, "|")
numbers3 = numbers.intersection(numbers2)
numbers4 = numbers.intersection(numbers2)
print(numbers4, "intersection")
numbers5 = numbers & numbers2
print(numbers5, "&")
numbers6 = numbers - numbers2
print(numbers6, "-")
numbers7 = numbers6.copy()
print(numbers7, "copy")
numbers8 = frozenset({1, 54, 545, 5455, 6, 7, 66, 777})
print(numbers8)
numbers9 = set()
print(numbers9)
print(type(numbers9))
numbers10 = set(
    [
        1,
        2,
        3,
        4,
        5,
        6,
        6,
        7,
        7,
        8,
        8,
        8,
        8,
    ]
)
print(numbers10)
print(type(numbers10))
print(2 in numbers10)
print(numbers10)
print(65 in numbers10)
print(numbers10.__len__())

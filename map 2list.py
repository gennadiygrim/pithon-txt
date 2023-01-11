def f(a, b):
    return a + b


a = map(f, [3, 3, 3], [5, 5, 5])
print(list((a)))

b = map(f, [3, 3, 3], [5, 5])
print(list((b)))
print(list((a)))

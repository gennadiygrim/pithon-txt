a = map(lambda x: x + 19, (3, 5, 6))
print(list(a))


def f(a):
    if a % 2 == 0:
        return a


b = map(f, (2, 4, 7, 7, 9))
print(list(b))

b1 = filter(lambda x: x % 2 == 0, (2, 4, 7, 7, 9))
print(list(b1))

def degree(x):
    y = 2

    def degree_two():
        return y**x

    return degree_two()


print(degree(5))

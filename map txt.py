with open("chisla2.txt") as f:
    n = int(f.readline())
    n1 = f.readline()
    print(n)
    print(n1)
with open("chisla2.txt") as f:
    for i in range(n + 1):
        if i == 0:
            print(f.readline())
        else:
            a, b = map(int, f.readline())
            print(a + b)

        # a,b = map(int,f.readline().split())
    #  print(a,b)

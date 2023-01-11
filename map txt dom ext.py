with open("chisla2.txt") as f:
    n = int(f.readline())
    n1 = f.readline()

arr = []
with open("chisla2.txt") as f:
    f1 = open("text.txt", "w")
    for i in range(n + 1):
        if i == 0:
            print(f.readline())
        else:
            # arr.append(f.readline().split())
            a = map(int, f.readline().split())
            b1 = filter(lambda x: x != 0, a)
            b1 = list(b1)
            if b1:
                # print(str(b1.pop()))
                f1.write(str(b1.pop()))
                f1.write("\n")
                # arr.append(a)
            # arr2.append()
# print(arr[1])
# v=arr[1]
# print(str(v))
# int(v)
# string = "".join(v)
# k=int(string)
# print(k*k)
# a,b = map(int,f.readline().split())
#  print(a,b)

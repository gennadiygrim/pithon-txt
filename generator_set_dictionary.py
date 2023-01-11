s = [7, 8, 8, -10, -10]
set_set = {i for i in s}
print(set_set)
print(type(set_set), "tolko raznie znach")

dictionry = {i: i**10 for i in s}
print(dictionry)
print(type(dictionry), "tolko raznie kluci")

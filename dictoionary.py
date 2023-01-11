slovart = {"Ybluko": "krasnie", "limon": "krasnie", "Banan": "zolty"}
for k in slovart.keys():
    print(k)


for k in slovart.values():
    print(k)

print(" ------- ")
for k in slovart.items():
    print(k)
slovart["Ybluko"] = "зелений"
print(" ------- ")
for k in slovart.items():
    print(k)
del slovart["Ybluko"]
print(" ------- ")
for k in slovart.items():
    print(k)

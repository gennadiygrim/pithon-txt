import re
s = "87+76845798654    ---- kkjrytgmhhhrhggd8urj888ht5uujh58788789765"
result = re.search(r"r..g", s)
print(result,"..")
result1 = re.search(r"r.g", s)
print(result1,".")
result2 = re.search(r"\d", s)
print(result2,"\d")
result3 = re.search(r"\d\d\d\d", s)
print(result3,"\d\d\d\d")
result4 = re.search(r"\D", s)
print(result4,"\D")
result5 = re.search(r"\s", s)
print(result5,"\s")
result6 = re.search(r"\S", s)
print(result6,"\S")
result7 = re.search(r"\bkkj", s)
print(result7,"\bkkj")
result8 = re.search(r"\Bkkj", s)
print(result8,"\Bkkj")
result9 = re.search(r"\d*", s)
print(result9,"\d*")
result10 = re.search(r"\d+", s)
print(result10,"\d+")
result11 = re.search(r"[ffdddgfgf]", s)
print(result11,"\[ffdddgfgf]")




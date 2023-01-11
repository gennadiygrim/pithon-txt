import re

s = "87+76845798654    ---- kkjrytgmhHhhrhggd8urj888ht5uujh58788789765"
result11 = re.search(r"[ffdddgfgf]", s)
print(result11, "\[ffdddgfgf]")
result13 = re.search(r"[4-6]", s)
print(result13, "\[4-6]")
result14 = re.search(r"[^4-6]", s)
print(result14, "\[^4-6]")
result15 = re.search(r"H|F", s)
print(result15, "H|F")
result16 = re.search(r"\d{3}", s)
print(result16, "\d{3}", s)
result17 = re.search(r"\d{1,3}", s)
print(result17, "\d{1,3}", s)
result18 = re.search(r"\d{4,}", s)
print(result18, "\d{4,}", s)
result19 = re.search(r"\d{,4}", s)
print(result19, "\d{,4}", s)

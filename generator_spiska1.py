s=[]
for i in range(1,21):
    for j in range(1,51):
         s.append((i,j))
print(s)
print("--------------------------------------------")
s1=[(i,j) for i in range(1,21) for j in range(1,51)]
print(s1, " easy spisok")
 
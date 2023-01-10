s=[]
for i in range(1,21):
     if (i%2==0):
         s.append(i)
print(s)

s1=[i for i in range(1,21) if i%2==0]
print(s1, " easy spisok") 

print([i**3 for i in range(1,21) if i%2==0], "kub")
print([i*3 for i in range(1,21) if i%2==0], "mnoz na 3")
print(sum([i**3 for i in range(1,21) if i%2==0]), " sum kub")
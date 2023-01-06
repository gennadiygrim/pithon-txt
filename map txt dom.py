

with open('chisla2.txt') as f:
     n = int(f.readline())
     n1 = f.readline()
     print(n)
     print(n1)
arr=[]   
with open('chisla2.txt') as f:     
  for i  in range (n+1):
    if (i==0):
      print(f.readline())
    else:
     #arr.append(f.readline().split())
     a = map(int,(f.readline().split()))
     arr.append(filter(lambda x: x%2!=0,a))
     
     #print(list(b1))
      #arr.append(a)
     # arr2.append()

#b1=filter(lambda x: x%2!=0,a)
print((arr[9]))
print()
#dd=list(b1)
#for i  in range(20):
# print(dd.index(8))     

#v=arr[1]
#print(str(v))
#int(v)
#string = "".join(str(arr[9]))
#k=int(string)    
#print(k)
    #a,b = map(int,f.readline().split())
#print(string)




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
     arr.append(f.readline())
     
a = map(int,arr)
a = list(a)
print(a)
     #print(list(a),"map")
    # b1=filter(lambda x: x%2!=0,a)
    # print(b1,"b1")
     #print(list(b1),"list-filter")
     #f1=list(b1)
    # print(f1,"f1")
     #print(str(list(b1)),'str-list')
    # arr.append(list(b1))
           #arr.append(a)
     # arr2.append()
#print(list(b1),"uuuuu" )
for i in range(len(arr)):
 print(arr[i],"+++++")
 #print(b1)
 #print(list(b1))
#int(v)
 string = "".join(arr[i])
 k=int(string)    
 print(k*k)
    #a,b = map(int,f.readline().split())
   #  print(a,b)
   # 
print(string,"yyyy")


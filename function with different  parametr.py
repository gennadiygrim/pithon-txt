def suma(a,b,c):
    print (a+b+c)
    
suma(4,5,5) 

def suma1(a,b,c=5):
    print (a+b+c) 
     
suma1(4,3)

def suma2(a=4,b=5,c=5):
    print (a+b+c) 
     
suma2()

def suma3(a=4,b=5,c=5):
    print (a+b+c) 
suma3(4,6)

def suma4(a=4,b=5,c=5):
    print (a+b+c) 
suma4(c=7,b=8)

def suma5(a,b=5,c=5):
    print (a+b+c) 
suma5(4,c=7,b=8)
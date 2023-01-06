def suma(**brand):
    print (type(brand))
    print (brand)


suma(a=3,b=5,c=6,d=7,e=9,f=9) 
suma(a="Apele",s="Samsung")   

def suma_modif(**brand):
    for x,y in brand.items():
     print (x," : ",y)
    
print("suma_modif")
suma_modif(a="Apele",s="Samsung") 
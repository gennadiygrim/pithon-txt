class House():
    """Opisanie Doma"""
    def __init__(self,street,number):
        self.street=street;
        self.number=number;
        self.adge=0
    """Strit Dom"""
    def build(self):
        print(str(self.number)+" gfhfhfghgf "+self.street)
    def adge_of_hause(self,yare):
        self.adge+=yare;
    

House1 = House("fsfsdfsdf",5);
House2 = House("fsfsdfsdf1",53);

print(House1.street)
print(House1.number)

print(House2.street)
print(House2.number)
print(House2.adge)

House2.build();
House2.adge_of_hause(5)
print(House2.adge)







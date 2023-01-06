class House():
    """Opisanie Doma"""

    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.adge = 0

    """Strit Dom"""

    def build(self):
        print(str(self.number) + " gfhfhfghgf " + self.street)

    def adge_of_hause(self, yare):
        self.adge += yare


class ProspectHouse(House):

    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect


PrHouse = ProspectHouse("Madddsxx", 34)

print(PrHouse.prospect)

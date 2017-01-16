class Address:

    def __init__(self, index, town, street, house, office):
        self.index = index
        self.town = town
        self.street = street
        self.house = house
        self.office = office

    def changeindex(self, value):
        self.index = value

    def changetown(self, value):
        self.town = value

    def changestreet(self, value):
        self.street = value

    def changehouse(self, value):
        self.house = value

    def changeoffice(self, value):
        self.office = value

    def __del__(self):
        del self
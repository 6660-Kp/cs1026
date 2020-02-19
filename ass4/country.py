""""
Name: xinhe xia
ASSIGNMENT 4
"""
class Country():

# Constructor
    def __init__(self, name, pop, area, continent):
        self.name = name
        self.pop = pop
        self.area = area
        self.continent = continent

#Getter Methods
    def getName(self):
        return self.name
    def getPopulation(self):
        return self.pop
    def getArea(self):
        return self.area
    def getContinent(self):
        return self.continent

#Setter Methods
    def setPopulation(self, pop):
        self.pop = pop
    def setArea(self, area):
        self.area = area
    def setContinent(self, continent):
        self.continent = continent

#This calculates and returns the population density for the country.
    def getPopDensity(self):
        popd = float(str(self.pop).replace(',', ''))/float(str(self.area).replace(',', ''))
        return round(popd, 2)

#generates a string representation for class objects.  
    def __repr__(self):
        return (self.name + "(pop: " + str(self.pop) + ", size: " + str(self.area) + ") in " + self.continent)



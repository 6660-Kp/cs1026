""""
Name: xinhe xia
ASSIGNMENT 4
"""
from country import Country

#Constructing
class CountryCatalogue:

    #Use two files and instance variables for both the continent
    def __init__(self, file1, file2):
        self._cDictionary = {}
        infile = open(file1, "r")
        #loop through continent
        for line in infile:
            with open('continent.txt') as x:
                next(x)
                for line in x:
                    line = line.strip()                                 #separate
                    splitline = line.split(",")                         #splitline by ,
                    self._cDictionary[splitline[0]] = splitline[1]      #appending to cDictionary
        infile.close()

        self._countryCat = {}
        infile2 = open(file2, "r")

        for line in infile2:
            with open("data.txt") as t:
                next(t)
                for line in t:
                    area = float(line.split("|")[2].replace(",", "").strip())   #splitline by | then replace with ,
                    pop = int(line.split("|")[1].replace(",", ""))
                    name = line.split("|")[0]
                    continent = self._cDictionary[name]
                    self._countryCat[name] = Country(name, pop, area, continent)
        infile2.close()

    def findCountry(self, name):                                               #This method allows a user to look up information on countries
        if name in self._countryCat:
            return self._countryCat[name]
        else:
            return None

#This method will take as parameters a country name and new population
#and then set the population of the country (if it is in the catalogue) to the value
    def setPopulationOfCountry(self, name, newPopulation):
        if name in self._countryCat:
            self._countryCat[name].setPopulation(newPopulation)
            return True
        else:
            return False

#This method will take as parameters a country name and a new area and then
#set the area of the country (if it is in the catalogue) to the value
    def setAreaOfCountry(self, name, newArea):
        if name in self._countryCat:
            self._countryCat[name].setArea = float(newArea)
            return True
        else:
            return False

#This method provides a way to add a new country to the dictionary of countries and country catalogue.
    def addCountry(self, name, pop, area, continent):
        if name in self._countryCat:
            return False
        else:
            self._cDictionary[name] = continent
            self._countryCat[name] = Country(name, pop, area, continent)
            return True
#This method will take as parameter a country name and then if this country exists
#then it should be deleted from the catalogue and from cDictionary.
    def deleteCountry(self, name):
        if name in self._countryCat:
            self._countryCat.pop(name)
            self._cDictionary.pop(name)
        return True
#This method displays the whole catalogue to the screen, using the default
#string representation for the Country objects.
    def printCountryCatalogue(self):
        for key in self._countryCat:
            print(self._countryCat[key].__repr__())
#This method will return a list of countries on a specific continent
    def getCountriesByContinent(self, continent):

        if continent in set(self._cDictionary.values()):
            concounl = []
            for key in self._cDictionary:
                if self._cDictionary[key] == continent:
                    concounl.append(key)
            return concounl
        else:
            return []

    #This method will return a list of pairs (tuples) where a pair is a country name and its population. 
    def getCountriesByPopulation(self, continent):

        countriesl = list(self._countryCat.values())

        for i in range(len(countriesl) - 1):
            for j in range(i + 1, len(countriesl)):
                if countriesl[i].getPopulation() < countriesl[j].getPopulation():
                    p = countriesl[j]
                    countriesl[j] = countriesl[i]
                    countriesl[i] = p

        #Will returned if there is no continent
        if continent == "":
            result = []
            for i in range(len(countriesl)):
                result.append((countriesl[i].getName(), countriesl[i].getPopulation()))
            return result

        #The values will be left if there is a continent
        elif continent in set(self._cDictionary.values()):
            result = []

            #The following code checks if the country object name is the same as the continent
            for i in range(len(countriesl)):
                if countriesl[i].getContinent() == continent: # Only append if they match.
                    result.append((countriesl[i].getName(), countriesl[i].getPopulation()))
            return result

    def getCountriesByArea(self, continent):
        countriesl = list(self._countryCat.values())
        for i in range(len(countriesl) - 1):
            for j in range(i + 1, len(countriesl)):
                if countriesl[i].getArea() < countriesl[j].getArea():
                    p = countriesl[j]
                    countriesl[j] = countriesl[i]
                    countriesl[i] = p
        if continent == "":
            result = []
            for i in range(len(countriesl)):
                result.append((countriesl[i].getName(), countriesl[i].getArea()))
            return result
        elif continent in set(self._cDictionary.values()):
            result = []
            for i in range(len(countriesl)):
                if countriesl[i].getContinent() == continent:
                    result.append((countriesl[i].getName(), countriesl[i].getArea()))
            return result
        else:
            return []

    #This method will find and return the name of the continent with
    #the most number of people living in it  and the number of people living in the continent.
    def findMostPopulousContinent(self):
        countriesl = list(self._countryCat.values())
        conSet = set(list(self._cDictionary.values()))
        mostPopCon = ""#***
        highestPop = 0

        #check for the same continent
        for continentName in conSet:
            conPop = 0
            for i in range(len(countriesl)):
                if countriesl[i].getContinent() == continentName:
                    conPop = conPop + countriesl[i].getPopulation() #country's population will be added to the total continent population

            if conPop > highestPop:
                highestPop = conPop
                mostPopCon = continentName
        return (mostPopCon, highestPop)

    #The following code will return a list of tuples in terms of population density from high to low between the bounds
    def filterCountriesByPopDensity(self, lowerBound, upperBound):
        countriesl = list(self._countryCat.values())
        for i in range(len(countriesl) - 1):
            for j in range(i + 1, len(countriesl)):
                if countriesl[i].getPopDensity() < countriesl[j].getPopDensity():
                    p = countriesl[j]
                    countriesl[j] = countriesl[i]
                    countriesl[i] = p
        result = []

        for i in range(len(countriesl)):
            if lowerBound <= countriesl[i].getPopDensity() <= upperBound:
                result.append((countriesl[i].getName(), countriesl[i].getPopDensity()))
        return result

    def saveCountryCatalogue(self, fileName):
        try:
            outfile = open(fileName, "w")       #write the country catalogue to a new file
            countrynl = sorted(self._countryCat.keys())
            countryol = []
            for countryName in countrynl:
                countryol.append(self._countryCat[countryName]) # sorted country objects list is made.

            countries = ""
            for i in range(len(countryol)-1):
                countries = countries + (countryol[i].getName() + "|" + countryol[i]
                    .getContinent() + "|" + "{}".format(countryol[i].getPopulation()) + "|" + "{}".format
                    (countryol[i].getArea())+ "|" + "{}\n".format(round(countryol[i]
                    .getPopDensity(), 2)))
            outfile.write(countries)

            return len(countryol)       #returns the number of countries
        except Exception:
            return -1
        finally:
            outfile.close()

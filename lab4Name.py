from lab4Database import Database

class Name:

    # Properties of the Name Class
    __name = ""
    __year = 0
    __gender = ""
    __count = 0

    #constructor
    def __init__(self, name, year, gender, count):
        self.__name = name
        self.__year = year
        self.__gender = gender
        self.__count = count

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def gender(self):
        return self.__gender

    @property
    def count(self):
        return self.__count

    #setters for each property

    @name.setter
    def name(self,newName):
        self.__name = newName

    @year.setter
    def year(self, newYear):
        self.__year = newYear

    @gender.setter
    def gender(self, newGender):
        self.__gender = newGender

    @count.setter
    def count(self, newCount):
        self.__count = newCount

    #static method called readNames() which calls Database.readNames()
    # and returns its results
    @staticmethod
    def readNames(year, gender):

        #get a list of "Dictionary Object" from the Databse
        lstNames = Database.readNames(year, gender)

        lstReturn = []

        for n in lstNames:
            #for each dictionary object, create an actual Name object
            objNewName = Name(n["Name"],n["Year"],n["Gender"],n["Count"])

            #add the Name Object to our list that we are gonna sent to UI
            lstReturn.append(objNewName)

        return lstReturn


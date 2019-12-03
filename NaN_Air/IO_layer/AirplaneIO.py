import csv
import collections

FILENAME = "../DataFiles/airplane.csv"


def readFile():
    returnList = []
    with open(FILENAME, encoding="utf8") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=",")
        for line in csvReader:
            returnList.append(line)
    return returnList


def writeToFile(list):
    """takes in a list and creates a new row in the airplane.csv file"""
    with open(FILENAME, "a", encoding="utf8", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(list)


def updateRow():
    pass



class OnLoad:
    """Load this class on load to create all rows as a instance variable inside 1 list"""

    def __init__(self):
        fileData = readFile()
        self.__objectList = []
        for object in fileData:
            self.__objectList.append(object)

    def __str__(self):
        """Prints all lines in a formatted way."""
        returnList = []
        for i in self.__objectList:
            for key, value in i.items():
                returnList.append((key + ": " + value))
            returnList.append("\n")
        return "\n".join(returnList)

    def getAirplaneInstance(self):
        """Takes in a list of all objects and the id to find.
            Returns the object with the id that matches"""
        pass
        # á þetta heima í LL?

    def newAirplane(self, list):
        """Takes in a list with all parameters required in airplane.csv (except id) and writes it to the list"""
        print(self.__objectList)
        newID = self.getHighestID()
        newID = str(newID)
        orderedDict = collections.OrderedDict()
        orderedDict["Airplane ID"] = newID
        orderedDict["Plane reg"] = list[0]
        orderedDict["Manufacturer"] = list[1]
        orderedDict["Model"] = list[2]
        orderedDict["Status"] = list[3]
        orderedDict["Number of seats"] = list[4]
        orderedDict["Odometer"] = list[5]
        self.__objectList.append(orderedDict)
        list.insert(0, newID)

        writeToFile(list)
        print(self.__objectList)
    def getHighestID(self):
        highestID = 0
        for dictionary in self.__objectList:
            for key, value in dictionary.items():
                if key == "Airplane ID":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def UpdateAirplaneInstance(self):
        """Takes in a ID of a plane, and all parameters"""
        pass



# main for testing
createInstanceVariable = OnLoad()

# add new row to csv
toAdd = ["BA1234", "Boeing", "123", "Grounded", "120", "0"]

createInstanceVariable.newAirplane(toAdd)
print(createInstanceVariable)


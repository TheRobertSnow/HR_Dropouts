import csv
import collections

FILENAME = "./DataFiles/airplane.csv"

FIELDNAMES = ["airplane id", "plane reg", "manufacturer", "model", "status", "number of seats",
              "odometer"]  # for update row


# if more fieldnames are added, they also have to be added to the newAirplane method along with the FIELDNAMES constant.
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


def updateRow(objectList):
    """Rewrites the whole csv file with the new and updated object list"""
    with open(FILENAME, "w", encoding="utf8", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(FIELDNAMES)
        for dictionary in objectList:
            writeList = []
            for value in dictionary.values():
                writeList.append(value)
            csvWriter.writerow(writeList)


class OnLoad:
    """Load this class on load to create all rows as a instance variable inside 1 list"""

    def __init__(self):
        self.__objectList = []
        fileData = readFile()
        for object in fileData:
            self.__objectList.append(object)

    def returnObjectList(self):
        return self.__objectList

    def __str__(self):
        """Prints all lines in a formatted way."""
        returnList = []
        for i in self.__objectList:
            for key, value in i.items():
                returnList.append((key + ": " + value))
            returnList.append("\n")
        return "\n".join(returnList)

    def newAirplane(self, dict, list):
        """takes in a dictionary and a lsit with all required fields for the airplane.csv format,
            returns the new plane in a list and a string with the outcome"""
        self.__objectList.append(dict)
        writeToFile(list)
        return list, "Plane added successfully"

    def getHighestID(self):
        """Finds the current highest ID in the airplane.csv and returns a new higher ID"""
        highestID = 0
        print(self.__objectList)
        for dictionary in self.__objectList:
            for key, value in dictionary.items():
                if key == "airplane id":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def checkIfRegExists(self, objectList, register):
        """takes in the object list and compares it to a register, returns True if the register exists"""
        for dictionary in objectList:
            for key, value in dictionary.items():
                if key == "plane reg":
                    if value == register:
                        return True
        return False

    def updateAirplaneInstance(self, aList):
        """Takes in a list with register of a plane, key and new value
            example list = ["BA0345", "status", "Broken"]
            Returns a string with a outcome"""

        indexValue = 0
        valueExists = False
        for count, dictionary in enumerate(self.__objectList):
            for key, value in dictionary.items():
                if key == "plane reg":
                    if value == aList[0]:
                        indexValue = count
                        valueExists = True
        if valueExists:
            self.__objectList[indexValue][aList[1]] = aList[2]
            updateRow(self.__objectList)
            return "Plane updated"
        else:
            return "plane register does not exist."

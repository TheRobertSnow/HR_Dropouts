import csv

FILENAME = "DataFiles/airplane.csv"

class AirplaneIO():

    def __init__(self):
        self.__dictList = []
        self.__airplaneList = []
        self.get_airplanes_from_file()
        self.create_airplane_instances()

    def get_airplanes(self):
        """Return a list of worker instances"""
        return self.__workerList

    def get_airplanes_from_file(self):
        """Get airplanes from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList

    def write_airplane_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict(aList)
            self.__dictList.append(orderedDict)
            newList = []
            newList.append(orderedDict['Plane registration'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Plane registration'
                        ,'Manufacturer'
                        ,'Model'
                        ,'Status'
                        ,'Seats'
                        ,'Odometer']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in self.__dictList:
                writer.writerow(dictionary)

    def convert_to_dict(self, aList):
        """Function converts list to dict"""
        orderedDict = {}
        orderedDict['Plane registration'] = aList[0]
        orderedDict['Manufacturer'] = aList[1]
        orderedDict['Model'] = aList[2]
        orderedDict['Status'] = aList[3]
        orderedDict['Seats'] = aList[4]
        orderedDict['Odometer'] = aList[5]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Plane registration':
                    if value == aList[0]:
                        self.__dictList[index][aList[1]] = aList[2]
                        self.write_dictList_to_file()
                        self.get_airplanes_from_file()
                        self.create_airplane_instances()

    def create_airplane_instances(self):
        """Methood runs through list of dictionaries,
        creates an instance of worker and appends to the list."""
        self.__workerList = []
        for dictionary in self.__dictList:
            worker = Worker(dictionary)
            self.__workerList.append(worker)


class Worker():
    def __init__(self, dictionary):
        self.myDictionary = dictionary
        self.planeRegistration = dictionary['Plane registration']
        self.manufacturer = dictionary['Manufacturer']
        self.model = dictionary["Model"]
        self.status = dictionary["Status"]
        self.seats = dictionary["Seats"]
        self.odometer = dictionary["Odometer"]


    def __str__(self):
        returnString = []
        for key, val in self.myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

# +++++++++++ Test Case +++++++++++++++
writeList = ['TF-EPG','Fokker','F100','Grounded','110','0']
updateList = ['TF-EPG', 'Status', 'Homosexual']
airplane = AirplaneIO()
# # print(newline)
airplane.write_airplane_to_file(writeList)
airplane.update_data_in_file(updateList)




# FIELDNAMES = ['Plane registration','Manufacturer','Model','Status','Seats','Odometer']  # for update row
#
#
# # if more fieldnames are added, they also have to be added to the newAirplane method along with the FIELDNAMES constant.
# def readFile():
#     returnList = []
#     with open(FILENAME, encoding="utf8") as csvFile:
#         csvReader = csv.DictReader(csvFile, delimiter=",")
#         for line in csvReader:
#             returnList.append(line)
#     return returnList
#
#
# def writeToFile(myList):
#     """takes in a list and creates a new row in the airplane.csv file"""
#     with open(FILENAME, "a", encoding="utf8", newline="") as csvFile:
#         csvWriter = csv.writer(csvFile)
#         csvWriter.writerow(myList)
#
#
# def updateRow(objectList):
#     """Rewrites the whole csv file with the new and updated object list"""
#     with open(FILENAME, "w", encoding="utf8", newline="") as csvFile:
#         csvWriter = csv.writer(csvFile)
#         csvWriter.writerow(FIELDNAMES)
#         for dictionary in objectList:
#             writeList = []
#             for value in dictionary.values():
#                 writeList.append(value)
#             csvWriter.writerow(writeList)
#
#
# class OnLoad:
#     """Load this class on load to create all rows as a instance variable inside 1 list"""
#     def __init__(self):
#         self.__objectList = []
#         fileData = readFile()
#         for object in fileData:
#             self.__objectList.append(object)
#
#     def returnObjectList(self):
#         return self.__objectList
#
#     def __str__(self):
#         """Prints all lines in a formatted way."""
#         returnList = []
#         for i in self.__objectList:
#             for key, value in i.items():
#                 returnList.append((key + ": " + value))
#             returnList.append("\n")
#         return "\n".join(returnList)
#
#     def newAirplane(self, newPlaneDict, newPlaneList):
#         """takes in a dictionary and a lsit with all required fields for the airplane.csv format,
#             returns the new plane in a list and a string with the outcome"""
#         self.__objectList.append(newPlaneDict)
#         writeToFile(newPlaneList)
#         return newPlaneList, "Plane added successfully"
#
#     def getHighestID(self):
#         """Finds the current highest ID in the airplane.csv and returns a new higher ID"""
#         highestID = 0
#         print(self.__objectList)
#         for dictionary in self.__objectList:
#             for key, value in dictionary.items():
#                 if key == "airplane id":
#                     if int(value) > highestID:
#                         highestID = int(value)
#         return highestID + 1
#
#     def checkIfRegExists(self, objectList, register):
#         """takes in the object list and compares it to a register, returns True if the register exists"""
#         for dictionary in objectList:
#             for key, value in dictionary.items():
#                 if key == "plane reg":
#                     if value == register:
#                         return True
#         return False
#
#     def updateAirplaneInstance(self, aList):
#         """Takes in a list with register of a plane, key and new value
#             example list = ["BA0345", "status", "Broken"]
#             Returns a string with a outcome"""
#
#         indexValue = 0
#         valueExists = False
#         for count, dictionary in enumerate(self.__objectList):
#             for key, value in dictionary.items():
#                 if key == "plane reg":
#                     if value == aList[0]:
#                         indexValue = count
#                         valueExists = True
#         if valueExists:
#             self.__objectList[indexValue][aList[1]] = aList[2]
#             updateRow(self.__objectList)
#             return "Plane updated"
#         else:
#             return "plane register does not exist."

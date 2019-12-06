import csv
import sys
FILENAME = 'DataFiles/worker.csv'
fieldnames = ['Social Security Number', 'Name', 'Position', 'Plane License', 'Address', 'Phone', 'Cellphone', 'Email', 'Active', 'Available']


class WorkerIO():

    def __init__(self):
        self.__objectList = []
        fileData = WorkerIO.readFile()
        for object in fileData:
            self.__objectList.append(object)
    
    def returnObjectList(self):
        return self.__objectList
    
    def readFile():
        returnList = []
        with open(FILENAME, encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=",")
            for line in csvReader:
                returnList.append(line)
        return returnList

    """def get_worker_from_file(self):
        Get workers from file in a list of dictionaries
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            for line in csvReader:
                returnList.append(line)
        return returnList"""


    def write_worker_to_file(self, objectDict, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            #orderedDict = self.convert_to_dict(aList)
            self.__objectList.append(objectDict)
            newList = []
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)
        return aList, "Worker successfully created!"

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in self.__dictList:
                writer.writerow(dictionary)

    def convert_to_dict(self, aList):
        """Function converts list to dict"""
        orderedDict = {}
        orderedDict['Social Security Number'] = aList[0]
        orderedDict['Name'] = aList[1]
        orderedDict['Position'] = aList[2]
        orderedDict['Plane License'] = aList[3]
        orderedDict['Address'] = aList[4]
        orderedDict['Phone'] = aList[5]
        orderedDict['Cellphone'] = aList[6]
        orderedDict['Email'] = aList[7]
        orderedDict['Active'] = aList[8]
        orderedDict['Available'] = aList[9]
        return orderedDict   

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Social Security Number':
                    if value == aList[0]:
                        self.__dictList[index][aList[1]] = aList[2]
                        self.write_dictList_to_file()

    def updateWorker(self, aList):
        """Takes in a list with SSN of a worker, key and new value
        example list = ["2607962249", "position", "pilot"]
        Returns a string with a outcome"""

        indexValue = 0
        valueExists = False
        for count, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == "Social Security Number":
                    if value == aList[0]:
                        indexValue = count
                        valueExists = True
        if valueExists:
            self[indexValue][aList[1]] = aList[2]
            write_dictList_to_file(self)
            return "Worker updated"
        else:
            return "Worker does not exist"
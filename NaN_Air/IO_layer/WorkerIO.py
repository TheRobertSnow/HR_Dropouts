import csv
import sys, os
FILENAME = '../DataFiles/worker.csv'


class Worker():

    def __init__(self):
        self.__dictList = []

    def get_worker_from_file(self):
        """Get worker from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList
        return self.__dictList

    def write_worker_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict(aList)
            self.__dictList.append(orderedDict)
            newList = []
            #newList.append(orderedDict['social security number']) BÆTIR VIÐ SSN FREMST???
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['social security number'
                        ,'name'
                        ,'position'
                        ,'rank'
                        ,'plane licence'
                        ,'address'
                        ,'phone'
                        ,'cellphone'
                        ,'email'
                        ,'active'
                        ,'available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in self.__dictList:
                writer.writerow(dictionary)

    def convert_to_dict(self, aList):
        """Function converts list to dict"""
        orderedDict = {}
        orderedDict['social security number'] = aList[0]
        orderedDict['name'] = aList[1]
        orderedDict['position'] = aList[2]
        orderedDict['rank'] = aList[3]
        orderedDict['plane licence'] = aList[4]
        orderedDict['address'] = aList[5]
        orderedDict['phone'] = aList[6]
        orderedDict['cellphone'] = aList[7]
        orderedDict['email'] = aList[8]
        orderedDict['active'] = aList[9]
        orderedDict['available'] = aList[10]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'social security number':
                    if value == aList[0]:
                        self.__dictList[index][aList[1]] = aList[2]
                        self.write_dictList_to_file()


writeList = ["9999999999","Elizabeth Mcfadden","Cabincrew","Flight Attendant","N/A","Fellsmúli 35","8998835","8998835","test@test.com","True","True"]
updateList = ['9999999999', 'position', 'Dick']
worker = Worker()

worker.get_worker_from_file()

worker.write_worker_to_file(writeList)
worker.update_data_in_file(updateList)
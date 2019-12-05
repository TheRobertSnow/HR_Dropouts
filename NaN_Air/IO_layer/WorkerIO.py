import csv
FILENAME = '../DataFiles/worker.csv'


class WorkerIO():

    def __init__(self):
        self.get_workers_from_file()
        self.create_worker_instances()

    def get_workers_from_file(self):
        """Get worker from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList

    def write_worker_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            newList = []
            newList.append(orderedDict['Worker ID'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Worker ID'
                        ,'Social security number'
                        ,'Name'
                        ,'Position'
                        ,'Rank'
                        ,'Plane licence'
                        ,'Address'
                        ,'Phone'
                        ,'Cellphone'
                        ,'Email'
                        ,'Active'
                        ,'Available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in self.__dictList:
                writer.writerow(dictionary)

    def getHighestID(self):
        """This method is only used by 'add_dict_to_list'.
        Returns the next id that is to be assigned."""
        highestID = 0
        for dictionary in self.__dictList:
            for key, value in dictionary.items():
                if key == "Worker ID":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def convert_to_dict_with_id(self, aList):
        """Function takes in a list of arguments,
        generates an ID, adds ID to a dictionary and then adds
        everyting from list to the dictionary."""
        orderedDict, newID = {}, self.getHighestID()
        orderedDict['Worker ID'] = newID
        orderedDict['Social security number'] = aList[0]
        orderedDict['Name'] = aList[1]
        orderedDict['Position'] = aList[2]
        orderedDict['Rank'] = aList[3]
        orderedDict['Plane licence'] = aList[4]
        orderedDict['Address'] = aList[5]
        orderedDict['Phone'] = aList[6]
        orderedDict['Cellphone'] = aList[7]
        orderedDict['Email'] = aList[8]
        orderedDict['Active'] = aList[9]
        orderedDict['Available'] = aList[10]
        return orderedDict

    def convert_to_dict(self, aList):
        """Function converts list to dict"""
        orderedDict = {}
        orderedDict['Worker ID'] = aList[0]
        orderedDict['Social security number'] = aList[1]
        orderedDict['Name'] = aList[2]
        orderedDict['Position'] = aList[3]
        orderedDict['Rank'] = aList[4]
        orderedDict['Plane licence'] = aList[5]
        orderedDict['Address'] = aList[6]
        orderedDict['Phone'] = aList[7]
        orderedDict['Cellphone'] = aList[8]
        orderedDict['Email'] = aList[9]
        orderedDict['Active'] = aList[10]
        orderedDict['Available'] = aList[11]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Worker ID':
                    if value == aList[0]:
                        self.__dictList[index][aList[1]] = aList[2]
                        self.write_dictList_to_file()

    def create_worker_instances(self):
        self.__workerList = []
        for dictionary in self.__dictList:
            worker = Worker(dictionary)
            self.__workerList.append(worker)
        print(self.__workerList)


class Worker():
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.__workerID = dictionary['Worker ID']
        self.__socialSecurityNumber = dictionary['Social security number']
        self.__name = dictionary["Name"]
        self.__position = dictionary["Position"]
        self.__rank = dictionary["Rank"]
        self.__planeLicence = dictionary["Plane licence"]
        self.__address = dictionary["Address"]
        self.__phone = dictionary["Phone"]
        self.__cellphone = dictionary["Cellphone"]
        self.__email = dictionary["Email"]
        self.__active = dictionary["Active"]
        self.__available = dictionary["Available"]


    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

writeList = ['35','1107951952','Elizabeth Mcfadden','Cabincrew','Flight Attendant','N/A','Fellsmúli 35','8998835','8998835','test@test.com','True','True']
updateList = ['35', 'Position', 'Looser']
worker = WorkerIO()
# print(newline)
worker.write_worker_to_file(writeList)
worker.update_data_in_file(updateList)

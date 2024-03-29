import csv
FILENAME = 'DataFiles/worker.csv'
FIELDNAMES = ['Social Security Number', 'Name', 'Position', 'Plane License', 'Address', 'Phone', 'Cellphone', 'Email', 'Active', 'Available']

class WorkerIO():

    def __init__(self):
        self.__dictList = []
        self.workerList = []
        self.get_workers_from_file()
        self.create_worker_instances()

    def get_workers(self):
        """Return a list of worker instances"""
        self.get_workers_from_file()
        self.create_worker_instances()
        return self.workerList

    def get_workers_from_file(self):
        """Only use for initializing WorkerIO.
        Get workers from file in a list of dictionaries"""
        dictList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            for line in csvReader:
                dictList.append(line)
        self.__dictList = dictList
        self.workerList = []
        for dictionary in self.__dictList:
            worker = Worker(dictionary)
            self.workerList.append(worker)

    def write_worker_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            workerInstance = self.add_worker_instance(orderedDict)
            newList = []
            newList.append(orderedDict['Worker ID'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)
        return workerInstance

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Worker ID'
                        ,'Social security number'
                        ,'Name'
                        ,'Position'
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

    def getNextID(self):
        """This method is only used by 'add_dict_to_list'.
        Returns the next id that is to be assigned."""
        highestID = 0
        # could use self.__dictList.count but what would not work if we allow
        # deleteing.
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
        orderedDict, newID = {}, self.getNextID()
        orderedDict['Worker ID'] = newID
        orderedDict['Social security number'] = aList[0]
        orderedDict['Name'] = aList[1]
        orderedDict['Position'] = aList[2]
        orderedDict['Plane licence'] = aList[3]
        orderedDict['Address'] = aList[4]
        orderedDict['Phone'] = aList[5]
        orderedDict['Cellphone'] = aList[6]
        orderedDict['Email'] = aList[7]
        orderedDict['Active'] = aList[8]
        orderedDict['Available'] = aList[9]
        return orderedDict

    def convert_to_dict(self, aList):
        """Function converts list to dict"""
        orderedDict = {}
        orderedDict['Worker ID'] = aList[0]
        orderedDict['Social security number'] = aList[1]
        orderedDict['Name'] = aList[2]
        orderedDict['Position'] = aList[3]
        orderedDict['Plane licence'] = aList[4]
        orderedDict['Address'] = aList[5]
        orderedDict['Phone'] = aList[6]
        orderedDict['Cellphone'] = aList[7]
        orderedDict['Email'] = aList[8]
        orderedDict['Active'] = aList[9]
        orderedDict['Available'] = aList[10]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        col, val = aList[1], aList[2] # The column of the desired value and the value
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Worker ID':
                    if value == aList[0]:
                        if col != "Worker ID" or col != "Social security number" or col != "Name":
                            self.__dictList[index][col] = val
                            self.write_dictList_to_file()
                            self.get_workers_from_file()
                            self.create_worker_instances()
                            for i in self.__workerList:
                                if i.workerID == aList[0]:
                                    if col == "Position":
                                        i.position = val
                                    elif col == "Plane licence":
                                        i.planeLicence = val
                                    elif col == "Address":
                                        i.address = val
                                    elif col == "Phone":
                                        i.phone = val
                                    elif col == "Cellphone":
                                        i.cellphone = val
                                    elif col == "Email":
                                        i.email = val
                                    elif col == "Active":
                                        i.active = val
                                    elif col == "Available":
                                        i.available = val
                                    return i

    def add_worker_instance(self, dict):
        newWorker = Worker(dict)
        self.workerList.append(newWorker)
        return newWorker

    def create_worker_instances(self):
        """Methood runs through list of dictionaries,
        creates an instance of worker and appends to the list."""
        self.__workerList = []
        for dictionary in self.__dictList:
            worker = Worker(dictionary)
            self.__workerList.append(worker)
        return self.__workerList

    def writeworkertoFile(self, workerList):
        workerInstance = self.write_worker_to_file(workerList)
        return workerInstance

    def updateCertainWorker(self, instance, key, newValue):
        instance.updateValue(key, newValue) 
        self.write_dictList_to_file()  
        return instance 

class Worker():
    def __init__(self, dictionary):
        self.myDictionary = dictionary
        self.workerID = dictionary['Worker ID']
        self.socialSecurityNumber = dictionary['Social security number']
        self.name = dictionary["Name"]
        self.position = dictionary["Position"]
        self.planeLicence = dictionary["Plane licence"]
        self.address = dictionary["Address"]
        self.phone = dictionary["Phone"]
        self.cellphone = dictionary["Cellphone"]
        self.email = dictionary["Email"]
        self.active = dictionary["Active"]
        self.available = dictionary["Available"]

    def updateValue(self, key, newValue):
        self.myDictionary[key] = newValue

    def __str__(self):
        returnString = []
        for key, val in self.myDictionary.items():
            if key != "Active" and key != "Available": #We do not want to print active and available status
                returnString.append((key + ": " + str(val)))
        return "\n".join(returnString)

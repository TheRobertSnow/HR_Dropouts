import csv
FILENAME = 'DataFiles/flight.csv'


class FlightIO():

    def __init__(self):
        self.__dictList = []
        self.flightList = []
        self.get_flights_from_file()
        self.create_flight_instances()

    def get_flights(self):
        """Return a list of flight instances"""
        return self.flightList

    def get_flights_from_file(self):
        """Get flight from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList
        for dictionary in self.__dictList:
            flight = Flight(dictionary)
            self.flightList.append(flight)

    def write_flight_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            newList = []
            newList.append(orderedDict['Flight ID'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Flight ID'
                        ,'Flight number'
                        ,'Airplane registration number'
                        ,'Origin ID'
                        ,'Destination ID'
                        ,'Flight status'
                        ,'Travel time'
                        ,'Departure time'
                        ,'Arrival time']
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
                if key == "Flight ID":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def convert_to_dict_with_id(self, aList):
        """Function takes in a list of arguments,
        generates an ID, adds ID to a dictionary and then adds
        everyting from list to the dictionary."""
        orderedDict, newID = {}, self.getNextID()
        orderedDict['Flight ID'] = newID
        orderedDict['Flight number'] = aList[0]
        orderedDict['Airplane registration number'] = aList[1]
        orderedDict['Origin ID'] = aList[2]
        orderedDict['Destination ID'] = aList[3]
        orderedDict['Flight status'] = aList[4]
        orderedDict['Travel time'] = aList[5]
        orderedDict['Departure time'] = aList[6]
        orderedDict['Arrival time'] = aList[7]
        return orderedDict

    def convert_to_dict(self, aList):
        """Function converts list to dict"""
        orderedDict = {}
        orderedDict['Flight ID'] = aList[0]
        orderedDict['Flight number'] = aList[1]
        orderedDict['Airplane registration number'] = aList[2]
        orderedDict['Origin ID'] = aList[3]
        orderedDict['Destination ID'] = aList[4]
        orderedDict['Flight status'] = aList[5]
        orderedDict['Travel time'] = aList[6]
        orderedDict['Departure time'] = aList[7]
        orderedDict['Arrival time'] = aList[8]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Flight ID':
                    if value == aList[0]:
                        if col != "Flight ID" or col != "Flight number":
                            self.__dictList[index][col] = val
                            self.write_dictList_to_file()
                            self.get_flights_from_file()
                            self.create_flight_instances()
                            for i in self.flightList:
                                if i.flightID == aList[0]:
                                    if col == "Airplane registration number":
                                        i.airplaneRegistrationNumber = val
                                    elif col == "Origin ID":
                                        i.originID = val
                                    elif col == "Destination ID":
                                        i.destinationID = val
                                    elif col == "Flight status":
                                        i.flightStatus = val
                                    elif col == "Travel time":
                                        i.travelTime = val
                                    elif col == "Departure time":
                                        i.departureTime = val
                                    elif col == "Arrival time":
                                        i.arrivalTime = val

    def create_flight_instances(self):
        """Methood runs through list of dictionaries,
        creates an instance of flight and appends to the list."""
        self.flightList = []
        for dictionary in self.__dictList:
            flight = Flight(dictionary)
            self.flightList.append(flight)


class Flight():
    def __init__(self, dictionary):
        self.myDictionary = dictionary
        self.flightID = dictionary['Flight ID']
        self.flightNumber = dictionary['Flight number']
        self.airplaneRegistrationNumber = dictionary["Airplane registration number"]
        self.originID = dictionary["Origin ID"]
        self.destinationID = dictionary["Destination ID"]
        self.flightStatus = dictionary["Flight status"]
        self.travelTime = dictionary["Travel time"]
        self.departureTime = dictionary["Departure time"]
        self.arrivalTime = dictionary["Arrival time"]


    def __str__(self):
        returnString = []
        for key, val in self.myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)


# +++++++++ Test Case ++++++++++++
# writeList = ['35','1107951952','Elizabeth Mcfadden','Cabincrew','Flight Attendant','N/A','Fellsmúli 35','8998835','8998835','test@test.com','True','True']
# updateList = ['35', 'Position', 'Looser']
# worker = WorkerIO()
# # print(newline)
# worker.write_worker_to_file(writeList)
# worker.update_data_in_file(updateList)

import csv
FILENAME = 'DataFiles/voyage.csv'


class VoyageIO:

    def __init__(self, airplaneList, flightList, workerList, flightRouteList):
        self.dictList = []
        self.voyageList = []
        self.get_voyages_from_file()
        self.create_voyage_instances()

    def get_voyages(self):
        """Return a list of voyage instances"""
        return self.voyageList

    def get_voyages_from_file(self):
        """Only use for initializing VoyageIO.
        Get voyages from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList
        for dictionary in self.__dictList:
            voyage = Voyage(dictionary)
            self.voyageList.append(voyage)

    def write_voyage_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            newList = []
            newList.append(orderedDict['Voyage ID'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Voyage ID'
                        ,'Flight out ID'
                        ,'Flight back ID'
                        ,'Main pilot'
                        ,'Assisting pilot'
                        ,'Main flight attendant'
                        ,'Flight attendants'
                        ,'Flight route ID'
                        ,'Departure from IS'
                        ,'Departure to IS']
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
                if key == "Voyage ID":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def convert_to_dict_with_id(self, aList):
        """Function takes in a list of arguments,
        generates an ID, adds ID to a dictionary and then adds
        everyting from list to the dictionary."""
        orderedDict, newID = {}, self.getNextID()
        orderedDict['Voyage ID'] = newID
        orderedDict['Flight out ID'] = aList[0]
        orderedDict['Flight back ID'] = aList[1]
        orderedDict['Main pilot'] = aList[2]
        orderedDict['Assisting pilot'] = aList[3]
        orderedDict['Main flight attendant'] = aList[4]
        orderedDict['Flight attendants'] = aList[5]
        orderedDict['Flight route ID'] = aList[6]
        orderedDict['Departure from IS'] = aList[7]
        orderedDict['Departure to IS'] = aList[8]
        return orderedDict

    def convert_to_dict(self, aList):
        """Function converts list to dict"""
        orderedDict = {}
        orderedDict['Voyage ID'] = aList[0]
        orderedDict['Flight out ID'] = aList[1]
        orderedDict['Flight back ID'] = aList[2]
        orderedDict['Main pilot'] = aList[3]
        orderedDict['Assisting pilot'] = aList[4]
        orderedDict['Main flight attendant'] = aList[5]
        orderedDict['Flight attendants'] = aList[6]
        orderedDict['Flight route ID'] = aList[7]
        orderedDict['Departure from IS'] = aList[8]
        orderedDict['Departure to IS'] = aList[9]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        col, val = aList[1], aList[2] # The column of the desired value and the value
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Voyage ID':
                    if value == aList[0]:
                        if col != "Voyage ID" or col != "Flight out ID" or col != "Flight back ID":
                            self.__dictList[index][col] = val
                            self.write_dictList_to_file()
                            self.get_voyages_from_file()
                            self.create_voyage_instances()
                            for i in self.__workerList:
                                if i.voyageID == aList[0]:
                                    if col == "Main pilot":
                                        i.mainPilot = val
                                    elif col == "Assisting pilot":
                                        i.assistingPilot = val
                                    elif col == "Main flight attendant":
                                        i.mainFlightAttendant = val
                                    elif col == "Flight attendants":
                                        i.flightAttendants = val
                                    elif col == "Flight route ID":
                                        i.flightRouteID = val
                                    elif col == "Departure from IS":
                                        i.departureFromIS = val
                                    elif col == "Departure to IS":
                                        i.departureToIS = val

    def create_voyage_instances(self):
        """Methood runs through list of dictionaries,
        creates an instance of worker and appends to the list."""
        self.__voyageList = []
        for dictionary in self.__dictList:
            voyage = Voyage(dictionary)
            self.__voyageList.append(voyage)

    def createNewVoyage(self, voyageList):
        return "were working on this method"


class Voyage:
    def __init__(self, dictionary):
        self.myDictionary = dictionary
        self.voyageID = dictionary['Voyage ID']
        self.flightOutID = dictionary['Flight out ID']
        self.flightBackID = dictionary["Flight back ID"]
        self.mainPilot = dictionary["Main pilot"]
        self.assistingPilot = dictionary["Assisting pilot"]
        self.mainFlightAttendant = dictionary["Main flight attendant"]
        self.flightAttendants = dictionary["Flight attendants"]
        self.flightRouteID = dictionary["Flight route ID"]
        self.departureFromIS = dictionary["Departure from IS"]
        self.departureToIS = dictionary["Departure to IS"]


    def __str__(self):
        returnString = []
        for key, val in self.myDictionary.items():
            returnString.append((key + ": " + str(val)))
        return "\n".join(returnString)

    def getflightAttendants(self):
        return self.flightAttendants

    def getflightIDS(self):
        return self.flightOutID, self.flightBackID


# writeList = ['35','1107951952','Elizabeth Mcfadden','Cabincrew','Flight Attendant','N/A','Fellsmúli 35','8998835','8998835','test@test.com','True','True']
# updateList = ['35', 'Position', 'Looser']
# worker = WorkerIO()
# # print(newline)
# worker.write_worker_to_file(writeList)
# worker.update_data_in_file(updateList)

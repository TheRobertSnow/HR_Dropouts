import csv
import sys
FILENAME = '../DataFiles/flight.csv'


class FlightIO():

    def __init__(self):
        randvar = self.get_flight_from_file()

    def get_flight_from_file(self):
        """Get flight from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList
        return self.__dictList

    def write_flight_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            newList = []
            newList.append(orderedDict['flight id'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['flight id'
                        ,'flight number'
                        ,'airplane reg'
                        ,'sold seats'
                        ,'flight route id'
                        ,'flight status'
                        ,'travel time'
                        ,'departure time'
                        ,'arrival time']
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
                if key == "flight id":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def convert_to_dict_with_id(self, aList):
        """Function converts list to dict, generates an ID
        and assigns it to the dictionary"""
        orderedDict, newId = {}, self.getHighestID()
        orderedDict['flight id'] = newId
        orderedDict['flight number'] = aList[0]
        orderedDict['airplane reg'] = aList[1]
        orderedDict['sold seats'] = aList[2]
        orderedDict['flight route id'] = aList[3]
        orderedDict['flight status'] = aList[4]
        orderedDict['travel time'] = aList[5]
        orderedDict['departure time'] = aList[6]
        orderedDict['arrival time'] = aList[7]
        return orderedDict

    def convert_to_dict_no_id(self, aList):
        """Function converts list to dict but doesn't
        generate an id since ID should be provided in argument list"""
        orderedDict = {}
        orderedDict['flight id'] = aList[0]
        orderedDict['flight number'] = aList[1]
        orderedDict['airplane reg'] = aList[2]
        orderedDict['sold seats'] = aList[3]
        orderedDict['flight route id'] = aList[4]
        orderedDict['flight status'] = aList[5]
        orderedDict['travel time'] = aList[6]
        orderedDict['departure time'] = aList[7]
        orderedDict['arrival time'] = aList[8]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'flight id':
                    if value == aList[0]:
                        self.__dictList[index][aList[1]] = aList[2]
                        self.write_dictList_to_file()


flight = FlightIO()
newline = ['NA011','T-911','8','1','0002','Boarding','18:35','20:32']
updateline = ["2","flight status", "crashing"]
# print(newline)
flight.write_flight_to_file(newline)
flight.update_data_in_file(updateline)

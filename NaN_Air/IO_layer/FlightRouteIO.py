import csv
import sys
FILENAME = '../DataFiles/flightRoutes.csv'


class FlightRouteIO():

    def __init__(self):
        self.get_flight_route_from_file()

    def get_flight_route_from_file(self):
        """Get flight routes from file in a list of dictionaries"""
        returnList = []
        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # next(csvReader, None)
            for line in csvReader:
                returnList.append(line)
        self.__dictList = returnList

    def write_flight_route_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            newList = []
            newList.append(orderedDict['Flight Route ID'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def getHighestID(self):
        """This method is only used by 'add_dict_to_list'.
        Returns the next id that is to be assigned."""
        highestID = 0
        for dictionary in self.__dictList:
            for key, value in dictionary.items():
                if key == "Flight Route ID":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def convert_to_dict_with_id(self, aList):
        orderedDict, newId = {}, self.getHighestID()
        orderedDict['Flight Route ID'] = newId
        orderedDict['Country'] = aList[0]
        orderedDict['Airport'] = aList[1]
        orderedDict['Flight distance'] = aList[2]
        orderedDict['Travel time'] = aList[3]
        orderedDict['Emergency contact'] = aList[4]
        orderedDict['Emergency number'] = aList[5]
        return orderedDict

    def convert_to_dict_no_id(self, aList):
        orderedDict = {}
        orderedDict['Flight Route ID'] = aList[0]
        orderedDict['Country'] = aList[1]
        orderedDict['Airport'] = aList[2]
        orderedDict['Flight distance'] = aList[3]
        orderedDict['Travel time'] = aList[4]
        orderedDict['Emergency contact'] = aList[5]
        orderedDict['Emergency number'] = aList[6]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data for and updates file"""
        for index, dictionary in enumerate(self.__dictList):
            if self.__dictList[index]['Flight Route ID'] == aList[0]:
                orderedDict = convert_to_dict_no_id(aList)
                self.__dictList[index] = orderedDict
        print(self.__dictList)
            # for key, value in dictionary.items():
            #     if key == aList[0]:
            #
        # for index, item in enumerate(self.__dictList):
        #     if item["Flight Route ID"] == aList[0]:
        #         for itemNum, item in enumerate(self.__dictList[index]):
        #             item == aList[itemNum]
        # with open(FILENAME, 'w', encoding='utf8') as csvFile:
        #     csvWriter = csv.writer(csvFile)
        #     print(type(self.__dictList[0]))
        #     csvWriter.writerow(self.__dictList[0])
        #     for dictionary in self.__dictList:
        #         tempList = []
        #         for value in dictionary.values():
        #             tempList.append(value)
        #         csvWriter.writerow(tempList)


flightroutes = FlightRouteIO()
updateline = [1,"Denmark","Kopenhagen",0,"0:00", "Áslaug Steingrímsdóttir", 3547745010]
newline = ["Denmark","Reykjavik",0,"0:00", "Áslaug Steingrímsdóttir", 3547745010]
# print(newline)
flightroutes.write_flight_route_to_file(newline)
flightroutes.update_data_in_file(updateline)

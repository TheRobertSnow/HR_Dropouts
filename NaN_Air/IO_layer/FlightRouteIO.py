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
        print(self.__dictList)

    def write_flight_route_to_file(self, data):
        """Method takes in list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(data)
            # self.add_dict_to_list(data)


    # def add_dict_to_list(self, aList):
    #     OrderedDict = {}
    #     OrderedDict['Flight Route ID'] = self.__dictList[-1]['Flight Route ID'] + 1
    #     OrderedDict['Country'] = aList[0]
    #     OrderedDict['Airport'] = aList[1]
    #     OrderedDict['Flight distance'] = aList[2]
    #     OrderedDict['Travel time'] = aList[3]
    #     OrderedDict['Emergency contact'] = aList[4]
    #     OrderedDict['Emergency number'] = aList[5]
    #     self.__dictList.append(OrderedDict)

    def update_data_in_file(self, data):
        """Method takes in list of data for and updates file"""
        for index, item in enumerate(self.__dictList):
            if item["Flight Route ID"] == data[0]:
                for itemNum, item in enumerate(self.__dictList[index]):
                    item == data[itemNum]
        with open(FILENAME, 'w', encoding='utf8') as csvFile:
            csvWriter = csv.writer(csvFile)
            print(type(self.__dictList[0]))
            csvWriter.writerow(self.__dictList[0])
            for dictionary in self.__dictList:
                tempList = []
                for value in dictionary.values():
                    tempList.append(value)
                csvWriter.writerow(tempList)


flightroutes = FlightRouteIO()
updateline = [1,"Denmark","Kopenhagen",0,"0:00", "Áslaug Steingrímsdóttir", 3547745010]
newline = [4, "Denmark","Reykjavik",0,"0:00", "Áslaug Steingrímsdóttir", 3547745010]
# print(newline)
flightroutes.write_flight_route_to_file(newline)
flightroutes.update_data_in_file(updateline)

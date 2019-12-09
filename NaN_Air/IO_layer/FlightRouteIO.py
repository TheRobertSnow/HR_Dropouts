import csv
import sys
FILENAME = 'DataFiles/flightRoutes.csv'


class FlightRouteIO():

    def __init__(self):
        self.__dictList = []
        self.flightRouteList = []
        self.get_flight_route_from_file()
        self.create_flight_route_instances()

    def get_flight_routes(self):
        """Return a list of flight instances"""
        return self.flightRouteList

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
            newList.append(orderedDict['Flight route ID'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Flight route ID'
                        ,'Country'
                        ,'Airport'
                        ,'Flight distance'
                        ,'Travel time'
                        ,'Emergency contact'
                        ,'Emergency number']
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
                if key == "Flight route ID":
                    if int(value) > highestID:
                        highestID = int(value)
        return highestID + 1

    def convert_to_dict_with_id(self, aList):
        """Function converts list to dict, generates an ID
        and assigns it to the dictionary"""
        orderedDict, newId = {}, self.getHighestID()
        orderedDict['Flight route ID'] = newId
        orderedDict['Country'] = aList[0]
        orderedDict['Airport'] = aList[1]
        orderedDict['Flight distance'] = aList[2]
        orderedDict['Travel time'] = aList[3]
        orderedDict['Emergency contact'] = aList[4]
        orderedDict['Emergency number'] = aList[5]
        return orderedDict

    def convert_to_dict_no_id(self, aList):
        """Function converts list to dict but doesn't
        generate an id since ID should be provided in argument list"""
        orderedDict = {}
        orderedDict['Flight route ID'] = aList[0]
        orderedDict['Country'] = aList[1]
        orderedDict['Airport'] = aList[2]
        orderedDict['Flight distance'] = aList[3]
        orderedDict['Travel time'] = aList[4]
        orderedDict['Emergency contact'] = aList[5]
        orderedDict['Emergency number'] = aList[6]
        return orderedDict

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Flight route ID':
                    if value == aList[0]:
                        self.__dictList[index][aList[1]] = aList[2]
                        self.write_dictList_to_file()

    def create_flight_route_instances(self):
        """Methood runs through list of dictionaries,
        creates an instance of flight route and appends to the list."""
        self.flightRouteList = []
        for dictionary in self.__dictList:
            flightRoute = FlightRoute(dictionary)
            self.flightRouteList.append(flightRoute)


class FlightRoute:
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.flightRouteID = dictionary["Flight route ID"]
        self.Country = dictionary["Country"]
        self.airport = dictionary["Airport"]
        self.flightDistance = dictionary["Flight distance"]
        self.travelTime = dictionary["Travel time"]
        self.emergencyContact = dictionary["Emergency contact"]
        self.emergencyNumber = dictionary["Emergency number"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

    def __repr__(self):
        return f"< Flight route ID: {self.flightRouteID} \n>"

# +++ Test cases +++
# flightroutes = FlightRouteIO()
# updateline = ["1","Country", "Denmark"]
# newline = ["Denmark","Reykjavik","0","0:00", "Áslaug Steingrímsdóttir", "3547745010"]
# # # print(newline)
# flightroutes.write_flight_route_to_file(newline)
# flightroutes.update_data_in_file(updateline)

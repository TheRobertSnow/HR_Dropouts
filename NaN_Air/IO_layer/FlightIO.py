import csv
# import datetime
FILENAME = 'DataFiles/flight.csv'
from datetime import datetime
from datetime import timedelta

class FlightIO():

    def __init__(self):
        self.__dictList = []
        self.flightList = []
        self.get_flights_from_file()
        self.create_flight_instances()

    def get_flights(self):
        """Return a list of flight instances"""
        return self.flightList

    def automatically_change_flight_status(self):
        now = datetime.now()
        flightStatuses = ["On schedule", "Loading", "In-Air", "Landed", "Cancelled"]
        for flight in self.flightList:
            departureTime = datetime.strptime(flight.departureTime, '%Y-%m-%d %H:%M:%S')
            loadingTimeStart = departureTime - timedelta(minutes = 20)
            inAirTimeStart = departureTime + timedelta(minutes = 10)
            arrivalTime = datetime.strptime(flight.arrivalTime, '%Y-%m-%d %H:%M:%S')
            landedTimeStart = arrivalTime
            if flight.flightStatus != flightStatuses[4]:
                if now < loadingTimeStart:
                    if flight.flightStatus != flightStatuses[0]:
                        self.update_data_in_file([flight.flightNumber, departureTime, "Flight status", flightStatuses[0]])
                elif now >= loadingTimeStart and now < inAirTimeStart:
                    if flight.flightStatus != flightStatuses[1]:
                        self.update_data_in_file([flight.flightNumber, departureTime, "Flight status", flightStatuses[1]])
                elif now >= inAirTimeStart and now < landedTimeStart:
                    if flight.flightStatus != flightStatuses[2]:
                        self.update_data_in_file([flight.flightNumber, departureTime, "Flight status", flightStatuses[2]])
                elif now >= landedTimeStart:
                    if flight.flightStatus != flightStatuses[3]:
                        self.update_data_in_file([flight.flightNumber, departureTime, "Flight status", flightStatuses[3]])

    def get_flights_from_file(self):
        """Only use for initializing FlightIO.
        Get flight from file in a list of dictionaries"""
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
        flightInstance = None
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = self.convert_to_dict_with_id(aList)
            self.__dictList.append(orderedDict)
            flightInstance = self.add_flight_instance(orderedDict)
            newList = []
            newList.append(orderedDict['Flight ID'])
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)
        return flightInstance

    def get_flight_number(self, originID, destinationID, departureTime):
        """Method takes in destinationID and departureTime and generates a
        flight number to return"""
        flightsOnDate = []# List of flights to the same destination on the same date
        #flightsOnDateFrom = []# List of flights from the same destination on the same date
        departureDate = departureTime.date()
        numOfFlight = 0 # The last digit in the flight number
        flightNumber = "NA"
        if int(destinationID) < 10 and int(destinationID) > 1:
            flightNumber = flightNumber + "0" + destinationID
        elif int(destinationID) == 1:
            if int(originID) < 10:
                flightNumber = flightNumber + "0" + originID
            else:
                flightNumber = flightNumber + originID
        else:
            flightNumber = flightNumber + destinationID

        for flight in self.flightList:
            #flightDT = flight.departureTime
            # TODO Need to fix the date check!!!!
            instanceDepartureDate = None
            if type(flight.departureTime) == str:
                date, time = flight.departureTime.split()
                year, month, day = date.split("-")
                hour, min, sec = time.split(":")
                instanceDeparture = datetime(int(year), int(month), int(day), int(hour), int(min), int(sec))
                instanceDepartureDate = instanceDeparture.date()
            else:
                instanceDepartureDate = flight.departureTime.date()
                
            # If the date of the instance matches the given date and destination
            if instanceDepartureDate == departureDate:
                if flight.destinationID == destinationID and flight.originID == originID:
                    flightsOnDate.append(flight)
        if destinationID != "1":    # If the Flight is not going back to iceland
            if len(flightsOnDate) == 0:   # If there are no flights for the day
                flightNumber = flightNumber + str(numOfFlight)
                return flightNumber
            else:
                for f in flightsOnDate:
                    numOfFlight += 2
                flightNumber = flightNumber + str(numOfFlight)
                return flightNumber
        elif destinationID == "1":  # If the flight is going back to iceland
            numOfFlight += 1
            if len(flightsOnDate) == 0:
                flightNumber = flightNumber + str(numOfFlight)
                return flightNumber
            else:
                for f in flightsOnDate:
                    numOfFlight += 2
                flightNumber = flightNumber + str(numOfFlight)
                return flightNumber



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
        col, val = aList[2], aList[3] # The column of the desired value and the value
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Flight number':
                    if value == aList[0]:
                        if col != "Flight ID" or col != "Flight number":
                            for i in self.flightList:
                                if i.flightNumber == aList[0]:
                                    departureTime = datetime.strptime(i.departureTime, '%Y-%m-%d %H:%M:%S')
                                    if departureTime.date() == aList[1].date():
                                        if col == "Flight status":
                                            i.flightStatus = val
                                        elif col == "Departure time":
                                            i.departureTime = val
                                            travelHours, travelMinutes = map(int, i.travelTime.split(':'))
                                            i.arrivalTime = val + timedelta(hours = travelHours, minutes = travelMinutes)
                                            self.__dictList[index]["Arrival time"] = val + timedelta(hours = travelHours, minutes = travelMinutes)
                                        self.__dictList[index][col] = val
                                        self.write_dictList_to_file()
                                        self.get_flights_from_file()
                                        self.create_flight_instances()
                                        return i

    def add_flight_instance(self, dict):
        flight = Flight(dict)
        self.flightList.append(flight)
        return flight

    def create_flight_instances(self):
        """Methood runs through list of dictionaries,
        creates an instance of flight and appends to the list."""
        self.flightList = []
        for dictionary in self.__dictList:
            flight = Flight(dictionary)
            self.flightList.append(flight)

    def createNewFlight(self, flightList):
        """creates a new airplane instance and writes the airplane to the csv, then it returns the new
            airplane object"""
        flightInstance = self.write_flight_to_file(flightList)
        return flightInstance


class Flight:
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
            returnString.append((key + ": " + str(val)))
        return "\n".join(returnString)

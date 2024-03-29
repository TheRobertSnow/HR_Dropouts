import sys
from datetime import datetime
from datetime import timedelta
sys.path.append('..')
import IOAPI

class FlightLL():
    def __init__(self):
        self.flightIO = IOAPI.IOAPI()
        self.__flightList = self.flightIO.getAllFlightInstances()

    def createNewFlight(self, flightList1):
        """Creates Flight with the information from the list -flightList1"""
        flightList = []
        for i in flightList1:
            flightList.append(i)
        flightNumber = self.flightIO.getFlightNumber(flightList[1], flightList[2], flightList[3])
        airplaneReg = flightList[0]
        airplane = self.flightIO.getCertainAirplane(airplaneReg)
        if type(airplane) == str:
            return airplane
        flightList.insert(0, flightNumber)
        flightList.insert(4, "On schedule")
        flightrouteInstances = self.flightIO.getAllFlightRouteInstances()
        if flightList[3] == "1":
            if int(flightList[2]) <= len(flightrouteInstances):
                travelTime = self.flightIO.getTravelTime(flightList[2])
            else:
                return "\nThere does not exist a flight route with the id {}\n".format(flightList[2])
        elif flightList[2] == "1":
            if int(flightList[3]) <= len(flightrouteInstances):
                travelTime = self.flightIO.getTravelTime(flightList[3])
                timeFrameStart = flightList[5] - timedelta(minutes = 5)
                timeFrameEnd = flightList[5] + timedelta(minutes = 5)
                for instance in self.__flightList:
                    if instance.originID == "1":
                        dt = instance.departureTime
                        if type(instance.departureTime) != str:
                            dt = instance.departureTime.__str__()
                        departureTime = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
                        if departureTime >= timeFrameStart and departureTime <= timeFrameEnd:
                            return "There is another flight from iceland at {} so the departure time you input is not valid".format(instance.departureTime)
            else:
                return "\nThere does not exist a flight route with the id {}\n".format(flightList[3])
        else:
            return "\nYou can not create a flight that does not have Iceland as the departure nor the destination country\n"
        travelHours, travelMinutes = map(int, travelTime.split(':'))
        flightList.insert(5, travelTime)
        arrivalTime = flightList[6] + timedelta(hours = travelHours, minutes = travelMinutes)
        flightList.insert(7, arrivalTime)
        flight = self.flightIO.createNewFlight(flightList)                                          
        print("\nNow there are", len(self.__flightList), "Flight objects in system")      
        return flight

    def getCertainflight(self, flightNumber, flightDate):
        """Gets the flight that is searched for by sending"""
        self.automatically_change_flight_status()
        for instance in self.__flightList:
            flightNumbers = instance.flightNumber
            departureTime = datetime.strptime(instance.departureTime, '%Y-%m-%d %H:%M:%S')
            if departureTime.date() == flightDate.date():
                if flightNumbers.lower() == flightNumber.lower():
                    return instance
        return "Flight not found!"

    def getAllFlights(self):
        """gets all flights and returns a list of all flights"""
        self.automatically_change_flight_status()
        self.__flightList = self.flightIO.getAllFlightInstances()
        return self.__flightList

    def viewFlightsByStatuses(self, statuses):
        """Views flights by statuses"""
        self.automatically_change_flight_status()
        statusFlightList = []
        for instance in self.__flightList:
            flightStatus = instance.flightStatus
            for status in statuses:
                if flightStatus == status:
                    statusFlightList.append(instance)
        if len(statusFlightList) == 0:
            return "\nThere are no flights with the statuses given!\n"
        else:
            return statusFlightList

    def automatically_change_flight_status(self):
        """Always called to change flight status"""
        flight = self.flightIO.automatically_change_flight_status()
        return flight

    def updateFlightStatus(self, flightlist):
        """updates flight status"""
        flight = self.flightIO.updateFlightStatus(flightlist)
        self.automatically_change_flight_status()
        return flight

    def updateFlightDepartureTime(self, newDepartureTime):
        """updates departure time for flights"""
        flight = self.flightIO.updateFlightDepartureTime(newDepartureTime)
        self.automatically_change_flight_status()
        return flight

    def getCertainFlightFromID(self, flightOutId):
        """searches for flight via id"""
        self.__flightList = self.flightIO.getAllFlightInstances()
        for instance in self.__flightList:
            if str(instance.flightID) == str(flightOutId):
                return instance
        return "\nNo flight with that ID found\n"

    def getNextFlightID(self):
        """Gets next flight id"""
        return self.flightIO.getNextFlightID()

    def getDate(self, flightID):
        """gets date"""
        self.__flightList = self.flightIO.getAllFlightInstances()
        for instance in self.__flightList:
            if str(instance.flightID) == str(flightID):
                date = instance.departureTime
                date = str(date)
                date = date.split(" ")[0]
                return date
        return "\nError! couldn't find a matching ID\n"

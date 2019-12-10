import sys
from datetime import datetime
from datetime import timedelta
sys.path.append('..')
import IOAPI

class FlightLL():
    def __init__(self):
        self.flightIO = IOAPI.IOAPI()
        self.__flightList = self.flightIO.getAllFlightInstances()
    
    def createNewFlight(self, flightList):
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
                return "There does not exist a flight route with the id {}".format(flightList[2])
        elif flightList[2] == "1":
            if int(flightList[3]) <= len(flightrouteInstances):
                travelTime = self.flightIO.getTravelTime(flightList[3])
                timeFrameStart = flightList[5] - timedelta(minutes = 5)
                timeFrameEnd = flightList[5] + timedelta(minutes = 5)
                for instance in self.__flightList:
                    if instance.originID == "1":
                        departureTime = datetime.strptime(instance.departureTime, '%Y-%m-%d %H:%M:%S')
                        if departureTime >= timeFrameStart and departureTime <= timeFrameEnd:
                            return "There is another flight from iceland at {} so the departure time you input is not valid".format(instance.departureTime)
            else:
                return "There does not exist a flight route with the id {}".format(flightList[3])
        else:
            return "You can not create a flight that does not have Iceland as the departure nor the destination country"
        travelHours, travelMinutes = map(int, travelTime.split(':'))
        flightList.insert(5, travelTime)
        arrivalTime = flightList[6] + timedelta(hours = travelHours, minutes = travelMinutes)
        flightList.insert(7, arrivalTime)
        flight = self.flightIO.createNewFlight(flightList)
        print("\nNow there are", len(self.__flightList), "Flight objects in system\n")
        return flight
                
    def getCertainflight(self, flightNumber):
        for instance in self.__flightList:
            flightNumbers = instance.flightNumber
            if flightNumbers.lower() == flightNumber.lower():
                return instance
        return "Flight not found!"
    
    def getAllFlights(self):     
        return self.__flightList
    
    def viewFlightsByStatus(self, status):
        statusFlightList = []       
        for instance in self.__flightList:           
            flightStatus = instance.flightStatus           
            if flightStatus == status:                
                statusFlightList.append(instance)     
        return statusFlightList
    
    def updateFlightStatus(self, flightlist):
        flight = self.flightIO.updateFlightStatus(flightlist)
        return flight
    
    def updateFlightDepartureTime(self, newDepartureTime):
        flight = self.flightIO.updateFlightDepartureTime(newDepartureTime)
        return flight
        
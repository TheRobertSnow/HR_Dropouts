import sys
from datetime import datetime  
from datetime import timedelta  
#import collections
sys.path.append('..')
import IOAPI

class FlightLL():
    def __init__(self):
        self.flightIO = IOAPI.IOAPI()
        self.__flightList = self.flightIO.getAllFlightInstances()
    
    def createNewFlight(self, flightList):
       self.flightIO.getFlightNumber(flightList[2], flightList[3])
       print(flightList)
       flightNumber = "NA031"
       flightList.insert(0, flightNumber)
       flightList.insert(4, "On schedule")
       if flightList[3] == "1":
           travelTime = self.flightIO.getTravelTime(flightList[2])
       else:
           travelTime = self.flightIO.getTravelTime(flightList[3])
       travelHours, travelMinutes = map(int, travelTime.split(':'))
       flightList.insert(5, travelTime)
       arrivalTime = flightList[6] + timedelta(hours = travelHours, minutes = travelMinutes)
       flightList.insert(7, arrivalTime)
       flight = self.flightIO.createNewFlight(flightList)
       print("\nNow there are", len(self.__flightList), "Flight objects in system\n")
       return flight
    
    def get_flight_list(self):
        return self.__flightList
                
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
        
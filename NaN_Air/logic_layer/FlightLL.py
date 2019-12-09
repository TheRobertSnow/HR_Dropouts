import sys
from datetime import datetime  
from datetime import timedelta  
#import collections
sys.path.append('..')
import IOAPI

def getFlightNumber(self, flightList):
    company = "NA"
    if flightList[1] == "0":
        lastNumber = "0"
    else:
        lastNumber = "1"
    flightNumber = company + "0" + flightList[1] + lastNumber
    return flightNumber

class FlightLL():
    def __init__(self):
        self.flightIO = IOAPI.IOAPI()
        self.__flightList = self.flightIO.getAllFlightInstances()
    
    def createNewFlight(self, flightList):
       newID = self.flightIO.getHigestFlightID()
       flightList.insert(0, newID)
       flightNumber = getFlightNumber(self, flightList)
       flightList.insert(1, flightNumber)
       flightList.insert(5, "On schedule")
       """if flightList[3] = "0":
           travelTime = self.flightIO.getTravelTime(flightList[4])
       else:
           travelTime = self.flightIO.getTravelTime(flightList[3])"""
       travelTime = "03:45"
       flightList.insert(6, travelTime)
       arrivalTime = datetime.now() + timedelta(hours=int(travelTime[:2]), minutes=int(travelTime[3:]))
       flightList.insert(8, arrivalTime)
       self.flightIO.createNewFlight(flightList)
       print("Now there are", len(self.__flightList), "Flight objects in system")
    
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
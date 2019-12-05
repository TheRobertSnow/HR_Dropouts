import IOAPI
from logic_layer import Flight
import collections

def getFlightNumber(self, flightList):
    company = "NA"
    print(flightList[1])
    if flightList[1] == "0":
        lastNumber = "0"
    else:
        lastNumber = "1"
    flightNumber = company + "0" + flightList[1] + lastNumber
    return flightNumber

class FlightLL():
    def __init__(self):
        """Calling me will create a object for every flight in the flight.csv file"""
        self.ioAPI = IOAPI.IOAPI()
        self.flightList = self.ioAPI.getFlightList()
        self.instanceList = []
        for objectDict in self.flightList:
            flight = Flight.CreateFlight(objectDict)
            self.instanceList.append(flight)
        print(len(self.instanceList), "Flight objects in our system, this print command is found in FlightLL")

    def createNewFlight(self, flightList):
        orderedDict = collections.OrderedDict()
        newID = 0
        for instance in self.instanceList:
            id = instance.getID()
            if int(id) > newID:
                newID = int(id)
        newID += 1
        flightNumber = getFlightNumber(self, flightList)
        orderedDict["flight id"] = newID
        orderedDict["flight number"] = flightNumber
        orderedDict["airplane reg"] = flightList[0]
        orderedDict["flight route id"] = flightList[1]
        orderedDict["destination"] = flightList[2]
        orderedDict["flight status"] = "On Air"
        orderedDict["travel time"] = "TravelTIMEisGOnnaBEHEre"
        orderedDict["departure time"] = flightList[3]
        orderedDict["arrival time"] = "ArrivalTIMEISgonnaBEhere"
        list.insert(0, newID)
        list.insert(1, flightNumber)
        list.insert(5, "On Air")
        list.insert(6, "TravelTIMEisGOnnaBEHEre")
        list.insert(8, "ArrivalTIMEISgonnaBEhere")
        newFlight = Flight.CreateFlight(orderedDict)
        self.instanceList.append(newFlight)
        
        print("now there are", len(self.instanceList), "Flight objects in system")
        returnString = self.ioAPI.createFlightRequest(orderedDict, flightList)
        return returnString

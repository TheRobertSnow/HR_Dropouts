import IOAPI
from logic_layer import Flight
import collections

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
        """Calling me will create a object for every flight in the flight.csv file"""
        self.ioAPI = IOAPI.IOAPI()
        self.flightList = self.ioAPI.getFlightList()
        self.instanceList = []
        for objectDict in self.flightList:
            flight = Flight.CreateFlight(objectDict)
            self.instanceList.append(flight)
        print(len(self.instanceList), "Flight objects in our system")

    def createNewFlight(self, flightList):
        orderedDict = collections.OrderedDict()
        newID = 0
        for instance in self.instanceList:
            id = instance.getID()
            if int(id) > newID:
                newID = int(id)
        newID += 1
        flightNumber = getFlightNumber(self, flightList)
        orderedDict["Flight ID"] = newID
        orderedDict["Flight number"] = flightNumber
        orderedDict["Airplane registration number"] = flightList[0]
        orderedDict["Origin ID"] = flightList[1]
        orderedDict["Destination ID"] = flightList[2]
        orderedDict["Flight status"] = "On Air"
        orderedDict["Travel time"] = "TravelTIMEisGOnnaBEHEre"
        orderedDict["Departure time"] = flightList[3]
        orderedDict["Arrival time"] = "ArrivalTIMEISgonnaBEhere"
        flightList.insert(0, newID)
        flightList.insert(1, flightNumber)
        flightList.insert(5, "On Air")
        flightList.insert(6, "TravelTIMEisGOnnaBEHEre")
        flightList.insert(8, "ArrivalTIMEISgonnaBEhere")
        newFlight = Flight.CreateFlight(orderedDict)
        self.instanceList.append(newFlight)
        print("now there are", len(self.instanceList), "Flight objects in system")
        returnString = self.ioAPI.createFlightRequest(orderedDict, flightList)
        return returnString
    
    def getXflight(self, flightNumber):
        for object in self.instanceList:
            tag = object.getFlightNumber()
            if tag.lower() == flightNumber.lower():
                return object
        return "Flight not found!"
    
    def getAllFlights(self):
        return self.instanceList

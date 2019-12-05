from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.OnLoad()
        self.flights = FlightIO.FlightIO()

    def createPlaneRequest(self, dictionary, list):
        returnString = self.airplanes.newAirplane(dictionary, list)
        return returnString

    def getPlaneList(self):
        planeList = self.airplanes.returnObjectList()
        return planeList
    
    def createFlightRequest(self, objectDict, flightList):
        returnString = self.flights.newFlight(objectDict, flightList)
        return returnString

    def getFlightList(self):
        flightList = self.flights.returnObjectList()
        return flightList
    
 
from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.OnLoad()
        self.flights = FlightIO.FlightIO()

    def createPlaneRequest(self, dictionary, myList):
        returnString = self.airplanes.newAirplane(dictionary, myList)
        return returnString

    def getPlaneList(self):
        planeList = self.airplanes.returnObjectList()
        return planeList
    
    def createFlightRequest(self, objectDict, flightList):
        returnString = self.flights.write_flight_to_file(objectDict, flightList)
        return returnString

    def getFlightList(self):
        flightList = self.flights.returnObjectList()
        return flightList
    
    def getHigestFlightID(self):
        highestID = self.flights.getHighestID()
        return highestID
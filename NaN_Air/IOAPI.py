from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.OnLoad()
        self.flightRoute = FlightRouteIO.FlightRoute()
        

    def createPlaneRequest(self, dictionary, alist):
        returnString = self.airplanes.newAirplane(dictionary, alist)
        return returnString

    def getPlaneList(self):
        planeList = self.airplanes.returnObjectList()
        return planeList

    def createFlightRouteRequest(self, newFlightRouteList):
        flightRouteList = self.flightRoute.write_flight_route_to_file(newFlightRouteList)
        return flightRouteList

    def getFlightRouteList(self):
        flightRouteList = self.flightRoute.FlightRoute()
        return flightRouteList


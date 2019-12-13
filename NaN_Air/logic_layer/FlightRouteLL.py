import sys
sys.path.append('..')
import IOAPI

class FlightRouteLL():
    def __init__(self):
        self.ioAPI = IOAPI.IOAPI()
        self.__flightRouteList = self.ioAPI.getAllFlightRouteInstances()        

    def find_flight_route_by_id(self, flightID):
        """finds flight route with id"""
        self.__flightRouteList = self.ioAPI.getAllFlightRouteInstances()
        for instance in self.__flightRouteList:
            if flightID == instance.flightRouteID:
                return instance
        return "\nFlight route not found!\n"

    def getAllFlightRoutes(self):
        """gets all flight routes in the form of a list from the init func"""
        return self.__flightRouteList
    
    def updateFlightRoute(self, flightRouteList):
        """Sends update function a new list that"""
        flightRoute = self.ioAPI.updateFlightRoute(flightRouteList)
        return flightRoute

    def createNewFlightRoute(self, flightRouteList):
        "List of strings and ints, information on flight route"
        "flight route list = str fx (Flight route succesfully created)"
        try:
            flightRouteList[2] = int(flightRouteList[2])
        except ValueError:
            return "\nError: Flight distance must be a whole number!\n"
        flightRoute = self.ioAPI.createNewFlightRoute(flightRouteList)
        print("\nNow there are", len(self.__flightRouteList), "Flight Route objects in system")
        return flightRoute


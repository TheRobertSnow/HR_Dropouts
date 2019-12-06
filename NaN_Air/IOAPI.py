from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.OnLoad()
        self.flights = FlightIO.FlightIO()
        self.workers = WorkerIO.WorkerIO()
        self.flightRoute = FlightRouteIO.FlightRoute()
    #
    # plane related
    #      
    def createPlaneRequest(self, dictionary, myList):
        returnString = self.airplanes.newAirplane(dictionary, myList)
        return returnString

    def getPlaneList(self):
        planeList = self.airplanes.returnObjectList()
        return planeList
    #
    # worker related
    #
    def createWorkerRequest(self, objectDict, myList):
        returnString = self.workers.write_worker_to_file(objectDict, myList)
        return returnString
    
    def getWorkerList(self):
        workerList = self.workers.returnObjectList()
        return workerList
    #
    # flight related
    #
    def createFlightRequest(self, objectDict, flightList):
        returnString = self.flights.write_flight_to_file(objectDict, flightList)
        return returnString

    def getFlightList(self):
        flightList = self.flights.returnObjectList()
        return flightList
    
    def getHigestFlightID(self):
        highestID = self.flights.getHighestID()
        return highestID
    #
    # voyage related
    #

    #
    # flight route related
    #
    def createFlightRouteRequest(self, newFlightRouteList):
        flightRouteList = self.flightRoute.write_flight_route_to_file(
            newFlightRouteList)
        return flightRouteList

    def getFlightRouteList(self):
        flightRouteList = self.flightRoute.FlightRoute()
        return flightRouteList
    

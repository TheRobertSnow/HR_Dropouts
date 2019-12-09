from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.AirplaneIO()
        self.flights = FlightIO.FlightIO()
        self.workers = WorkerIO.WorkerIO()
        self.flightRoutes = FlightRouteIO.FlightRouteIO()
        self.voyages = VoyageIO.VoyageIO()

    def request_airplanes(self):
        airplaneList = self.airplanes.get_airplanes_from_file()
        return airplaneList

    def request_flights(self):
        flightList = self.flights.get_flights()
        return flightList

    def request_workers(self):
        workerInstanceList = self.workers.get_workers_from_file()
        return workerInstanceList

    def request_flight_routes(self):
        flightRouteList = self.flightRoutes.get_flight_routes()
        # print(flightRouteList)
        return flightRouteList

    def request_voyages(self):
        voyageList = self.voyages.get_voyages()
        return voyageList

    # def createPlaneRequest(self, dictionary, myList):
    #     returnString = self.airplanes.newAirplane(dictionary, myList)
    #     return returnString
    #
    # def getPlaneList(self):
    #     planeList = self.airplanes.returnObjectList()
    #     return planeList

    # def createFlightRequest(self, objectDict, flightList):
    #     returnString = self.flights.write_flight_to_file(objectDict, flightList)
    #     return returnString
    #
    # def getFlightList(self):
    #     flightList = self.flights.returnObjectList()
    #     return flightList
    #
    # def getHigestFlightID(self):
    #     highestID = self.flights.getHighestID()
    #     return highestID

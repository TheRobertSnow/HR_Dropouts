from IO_layer import *


class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.AirplaneIO()
        self.flights = FlightIO.FlightIO()
        self.workers = WorkerIO.WorkerIO()
        self.flightRoutes = FlightRouteIO.FlightRouteIO()
        self.voyages = VoyageIO.VoyageIO()

    #
    # plane related
    #
    def request_airplanes(self):
        return self.airplanes.get_airplanes_from_file()

    def newPlaneRequest(self, planeList):
        """requests to write a new plane into the csv file with all parameters checked. needs to be returned the
            instance of the plane that gets created"""
        return self.airplanes.create_airplane_instances(planeList)

    def updateAirplaneStatus(self, newStatus):
        """sends forward the object and the new status of that airplane object, then returns it updated."""
        return self.airplanes.update_data_in_file(newStatus)

    #
    # flight related
    #
    def request_flights(self):
        return self.request_flights()

    #
    # voyage related
    #
    def request_voyages(self):
        return self.voyages.get_voyages()

    #
    # worker related
    #
    def request_workers(self):
        return self.workers.get_workers_from_file()

    #
    # flight route related
    #
    def request_flight_routes(self):
        flightRouteList = self.flightRoutes.get_flight_routes()
        return self.flightRoutes.get_flight_route_from_file()

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

from IO_layer import *


class IOAPI:
    def __init__(self):
        self.airplaneIO = AirplaneIO.AirplaneIO()
        self.flightIO = FlightIO.FlightIO()
        self.workerIO = WorkerIO.WorkerIO()
        self.flightRouteIO = FlightRouteIO.FlightRouteIO()
        self.voyageIO = VoyageIO.VoyageIO()
        # self.send_instance_to_voyage()

    #
    # Worker
    #
    def createNewWorker(self, workerList):
        return self.workerIO.createNewWorker(workerList)

    def request_workers(self):
        return self.workerIO.get_workers_from_file()

    #
    # Airplane
    #

    def createNewAirplane(self, airplaneList):
        """takes in a list for the airplane csv file to write to. returns the result"""
        return self.airplaneIO.createNewAirplane(airplaneList)

    def request_airplanes(self):
        """returns a updated list of all plane objects"""
        return self.airplaneIO.get_airplanes()

    def updatePlane(self, planeInstance, newStatus):
        """takes in the instance of the plane and the new status and sends it back, returns the updated object"""
        return self.airplaneIO.UpdateCertainAirplane(planeInstance, newStatus)
    #
    # Flight Route
    #

    def createNewFlightRoute(self, createFlightRouteList):
        # TODO create new flight route method in flightRouteIO
        newFlightRouteList = self.flightRouteIO.create_new_flight_route(
            createFlightRouteList)  # sending list of strings and ints
        return newFlightRouteList

    def request_flight_routes(self):
        return self.flightRouteIO.get_flight_routes()

    #
    # Voyage
    #

    def createNewVoyage(self, voyageList):
        return self.voyageIO.createNewVoyage(voyageList)

    def request_voyages(self):
        return self.voyageIO.get_voyages()

    #
    # Flight
    #

    def createNewFlight(self, flightList):
        return self.flightIO.write_flight_to_file(flightList)

    def getHigestFlightID(self):
        return self.workerIO.getNextID()

    def getAllFlightInstances(self):
        return self.flightIO.get_flights()

    def send_instance_to_voyage(self):
        """This methood is for sending pointers to the instance lists of
        workers, flights, airplanes and flight routes to voyage."""
        # self.voyages.get_other_class_instances(self.request_airplanes()
        # , self.request_flights(), self.request_workers(), self.request_flight_routes())
        print("")
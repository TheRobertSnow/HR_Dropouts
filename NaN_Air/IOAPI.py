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

    def createNewWorker(self, workerDict):
        return self.workerIO.createNewWorker(workerDict)

    def createNewWorkerInstance(self, workerList):
        return self.workerIO.createNewWorkerInstance(workerList)

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

    def createNewFlightRoute(self, flightRouteDict):
        return self.flightRouteIO.createNewFlightRoute(flightRouteDict)

    def createNewFlightRouteInstance(self, flightRouteList):
        return self.flightRouteIO.createNewFlightRouteInstance(flightRouteList)

    def request_flight_routes(self):
        return self.flightRouteIO.get_flight_routes()

    #
    # Voyage
    #

    def createNewVoyage(self, voyageDict):
        return self.voyageIO.createNewVoyage(voyageDict)

    def createNewVoyageInstance(self, voyageList):
        return self.voyageIO.createNewVoyageInstance(voyageList)

    def request_voyages(self):
        return self.voyageIO.get_voyages()

    # Flight
    def createNewFlight(self, flightDict):
        return self.flightIO.createNewFlight(flightDict)

    def createNewFlightInstance(self, flightList):
        return self.flightIO.createNewFlightInstance(flightList)

    def requestFlights(self):
        return self.flightIO.get_flights()

    def send_instance_to_voyage(self):
        """This methood is for sending pointers to the instance lists of
        workers, flights, airplanes and flight routes to voyage."""
        # self.voyages.get_other_class_instances(self.request_airplanes()
        # , self.request_flights(), self.request_workers(), self.request_flight_routes())
        pass

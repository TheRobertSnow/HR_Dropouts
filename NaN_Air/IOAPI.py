from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplaneIO = AirplaneIO.AirplaneIO()
        self.flightIO = FlightIO.FlightIO()
        self.workerIO = WorkerIO.WorkerIO()
        self.flightRouteIO = FlightRouteIO.FlightRouteIO()
        self.voyageIO = VoyageIO.VoyageIO()
        #self.send_instance_to_voyage()
        
    #Worker
    def createNewWorker(self, workerList):
        return self.workerIO.createNewWorker(workerList)

    def request_workers(self):
        return self.workerIO.get_workers_from_file()

    #Ariplane
    def createNewAirplane(self, airplaneList):
        return self.airplaneIO.createNewAirplane(airplaneList)

    def request_airplanes(self):
        return self.airplaneIO.get_airplanes_from_file()

    #Flight Route
    def createNewFlightRoute(self, flightRouteList):
        return self.flightRouteIO.createNewFlightRoute(flightRouteList)

    def request_flight_routes(self):
        return self.flightRouteIO.get_flight_routes()

    #Voyage
    def createNewVoyage(self, voyageList):
        return self.voyageIO.createNewVoyage(voyageList)

    def request_voyages(self):
        return self.voyageIO.get_voyages()

    #Flight
    def createNewFlight(self, flightList):
        return self.flightIO.write_flight_to_file(flightList)

    def getHigestFlightID(self):
        return self.workerIO.getNextID()

    def getAllFlightInstances(self):
        return self.flightIO.get_flights()

    def send_instance_to_voyage(self):
        """This methood is for sending pointers to the instance lists of
        workers, flights, airplanes and flight routes to voyage."""
        #self.voyages.get_other_class_instances(self.request_airplanes()
        #, self.request_flights(), self.request_workers(), self.request_flight_routes())
        print("")


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

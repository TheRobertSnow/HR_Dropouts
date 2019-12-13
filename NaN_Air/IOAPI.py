from IO_layer import *


class IOAPI:
    def __init__(self):
        self.airplaneIO = AirplaneIO.AirplaneIO()
        self.flightIO = FlightIO.FlightIO()
        self.workerIO = WorkerIO.WorkerIO()
        self.flightRouteIO = FlightRouteIO.FlightRouteIO()
        self.voyageIO = VoyageIO.VoyageIO(self.airplaneIO.airplaneList,
                                          self.flightIO.flightList,
                                          self.workerIO.workerList,
                                          self.flightRouteIO.flightRouteList)

    #
    # Worker
    #
    
    def createNewWorker(self, workerList):
        """creates new worker """
        worker = self.workerIO.writeworkertoFile(workerList)
        return worker

    def request_workers(self):
        """gets workers"""
        return self.workerIO.get_workers()

    def updateWorker(self, instance, key, newValue):
        """updates worker"""
        return self.workerIO.updateCertainWorker(instance, key, newValue)

    #
    # Airplane
    #

    def createNewAirplane(self, airplaneList):
        """takes in a list for the airplane csv file to write to. returns the result"""
        return self.airplaneIO.createNewAirplane(airplaneList)

    def getCertainAirplane(self, airplaneReg):
        """Gets airplane with airplane register"""
        airplane = self.airplaneIO.getCertainAirplane(airplaneReg)
        return airplane

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
        """creates a new flight route"""
        newFlightRouteList = self.flightRouteIO.create_new_flight_route(createFlightRouteList)  # sending list of strings and ints
        return newFlightRouteList

    def getAllFlightRouteInstances(self):
        """gets all flight route instances"""
        return self.flightRouteIO.get_flightRoutes()

    def updateFlightRoute(self, flightRouteList):
        """updates a flight route"""
        return self.flightRouteIO.update_data_in_file(flightRouteList)

    #
    # Voyage
    #

    def createNewVoyage(self, voyageList):
        """creates a new voyage"""
        return self.voyageIO.createNewVoyage(voyageList)

    def request_voyages(self):
        """gets voyages"""
        return self.voyageIO.get_voyages()

    def updateVoyage(self, theObject, theKey, newValue):
        """updates voyages"""
        return self.voyageIO.updateCertainVoyage(theObject, theKey, newValue)
    
    #
    # Flight
    #
    
    def automatically_change_flight_status(self):
        """automaticly changes flights"""
        return self.flightIO.automatically_change_flight_status()
    
    def getFlightNumber(self, originID, destinationID, departureTime):
        """Send request to FlightIO to get flight number"""
        return self.flightIO.get_flight_number(originID, destinationID, departureTime)

    def createNewFlight(self, flightList):
        """creates a new flight"""
        return self.flightIO.write_flight_to_file(flightList)

    def getHighestFlightID(self):
        """gets latest flight id"""
        return self.workerIO.getNextID()

    def getTravelTime(self, flightRouteID):
        """gets travel time for a flight"""
        return self.flightRouteIO.getFlightRouteTravelTime(flightRouteID)

    def updateFlightStatus(self, flightlist):
        """updates status for flights"""
        return self.flightIO.update_data_in_file(flightlist)

    def updateFlightDepartureTime(self, newDepartureTime):
        """updates departure time for flights"""
        return self.flightIO.update_data_in_file(newDepartureTime)

    def getAllFlightInstances(self):
        """gets instances for flights"""
        return self.flightIO.get_flights()

    def getNextFlightID(self):
        """flights"""
        return self.flightIO.getNextID()



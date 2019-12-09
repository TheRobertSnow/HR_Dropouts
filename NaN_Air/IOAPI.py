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
    def createNewWorker(self, workerDict):
        workerData = self.workerIO.createNewWorker(workerDict)
        return workerData
    
    def createNewWorkerInstance(self, workerList):
        workerData = self.workerIO.createNewWorkerInstance(workerList)
        return workerData
    
    def request_workers(self):
        workerInstanceList = self.workerIO.get_workers_from_file()
        return workerInstanceList
    
    #Ariplane
    def createNewAirplane(self, airplaneDict):
        airplaneData = self.airplaneIO.createNewAirplane(airplaneDict)
        return airplaneData
    
    def createNewAirplaneInstance(self, airplaneList):
        airplaneData = self.airplaneIO.createNewAirplaneInstance(airplaneList)
        return airplaneData
    
    def request_airplanes(self):
        airplaneList = self.airplaneIO.get_airplanes_from_file()
        return airplaneList

    #Flight Route
    def createNewFlightRoute(self, createFlightRouteList):
        # TODO create new flight route method in flightRouteIO
        newFlightRouteList = self.flightRouteIO.create_new_flight_route(createFlightRouteList) # sending list of strings and ints
        return newFlightRouteList
    
    
    
    
    def request_flight_routes(self):
        flightRouteList = self.flightRouteIO.get_flight_routes()
        # print(flightRouteList)
        return flightRouteList

    #Voyage
    def createNewVoyage(self, voyageDict):
        voyageData = self.voyageIO.createNewVoyage(voyageDict)
        return voyageData
    
    def createNewVoyageInstance(self, voyageList):
        voyageData = self.voyageIO.createNewVoyageInstance(voyageList)
        return voyageData
    
    def request_voyages(self):
        voyageList = self.voyageIO.get_voyages()
        return voyageList
    
    #Flight
    def createNewFlight(self, flightDict):
        flightData = self.flightIO.createNewFlight(flightDict)
        return flightData

    
    
    def createNewFlightInstance(self, flightList):
        flightData = self.flightIO.createNewFlightInstance(flightList)
        return flightData
    
    def request_flights(self):
        flightList = self.flightIO.get_flights()
        return flightList

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

    #def createNewFlightRoute(self, createFlightRouteList):
     #   newFlightRouteList = self.flightRoutes.write_flightRoute_to_file(createFlightRouteList)
      #  return newFlightRouteList






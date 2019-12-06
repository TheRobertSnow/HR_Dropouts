from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.OnLoad()
        self.flights = FlightIO.FlightIO()
        self.workers = WorkerIO.WorkerIO()
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
    def createWorkerRequest(self, objectDictionary, myList):
        returnString = self.workers.write_worker_to_file(objectDictionary, myList)
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
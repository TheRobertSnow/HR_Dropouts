from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplaneIO = AirplaneIO.AirplaneIO()
        self.flightIO = FlightIO.FlightIO()
        self.workerIO = WorkerIO.WorkerIO()
    #
    # plane related
    #      
    def createPlaneRequest(self, dictionary, myList):
        returnString = self.airplaneIO.newAirplane(dictionary, myList)
        return returnString

    def getPlaneList(self):
        planeList = self.airplaneIO.returnObjectList()
        return planeList
    #
    # worker related
    #
    def getHigestWorkerID(self):
        highestID = self.workerIO.getHighestID()
        return highestID
    
    def createWorkerRequest(self, objectDictionary, myList):
        returnString = self.workerIO.write_worker_to_file(objectDictionary, myList)
        return returnString
    
    def getWorkerList(self):
        workerList = self.workerIO.returnObjectList()
        return workerList
    #
    # flight related
    #
    def createFlightRequest(self, objectDict, flightList):
        returnString = self.flightIO.write_flight_to_file(objectDict, flightList)
        return returnString

    def getFlightList(self):
        flightList = self.flightIO.returnObjectList()
        return flightList
    
    def getHigestFlightID(self):
        highestID = self.flightIO.getHighestID()
        return highestID
    #
    # voyage related
    #

    #
    # flight route related
    #
from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.AirplaneIO()
        # self.flights = FlightIO.FlightIO()
        self.workers = WorkerIO.WorkerIO()

    def request_workers(self):
        workerList = self.workers.get_workers()
        return workerList

    def request_airplanes(self):
        airplaneList = self.airplanes.get_airplanes()
        return airplaneList

    # def createPlaneRequest(self, dictionary, myList):
    #     returnString = self.airplanes.newAirplane(dictionary, myList)
    #     return returnString
    #
    # def getPlaneList(self):
    #     planeList = self.airplanes.returnObjectList()
    #     return planeList

    def createFlightRequest(self, objectDict, flightList):
        returnString = self.flights.write_flight_to_file(objectDict, flightList)
        return returnString

    def getFlightList(self):
        flightList = self.flights.returnObjectList()
        return flightList

    def getHigestFlightID(self):
        highestID = self.flights.getHighestID()
        return highestID

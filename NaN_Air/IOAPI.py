from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.OnLoad()

    def createPlaneRequest(self, dictionary, myList):
        returnString = self.airplanes.newAirplane(dictionary, myList)
        return returnString

    def getPlaneList(self):
        planeList = self.airplanes.returnObjectList()
        return planeList

from IO_layer import *

class IOAPI:
    def __init__(self):
        self.airplanes = AirplaneIO.OnLoad()

    def getPlaneInstance(self):
        """ Returns a list with dictionaries that hold each plane"""
        planeInstances = AirplaneIO.OnLoad()
        planeInstances = AirplaneIO.OnLoad.returnObjectList(planeInstances)
        return planeInstances

    def createPlaneRequest(self, list):
        returnString = AirplaneIO.OnLoad.newAirplane(self.airplanes, list)
        return returnString


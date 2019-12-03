from IO_layer import *


def getPlaneInstance():
    planeInstances = AirplaneIO.OnLoad()
    planeInstances = AirplaneIO.OnLoad.returnObjectList(planeInstances)
    return planeInstances


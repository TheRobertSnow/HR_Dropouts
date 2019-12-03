<<<<<<< HEAD
<<<<<<< HEAD
import sys, os
from IO_layer import *
myInstance = FlightRouteIO.FlightRoute()

# sys.path.append(os.path.abspath('IO_layer'))
# print('\n'.join(sys.path))

# import FlightRouteIO as f
#
# myflightroute = f.FlightRoute()
=======
from IO_layer import *
from logic_layer import *
=======
from IO_layer import *
>>>>>>> d03aad65c30abfcab49244f5b7ac7b4dad3acb78


def getPlaneInstance():
    planeInstances = AirplaneIO.OnLoad()
    planeInstances = AirplaneIO.OnLoad.returnObjectList(planeInstances)
    return planeInstances


<<<<<<< HEAD
>>>>>>> 34f5655694436993af5f8c3a8d490af70fd097c0
=======
>>>>>>> d03aad65c30abfcab49244f5b7ac7b4dad3acb78

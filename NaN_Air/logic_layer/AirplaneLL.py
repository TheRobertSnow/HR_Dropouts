import IOAPI
from logic_layer import Airplane


class AirplaneLL:
    def __init__(self):
        """Calling me will create a object for every plane in the plane.csv file"""
        self.ioAPI = IOAPI.IOAPI()

    def createNewPlane(self, list):
        returnString = IOAPI.IOAPI.createPlaneRequest(self.ioAPI, list)
        return returnString


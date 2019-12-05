import IOAPI
from logic_layer import Airplane
import collections


class AirplaneLL:
    def __init__(self):
        """Calling me will create a object for every plane in the plane.csv file"""
        self.ioAPI = IOAPI.IOAPI()
        self.planeList = self.ioAPI.getPlaneList()
        self.instanceList = []
        for dict in self.planeList:
            airplane = Airplane.CreateAirplane(dict)
            self.instanceList.append(airplane)
        print(len(self.instanceList), "objects in our system, this print command is found in AirplaneLL")

    def createNewPlane(self, list):
        for airplane in self.instanceList:
            reg = airplane.getReg()
            if reg == list[0]:
                return ["Plane with that register already exists"], "Plane creation failed"
        orderedDict = collections.OrderedDict()
        orderedDict["plane reg"] = list[0]
        orderedDict["manufacturer"] = list[1]
        orderedDict["model"] = list[2]
        orderedDict["status"] = "Grounded"
        orderedDict["number of seats"] = list[3]
        orderedDict["odometer"] = list[4]
        list.insert(4, "Grounded")
        newAirPlane = Airplane.CreateAirplane(orderedDict)
        self.instanceList.append(newAirPlane)
        print("now there are", len(self.instanceList), "objects in system")
        returnString = self.ioAPI.createPlaneRequest(orderedDict, list)
        return returnString

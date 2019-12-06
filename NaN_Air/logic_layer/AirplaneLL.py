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

        print(len(self.instanceList), "Airplane objects in our system")
        
    def createNewAirlane(self, airplaneList):
        for airplane in self.instanceList:
            reg = airplane.getReg()
            if reg == airplaneList[0]:
                return ["Plane with that register already exists"], "Plane creation failed"
        orderedDict = collections.OrderedDict()
        orderedDict["plane reg"] = airplaneList[0]
        orderedDict["manufacturer"] = airplaneList[1]
        orderedDict["model"] = airplaneList[2]
        orderedDict["status"] = "Grounded"
        orderedDict["seats"] = airplaneList[3]
        orderedDict["odometer"] = airplaneList[4]
        airplaneList.insert(3, "Grounded")
        newAirPlane = Airplane.CreateAirplane(orderedDict)
        self.instanceList.append(newAirPlane)
        print("now there are", len(self.instanceList), "objects in system")
        returnString = self.ioAPI.createPlaneRequest(orderedDict, airplaneList)
        return returnString

    def getAllAirplanes(self):
        return self.instanceList

    def getCertainAirplane(self, airplaneReg):
        for airplaneObject in self.instanceList:
            currentReg = airplaneObject.airplaneReg
            if currentReg == airplaneReg:
                return airplaneObject
        return "No flight with that Register"

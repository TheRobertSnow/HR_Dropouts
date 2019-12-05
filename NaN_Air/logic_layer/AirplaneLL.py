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
        print(hex(id(self.instanceList)))
        print(len(self.instanceList), "objects in our plane system, this print command is found in AirplaneLL")

    def createNewPlane(self, myList):
        for airplane in self.instanceList:
            reg = airplane.getReg()
            if reg == myList[0]:
                return ["Plane with that register already exists"], "Plane creation failed"
        orderedDict = collections.OrderedDict()
        orderedDict["plane reg"] = myList[0]
        orderedDict["manufacturer"] = myList[1]
        orderedDict["model"] = myList[2]
        orderedDict["status"] = "Grounded"
        orderedDict["number of seats"] = myList[3]
        orderedDict["odometer"] = myList[4]
        myList.insert(3, "Grounded")
        newAirPlane = Airplane.CreateAirplane(orderedDict)
        self.instanceList.append(newAirPlane)
        print("now there are", len(self.instanceList), "objects in system")
        returnString = self.ioAPI.createPlaneRequest(orderedDict, myList)
        return returnString

    def getAllFlights(self):
        return self.instanceList

    def getSpecificFlight(self, regToFind):
        for object in self.instanceList:
            currentReg = object.getReg()
            if currentReg == regToFind:
                return object
        return "No flight with that Register"

    def getXplane(self, tagToFind):
        for object in self.instanceList:
            tag = object.getReg()
            if tag.lower() == tagToFind.lower():
                return object
        return "Flight not found!"

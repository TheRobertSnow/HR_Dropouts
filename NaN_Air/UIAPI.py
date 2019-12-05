from logic_layer import *


# functions that UI layer calls --
class UIAPI:
    def __init__(self):
        self.airplaneInstance = AirplaneLL.AirplaneLL()

    #
    # plane related
    #
    def newPlaneRequest(self, myList):
        """"""
        returnString = self.airplaneInstance.createNewPlane(myList)
        return returnString

    def viewXplane(self, idToFind):
        returnData = self.airplaneInstance.getXplane(idToFind)
        return returnData

    def viewAllPlanes(self):
        returnData = self.airplaneInstance.getAllFlights()
        return returnData

    #
    # worker related
    #

    #
    # flight related
    #

    #
    # voyage related
    #

    #
    # flight route related
    #

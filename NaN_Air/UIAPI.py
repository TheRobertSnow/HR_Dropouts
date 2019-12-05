from logic_layer import *

#functions that UI layer calls --
class UIAPI:
    def __init__(self):
        self.airplaneInstance = AirplaneLL.AirplaneLL()

    #
    # plane related
    #
    def newPlaneRequest(self, list):
        """"""
        returnString = self.airplaneInstance.createNewPlane(list)
        return returnString

    def viewXplane(self, idToFind):
        pass

    def viewAllPlanes(self):
        pass

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

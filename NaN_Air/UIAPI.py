from logic_layer import *

#functions that UI layer calls --
class UIAPI:
    def __init__(self):
        self.instance = AirplaneLL.AirplaneLL()

    def newPlaneRequest(self, list):
        """"""
        returnString = AirplaneLL.AirplaneLL.createNewPlane(self.instance, list)
        return returnString

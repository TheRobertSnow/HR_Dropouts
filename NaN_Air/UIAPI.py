from logic_layer import *

#functions that UI layer calls --
class UIAPI:
    def __init__(self):
        self.instance = AirplaneLL.AirplaneLL()
        self.flightInstance = FlightLL.FlightLL()

    def newPlaneRequest(self, list):
        """"""
        returnString = AirplaneLL.AirplaneLL.createNewPlane(self.instance, list)
        
        return returnString
    def newFlightRequest(self, flightList):
        """"""
        returnString = FlightLL.FlightLL.createNewFlight(self.instance, flightList)
        return returnString
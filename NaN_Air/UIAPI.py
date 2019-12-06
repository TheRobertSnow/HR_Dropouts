from logic_layer import WorkerLL, AirplaneLL, FlightLL, FlightRouteLL, VoyageLL


# functions that UI layer calls --
class UIAPI:
    def __init__(self):
        self.workerLL = WorkerLL.WorkerLL()
        self.flightLL = FlightLL.FlightLL()
        self.airplaneLL = AirplaneLL.AirplaneLL()
        self.flightRouteLL = FlightRouteLL.FlightRouteLL()
        self.voyageLL = VoyageLL.VoyageLL()

    def get_airplanes(self):
        [print(instance) for instance in self.airplaneLL.get_airplane_list()]

    #
    # plane related
    #
    def newPlaneRequest(self, myList):
        """"""
        returnString = self.airplaneLL.createNewPlane(myList)
        return returnString

    def viewXplane(self, idToFind):
        returnData = self.airplaneLL.getXplane(idToFind)
        return returnData

    def viewAllPlanes(self):
        returnData = self.airplaneLL.getAllFlights()
        return returnData

    #
    # worker related
    #
    def view_worker(self, Position, ssn=""):
        """Methood for retreving worker by ssn and, or position"""
        returnData = self.workerLL.find_worker_by_ssn(ssn, Position)
        return returnData

    #
    # flight related
    #
    def newFlightRequest(self, flightList):
        """"""
        returnString = self.flightInstance.createNewFlight(flightList)
        return returnString

    def viewXflight(self, flightNumber):
        returnString = self.flightInstance.getXflight(flightNumber)
        return returnString

    def viewAllFlights(self):
        returnData = self.flightInstance.getAllFlights()
        return returnData

    def viewActiveFlights(self):
        returnString = self.flightInstance.getActiveFlights()
        return returnString

    def viewCancelledFlights(self):
        returnString = self.flightInstance.getCancelledFlights()
        return returnString
    #
    # voyage related
    #

    #
    # flight route related
    #


# ++++++++++ Test Case ++++++++++
# UIAPI = UIAPI()
# UIAPI.get_airplanes()

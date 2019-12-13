import IOAPI

class AirplaneLL:

    def __init__(self):
        self.__IOAPI = IOAPI.IOAPI()  # object for API
        self.__airplanes = self.get_airplane_list()  # object that holds a list of flights from our csv

    def get_airplane_list(self):
        """Returns a list with all airplanes from the airplane.csv file."""
        return self.__IOAPI.request_airplanes()

    def getCertainAirplane(self, airplaneReg):
        return self.__IOAPI.getCertainAirplane(airplaneReg)

    def find_airplane_by_reg(self, reg):
        """Checks all current airplanes in the csv file and prints all matching instances of the reg."""
        notFound = True
        for instance in self.__airplanes:
            if instance.planeRegistration == reg:
                notFound = False
                return instance
        if notFound:
            return "\nAirplane not found!\n"

    def createNewAirplane(self, newPlaneList):
        """ Takes in a list with all values that match the 'airplane.csv' file, sends a request to create the
            new plane and prints out the result. Also checks if all values are valid"""
        # airplane.csv constants
        reg = 0
        seats = 3
        odometer = 4
        # testing all values
        if "-" not in newPlaneList[reg]:  # testing register
            return "\nAirplane creation unsuccessful, all plane registrations must have a '-'!\n"

        try:  # testing odometer
            tester = int(newPlaneList[odometer])
        except ValueError:
            return "\nAirplane creation unsuccessful, odometer value can only have integers.\n"

        try:  # testing seats
            tester = int(newPlaneList[seats])
        except ValueError:
            return "\nAirplane creation unsuccessful, seats value can only have integers.\n"

        for instance in self.__airplanes:  # testing if reg already exists
            if instance.planeRegistration == newPlaneList[reg]:
                return "\nAirplane creation unsuccessful, that register already exists in our system.\n"

        newPlaneObject = self.__IOAPI.createNewAirplane(newPlaneList)
        self.__airplanes = AirplaneLL.get_airplane_list(self)  # update our list of plane objects
        print("\nNow there are", len(self.__airplanes), "Airplane objects in system")   
        return newPlaneObject

    def getAllAirplanes(self):
        return self.__airplanes

    def updateAirplaneStatus(self, airplaneReg, newStatus):
        """takes in the register of plane that needs to be updated and what the new status is."""
        # finding the plane reg object
        for instance in self.__airplanes:
            if instance.planeRegistration.lower() == airplaneReg.lower():
                updatedObject = self.__IOAPI.updatePlane(instance, newStatus)
                self.__airplanes = AirplaneLL.get_airplane_list(self)  # update our list of plane objects
                return updatedObject
        return "\nAirplane register not found. could not update\n"

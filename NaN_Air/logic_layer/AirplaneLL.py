import IOAPI


class AirplaneLL:

    def __init__(self):
        self.__IOAPI = IOAPI.IOAPI()  # object for API
        self.__airplanes = self.get_airplane_list()  # object that holds a list of flights from our csv

    def get_airplane_list(self):
        """Returns a list with all airplanes from the airplane.csv file."""
        return self.__IOAPI.request_airplanes()


    def getCertainAirplane(self, airplaneReg):
        """checks all current airplanes in the csv file and returns the instance that matches
            takes in the object instance and the reg of the object you need."""
        self.__airplanes = AirplaneLL.get_airplane_list(self)  # update our list in case there are new planes
        for instance in self.__airplanes:
            if instance.planeRegistration == airplaneReg:
                return instance
        return "Airplane not found!"

    def find_airplane_by_reg(self, reg):
        """Checks all current airplanes in the csv file and prints all matching instances of the reg."""
        self.airplanes = AirplaneLL.get_airplane_list(self)  # update our list in case there are new planes
        print(len(self.airplanes))
        notFound = True
        for instance in self.airplanes:
            if instance.planeRegistration == reg:
                notFound = False
                print(instance)
        if notFound:
            print("Airplane not found!")

    def createNewAirplane(self, newPlaneList):
        """ Takes in a list with all values that match the 'airplane.csv' file, sends a request to create the
            new plane and prints out the result. Also checks if all values are valid"""
        # airplane.csv constants
        reg = 0
        seats = 4
        odometer = 5
        # testing all values
        if "-" not in newPlaneList[reg]:  # testing register
            return "plane creation unsuccessful, all plane registrations must have a '-'!"

        try:  # testing odometer
            tester = int(newPlaneList[odometer])
        except ValueError:
            return "plane creation unsuccessful, odometer value can only have integers."

        try:  # testing seats
            tester = int(newPlaneList[seats])
        except ValueError:
            return "plane creation unsuccessful, seats value can only have integers."

        for instance in self.__airplanes:  # testing if reg already exists
            if instance.planeRegistration == newPlaneList[reg]:
                return "plane creation unsuccessful, that register already exists in our system."

        newPlaneObject = self.__IOAPI.newPlaneRequest(newPlaneList)
        self.__airplanes.append(newPlaneObject)
        return newPlaneObject

    def getAllAirplanes(self):
        pass

    def updateAirplaneStatus(self, airplaneReg, newStatus):
        """takes in the register of plane that needs to be updated and what the new status is."""
        # finding the plane reg object
        for instance in self.__airplanes:
            if instance.planeRegistration == airplaneReg:
                updatedObject = self.__IOAPI.updateAirplaneStatus(newStatus)
                return updatedObject
        return "Plane register not found. could not update"


# +++++++++ Test Case ++++++++++
# testing is done from a file at the root, similar to run.py
# testCase = AirplaneLL()
# testCase.get_airplane_list()

class CreateAirplane:
    def __init__(self, dictionary):
        self.__myDictionary = {"airplaneId": dictionary["airplane id"], "planeReg": dictionary["plane reg"],
                               "manufacturer": dictionary["manufacturer"], "model": dictionary["model"],
                               "status": dictionary["status"], "numbOfSeats": dictionary["number of seats"],
                               "odometer": dictionary["odometer"]}

    def getID(self):
        return self.__myDictionary["airplaneId"]

    def getReg(self):
        return self.__myDictionary["planeReg"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)



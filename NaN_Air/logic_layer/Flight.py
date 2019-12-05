class CreateFlight:
    def __init__(self, objectDict):
        self.__myDictionary = objectDict
        self.flightID = objectDict["Flight ID"]
        self.flightNumber = objectDict["Flight number"]
        self.airplaneReg = objectDict["Airplane registration number"]
        self.originID = objectDict["Origin ID"]
        self.destinationID = objectDict["Destination ID"]
        self.flightStatus = objectDict["Flight status"]
        self.travelTime = objectDict["Travel time"]
        self.departureTime = objectDict["Departure time"]
        self.arrivalTime = objectDict["Arrival time"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

class CreateFlight:
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.flightID = dictionary["Flight ID"]
        self.flightNumber = dictionary["Flight number"]
        self.airplaneReg = dictionary["Airplane registration number"]
        self.originID = dictionary["Origin ID"]
        self.destinationID = dictionary["Destination ID"]
        self.flightStatus = dictionary["Flight status"]
        self.travelTime = dictionary["Travel time"]
        self.departureTime = dictionary["Departure time"]
        self.arrivalTime = dictionary["Arrival time"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

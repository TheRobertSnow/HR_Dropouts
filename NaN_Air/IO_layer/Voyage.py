class CreateVoyage:
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.voyageId = dictionary["Voyage ID"]
        self.flightOutID = dictionary["Flight out ID"]
        self.flightBackID = dictionary["Flight back ID"]
        self.mainPilot = dictionary["Main pilot"]
        self.assistingPilot = dictionary["Assisting pilot"]
        self.mainFlightAttendant = dictionary["Main flight attendant"]
        self.flightAttendants = dictionary["Flight attendants"]
        self.flightRouteID = dictionary["Flight route ID"]
        self.departureFromIs = dictionary["Departure from IS"]
        self.departureToIs = dictionary["Departure to IS"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)



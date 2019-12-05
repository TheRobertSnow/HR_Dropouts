class CreateFlightRoute:
    def __init__(self, dictionary):
        self.__myDictionary = {}
        self.__myDictionary["Flight Route Id"] = dictionary["flight route id"]
        self.__myDictionary["Country"] = dictionary["country"]
        self.__myDictionary["Airport"] = dictionary["airport"]
        self.__myDictionary["Flight Distance"] = dictionary["flight distance"]
        self.__myDictionary["Travel Time"] = dictionary["travel time"]
        self.__myDictionary["Emergency Contact"] = dictionary["emergency contact"]
        self.__myDictionary["Emergency Number"] = dictionary["emergency number"]
        self.__myDictionary["Departure Time"] = dictionary["Departure time"]
        self.__myDictionary["Arrival Time"] = dictionary["Arrival time"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)


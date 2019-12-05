class CreateFlight:
    def __init__(self, dictionary):
        self.__myDictionary = {}
        self.__myDictionary["Flight Id"] = dictionary["Flight ID"]
        self.__myDictionary["Flight Number"] = dictionary["Flight number"]
        self.__myDictionary["Airplane ID"] = dictionary["Airplane ID"]
        self.__myDictionary["Sold Seats"] = dictionary["Sold seats"]
        self.__myDictionary["Flight Route ID"] = dictionary["Flight route ID"]
        self.__myDictionary["Flight Status"] = dictionary["Flight status"]
        self.__myDictionary["Travel Time"] = dictionary["Travel time"]
        self.__myDictionary["Departure Time"] = dictionary["Departure time"]
        self.__myDictionary["Arrival Time"] = dictionary["Arrival time"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            #print(key, val)
            returnString.append((key + ": " + val))
        return "\n".join(returnString)




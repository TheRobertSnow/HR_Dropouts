class CreateAirplane:
    def __init__(self, dictionary):
        self.__myDictionary = {}
        self.__myDictionary["airplaneId"] = dictionary["airplane id"]
        self.__myDictionary["planeReg"] = dictionary["plane reg"]
        self.__myDictionary["manufacturer"] = dictionary["manufacturer"]
        self.__myDictionary["model"] = dictionary["model"]
        self.__myDictionary["status"] = dictionary["status"]
        self.__myDictionary["numbOfSeats"] = dictionary["number of seats"]
        self.__myDictionary["odometer"] = dictionary["odometer"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            print(key, val)
            returnString.append((key + ": " + val))
        return "\n".join(returnString)



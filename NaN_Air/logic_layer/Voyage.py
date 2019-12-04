class CreateVoyage:
    def __init__(self, dictionary):
        self.__myDictionary = {}
        self.__myDictionary["Voyage Id"] = dictionary["voyage id"]
        self.__myDictionary["Flight out ID"] = dictionary["Flight out ID"]
        self.__myDictionary["Flight back ID"] = dictionary["Flight back ID"]
        self.__myDictionary["Main Pilot"] = dictionary["Main Pilot"]
        self.__myDictionary["Assisting Pilot"] = dictionary["Assisting Pilot"]
        self.__myDictionary["Main Flight Attendant"] = dictionary["Main Flight Attendant"]
        self.__myDictionary["Flight Attendants"] = dictionary["Flight Attendants"]
        self.__myDictionary["Flight Route ID"] = dictionary["Flight route ID"]
        self.__myDictionary["Departure from Is"] = dictionary["departure from is"]
        self.__myDictionary["Departure to Is"] = dictionary["departure to is"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)



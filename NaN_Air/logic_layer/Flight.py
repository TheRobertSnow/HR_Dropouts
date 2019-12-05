class CreateFlight:
    def __init__(self, objectDict):
        self.__myDictionary = objectDict
        
    def getID(self):
        return self.__myDictionary["flight id"]
    
    def getFlightRouteID(self):
        return self.__myDictionary["flight route id"]
    
    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

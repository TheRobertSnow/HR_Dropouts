class CreateFlight:
    def __init__(self, objectDict):
        self.__myDictionary = objectDict
        
    def getID(self):
        return self.__myDictionary["Flight ID"]
    
    def getFlightNumber(self):
        return self.__myDictionary["Flight number"]
    
    def getOriginID(self):
        return self.__myDictionary["Origin ID"]
    
    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

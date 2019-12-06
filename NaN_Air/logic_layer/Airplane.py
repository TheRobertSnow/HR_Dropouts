class CreateAirplane:
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.airplaneReg = dictionary["Airplane registration number"]

    def getReg(self):
        return self.__myDictionary["plane reg"]

    def __str__(self):
        returnList = []
        for key, val in self.__myDictionary.items():
            returnList.append(str(key) + ": " + str(val))
        return " | ".join(returnList)



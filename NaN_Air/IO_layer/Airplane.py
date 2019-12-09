class Airplane:
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.__planereg = dictionary["Plane registration"]

    """def getReg(self):
        return dictionary["Plane registration"]"""

    def __str__(self):
        returnList = []
        for key, val in self.__myDictionary.items():
            returnList.append(str(key) + ": " + str(val))
        return " | ".join(returnList)



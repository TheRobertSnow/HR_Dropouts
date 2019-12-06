class CreateVoyage:
    def __init__(self, dictionary):
        self.__myDictionary = dictionary

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)



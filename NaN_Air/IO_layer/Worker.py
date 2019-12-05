class Worker():
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.__workerID = dictionary['Worker ID']
        self.__socialSecurityNumber = dictionary['Social security number']
        self.__name = dictionary["Name"]
        self.__position = dictionary["Position"]
        self.__rank = dictionary["Rank"]
        self.__planeLicence = dictionary["Plane licence"]
        self.__address = dictionary["Address"]
        self.__phone = dictionary["Phone"]
        self.__cellphone = dictionary["Cellphone"]
        self.__email = dictionary["Email"]
        self.__active = dictionary["Active"]
        self.__available = dictionary["Available"]


    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

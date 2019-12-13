class Worker():
    def __init__(self, dictionary):
        self.myDictionary = dictionary
        self.workerID = dictionary['Worker ID']
        self.socialSecurityNumber = dictionary['Social security number']
        self.name = dictionary["Name"]
        self.position = dictionary["Position"]
        self.rank = dictionary["Rank"]
        self.planeLicence = dictionary["Plane licence"]
        self.address = dictionary["Address"]
        self.phone = dictionary["Phone"]
        self.cellphone = dictionary["Cellphone"]
        self.email = dictionary["Email"]
        self.active = dictionary["Active"]
        self.available = dictionary["Available"]

    def updateValue(self, key, newValue):
        self.myDictionary[key] = newValue


    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

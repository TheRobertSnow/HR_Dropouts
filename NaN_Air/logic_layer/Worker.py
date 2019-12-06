class CreateWorker:
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        #self.socialSecurityNumber = dictionary["Social Security Number"]
        self.name = dictionary["Name"]
        self.position = dictionary["Position"]
        self.planelicense = dictionary["Plane License"]
        self.address = dictionary["Address"]
        self.phone = dictionary["Phone"]
        self.cellphone = dictionary["Cellphone"]
        self.email = dictionary["Email"]
        self.active = dictionary["Active"]
        self.available = dictionary["Available"]
        
    def __str__(self): 
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)
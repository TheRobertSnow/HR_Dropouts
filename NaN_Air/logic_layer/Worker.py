class Worker():
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.socialSecurityNumber = dictionary["Social security number"]
        self.position = dictionary["Position"]
        



        self.__myDictionary = {}
        self.__myDictionary["Social Security Number"] = dictionary['social security number']
        self.__myDictionary['Name'] = dictionary["name"]
        self.__myDictionary["Position"] = dictionary["position"]
        self.__myDictionary["Rank"] = dictionary["rank"]
        self.__myDictionary["Plane License"] = dictionary["plane license"]
        self.__myDictionary["Address"] = dictionary["address"]
        self.__myDictionary["Phone"] = dictionary["phone"]
        self.__myDictionary["Cellphone"] = dictionary["cellphone"]
        self.__myDictionary["Email"] = dictionary["email"]
        self.__myDictionary["Active"] = dictionary["active"]
        self.__myDictionary["Available"] = dictionary["available"] 


    def getSSN(self):
        return self.__myDictionary["Social Security Number"]

    def getPosition(self):
        return self.__myDictionary["Position"]

    def getRank(self):
        return self.__myDictionary["Rank"]
    
    def getplaneLicense(self):
        return self.__myDictionary["Plane License"] 

    def __str__(self): 
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

#dict1 = {"social security number": "9999999999", "name": "Elizabeth Mcfadden", "position": "Dick", "rank": "Flight Attendant", "plane license": "N/A",
#"address": "Fellsmúli 35", "phone": "8998835", "cellphone": "8998835", "email": "test@test.com", "active": "True", "available": "True"}

#Elize = Worker(dict1)
#print(Elize)
#print(Elize.getSSN())
#print(Elize.getPosition())
#print(Elize.getRank())
#print(Elize.getplaneLicense())

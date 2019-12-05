class Worker():
    def __init__(self, dictionary):
        self.__myDictionary = dictionary
        self.socialSecurityNumber = dictionary["Social Security Number"]
        self.position = dictionary["Position"]
        self.rank = dictionary["Rank"]
        self.planelicense = dictionary["Plane License"]
        


    def __str__(self): 
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

#dict1 = {"Social Security Number": "9999999999", "Name": "Elizabeth Mcfadden", "Position": "Dick", "Rank": "Flight Attendant", "Plane License": "N/A",
#"Address": "Fellsmúli 35", "Phone": "8998835", "Cellphone": "8998835", "Email": "test@test.com", "Active": "True", "Available": "True"}

#Elize = Worker(dict1)
#print(Elize)
#print(Elize.socialSecurityNumber)
#print(Elize.position)
#print(Elize.rank)
#print(Elize.planelicense)

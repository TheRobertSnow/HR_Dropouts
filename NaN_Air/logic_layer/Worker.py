class Worker():
    def __init__(self, dictionary):
        self.__myDictionary = {}
        self.__myDictionary["Social security number"] = dictionary['social security number']
        self.__myDictionary['Name'] = dictionary["name"]
        self.__myDictionary["Position"] = dictionary["position"]
        self.__myDictionary["Address"] = dictionary["address"]
        self.__myDictionary["Phone"] = dictionary["phone"]
        self.__myDictionary["Cellphone"] = dictionary["cellphone"]
        self.__myDictionary["Email"] = dictionary["email"]
        self.__myDictionary["Active"] = dictionary["active"]
        self.__myDictionary["Available"] = dictionary["available"] 
        self.__myDictionary["Plane Licence"] = dictionary["plane licence"]



    def __str__(self): 
        
        returnString = []
        for key, val in self.__myDictionary.items():
            returnString.append((key + ": " + val))
        return "\n".join(returnString)
worker = Worker(workerDict)
print(worker)

class CreateVoyage:
    def __init__(self, dictionary):
        self.__myDictionary = {}
        self.__myDictionary["Voyage Id"] = dictionary["voyage id"]
        self.__myDictionary["Flight out ID"] = dictionary["Flight out ID"]
        self.__myDictionary["Flight back ID"] = dictionary["Flight back ID"]
        self.__myDictionary["Main Pilot"] = dictionary["Main Pilot"]
        self.__myDictionary["Assisting Pilot"] = dictionary["Assisting Pilot"]
        self.__myDictionary["Main Flight Attendant"] = dictionary["Main Flight Attendant"]
        self.__myDictionary["Flight Attendants"] = dictionary["Flight Attendants"]
        self.__myDictionary["Flight Route ID"] = dictionary["Flight route ID"]
        self.__myDictionary["Departure from Is"] = dictionary["departure from is"]
        self.__myDictionary["Departure to Is"] = dictionary["departure to is"]

    def __str__(self):
        returnString = []
        for key, val in self.__myDictionary.items():
            print(key, val)
            returnString.append((key + ": " + val))
        return "\n".join(returnString)

"""dict1 = {'voyage id': '1', 'Flight out ID': '3', 'Flight back ID': '4', 'Main Pilot': '101013641', 'Assisting Pilot': '101233641', 'Main Flight Attendant': '101233444', 
'Flight Attendants': '["1212886219", "1111435259"]', 'Flight route ID': '5', 'departure from is': '14:00', 'departure to is': '18:00'}"""

#voyage = CreateVoyage(dict1)
#print(voyage)


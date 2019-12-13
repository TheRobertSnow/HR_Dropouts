import csv
FILENAME = "DataFiles/airplane.csv"

def convert_to_dict(aList):
    """Function converts list to dict"""
    orderedDict = {}
    orderedDict['Plane registration'] = aList[0]
    orderedDict['Manufacturer'] = aList[1]
    orderedDict['Model'] = aList[2]
    orderedDict['Status'] = aList[3]
    orderedDict['Seats'] = aList[4]
    orderedDict['Odometer'] = aList[5]
    return orderedDict

class AirplaneIO:

    def __init__(self):
        self.__dictList = []
        self.airplaneList = []
        self.get_airplanes_from_file()
        self.create_airplane_instances()
    
    def getCertainAirplane(self, airplaneReg):
        """checks all current airplanes in the csv file and returns the instance that matches
            takes in the object instance and the reg of the object you need."""
        self.get_airplanes_from_file()
        self.create_airplane_instances()
        for instance in self.airplaneList:
            if instance.planeRegistration.lower() == airplaneReg.lower():
                return instance
        return "Airplane with registration number {} not found!".format(airplaneReg)
    
    def get_airplanes(self):
        """Return a list of plane instances"""
        return self.airplaneList

    def get_airplanes_from_file(self):
        """Only use for initializing AirplaneIO.
        Get airplanes from file in a list of dictionaries"""
        dictList = []

        with open(FILENAME, 'r', encoding="utf8") as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            for line in csvReader:
                dictList.append(line)
        self.__dictList = dictList
        for dictionary in self.__dictList:
            airplane = Airplane(dictionary)
            self.airplaneList.append(airplane)
        return self.airplaneList

    def write_airplane_to_file(self, aList):
        """Method takes in a list of data and writes to file"""
        with open(FILENAME, 'a', encoding="utf8", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            orderedDict = convert_to_dict(aList)
            self.__dictList.append(orderedDict)
            airplaneInstance = self.add_airplane_instance(orderedDict)
            newList = []
            [newList.append(i) for i in aList]
            csvWriter.writerow(newList)
        return airplaneInstance
    

    def write_dictList_to_file(self):
        """Method overwrites file with data from dictList"""
        with open(FILENAME, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Plane registration'
                , 'Manufacturer'
                , 'Model'
                , 'Status'
                , 'Seats'
                , 'Odometer']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in self.__dictList:
                writer.writerow(dictionary)

    def update_data_in_file(self, aList):
        """Method takes in list of data, updates the dictionary list
        and writes the changes to file"""
        col, val = aList[1], aList[2] # The column of the desired value and the value
        for index, dictionary in enumerate(self.__dictList):
            for key, value in dictionary.items():
                if key == 'Plane registration':
                    if value == aList[0]:
                        if col != "Plane registration":
                            for i in self.airplaneList:
                                if i.planeRegistration == aList[0]:
                                    if col == "Manufacturer":
                                        i.manufacturer = val
                                    elif col == "Model":
                                        i.model = val
                                    elif col == "Status":
                                        i.status = val
                                    elif col == "Seats":
                                        i.seats = val
                                    elif col == "Odometer":
                                        i.odometer = val
                                    elif col == "Email":
                                        i.email = val
                                    elif col == "Active":
                                        i.active = val
                                    elif col == "Available":
                                        i.available = val
                                    self.__dictList[index][col] = val
                                    self.write_dictList_to_file()
                                    self.get_airplanes_from_file()
                                    self.create_airplane_instances()
                                    return i

    def create_airplane_instances(self):
        """Method runs through list of dictionaries,
        creates an instance of worker and appends to the list."""
        self.airplaneList = []
        for dictionary in self.__dictList:
            airplane = Airplane(dictionary)
            self.airplaneList.append(airplane)
    
    def add_airplane_instance(self, dict):
        airplane = Airplane(dict)
        self.airplaneList.append(airplane)
        return airplane

    def createNewAirplane(self, airplaneList):
        """creates a new airplane instance and writes the airplane to the csv, then it returns the new
            airplane object"""
        airplaneList.insert(3, "Grounded")
        airplane = self.write_airplane_to_file(airplaneList)
        return airplane  # returns the new object

    def UpdateCertainAirplane(self, planeInstance, newStatus):
        """takes in the instance of a plane and the new status, updates the instance and the file then returns
            the updated instance"""
        planeInstance = AirplaneIO.update_data_in_file(self, [planeInstance.planeRegistration, "Status", newStatus])
        return planeInstance

class Airplane:
    def __init__(self, dictionary):
        self.myDictionary = dictionary
        self.planeRegistration = dictionary['Plane registration']
        self.manufacturer = dictionary['Manufacturer']
        self.model = dictionary["Model"]
        self.status = dictionary["Status"]
        self.seats = dictionary["Seats"]
        self.odometer = dictionary["Odometer"]

    def updateStatus(self, newStatus):
        self.myDictionary["Status"] = newStatus

    def __str__(self):
        returnString = []
        for key, val in self.myDictionary.items():
            returnString.append((key + ": " + str(val)))
        return "\n".join(returnString)

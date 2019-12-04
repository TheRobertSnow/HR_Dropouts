import UIAPI
class Create:
    def __init__(self):
        self.object = UIAPI.UIAPI()
    def createFlight(self, airplane = None, origin = None, destination = None):
        flightList = []
        if airplane == None:
            airplane = input("  - Airplane registration number: ")
        flightList.append(airplane)
        if origin == None:
            origin = input("  - Origin airport name: ")
        flightList.append(origin)
        if destination == None:
            destination = input("  - Destination airport name: ")
        flightList.append(destination)
        departureTime = input("  - Departure time from {}(f.x. 12:30): ".format(origin))
        departureDate = input("  - Departure date from {}(f.x. 24/12/2019): ".format(origin))
        departureDateTime = departureDate + "T" + departureTime + ":00"
        flightList.append(departureDateTime)
        return flightList
    
    def addCrew(self):
        print("\nAdd Crew")
        crewList = []
        mainPilot = int(input("  - Main pilot social security number: "))
        assistingPilot = int(input("  - Assisting pilot social security number: "))
        mainFlightAttendant = int(input("  - Main flight attendant social security number: "))
        flightAttendants = []
        while True:
            flightAttendant = input("  - Flight attendant social security number(q to stop adding attendants): ")
            flightAttendant = flightAttendant.lower()
            if flightAttendant == "q":
                break
            else:
                flightAttendants.append(flightAttendant)
        crewList.append(mainPilot)
        crewList.append(assistingPilot)
        crewList.append(mainFlightAttendant)
        crewList.append(flightAttendants)
        return crewList
    
    def createVoyageMenu(self):
        print('''4. Create Voyage
--------------------------------------------
1. Create Voyage using existing flights
2. Create Voyage by creating 2 flights
--------------------------------------------''')
        createVoyageMenuInput = input("Input choice(q to Quit, b for Back): ")
        createVoyageMenuInput = createVoyageMenuInput.lower()
        if createVoyageMenuInput == "1":
            print('''4.1. Create Voyage using existing flights
--------------------------------------------
Please input the following information:''')
            voyageList = []
            flightOutId = int(input("  - Flight from iceland id: "))
            voyageList.append(flightOutId)
            flightBackId = int(input("  - Flight to iceland id: "))
            voyageList.append(flightBackId)
            #gets the flights and validates  that they exist
            crewList = Create.addCrew(self)
            voyageList.append(crewList)
            print("Crew successfully Added!")
            #prints out crew info
            print(crewList)
            print("Voyage successfully created!")
            #Prints out Voyage info
            print(voyageList)
            print("--------------------------------------------")
            return createVoyageMenuInput
        elif createVoyageMenuInput == "2":
            print('''4.2. Create Voyage by creating 2 flights
--------------------------------------------
Please input the following information:''')
            voyageList2 = []
            print("\nFlight from Iceland")
            flightList = Create.createFlight(None,"Reykjavíkurflugvöllur")
            #creates flight1
            #finds id of created flight
            voyageList2.append("123")
            #voyageList2.append(flightOutId)
            print("Flight 1 successfully created!")
            print(flightList)
            
            print("\nFlight to Iceland")
            flightList = Create.createFlight(flightList[0],flightList[2],flightList[1])
            #creates flight2
            #finds id of created flight
            voyageList2.append("124")
            #voyageList2.append(flightBackId)
            print("Flight 2 successfully created!")
            print(flightList)
            #print(flightBackList)
            
            crewList = Create.addCrew(self)
            print("Crew successfully Added!")
            #prints out crew info
            print(crewList)
            
            voyageList2.append(crewList)
            print("Voyage successfully created!")
            #Prints out Voyage info
            print(voyageList2)
            print("--------------------------------------------")
            return createVoyageMenuInput
        elif createVoyageMenuInput == "b":
            return createVoyageMenuInput
        elif createVoyageMenuInput == "q":
            return createVoyageMenuInput
        else:
            print("Wrong input, try again")
            createVoyageMenuInput = Create.createVoyageMenu(self)
        return createVoyageMenuInput
            
    def createMenu(self):
        print('''Create Data
--------------------------------------------
  1. Create Worker
  2. Create Airplane
  3. Create Flight Route
  4. Create Voyage
  5. Create Flight
--------------------------------------------''')
        
        createMenuInput = input("Input choice(q to Quit, b for Back): ")
        createMenuInput = createMenuInput.lower()
        if createMenuInput == "1":
            print('''1. Create Worker
--------------------------------------------
Please input the following information:''')
            createWorkerList = []
            ssn = int(input("  - Social security number: "))
            createWorkerList.append(ssn)
            name = input("  - Name: ")
            createWorkerList.append(name)
            print('''\n  Select worker position\n
    1. Main Pilot
    2. Assisting Pilot
    3. Main Flight Attendant
    4. Flight Attendant''')
            position = input("  Input choice: ")
            createWorkerList.append(position)
            address = input("  - Address: ")
            createWorkerList.append(address)
            phone = int(input("  - Phone: "))
            createWorkerList.append(phone)
            cellphone = int(input("  - Cellphone: "))
            createWorkerList.append(cellphone)
            email = input("  - Email: ")
            createWorkerList.append(email)
            planeLicence = input("  - Plane Licence: ")
            createWorkerList.append(planeLicence)
            print("Worker successfully created!")
            print(createWorkerList)
            #Prints out info on the created worker
            print("--------------------------------------------")
            createMenuInput = Create.createMenu(self)
        elif createMenuInput == "2":
            print('''2. Create Airplane
--------------------------------------------
Please input the following information:''')
            createAirplaneList = []
            planeReg = input("  - Plane registration number: ")
            createAirplaneList.append(planeReg)
            manufacturer = input("  - Manufacturer: ")
            createAirplaneList.append(manufacturer)
            model = input("  - Model: ")
            createAirplaneList.append(model)
            numberOfSeats = int(input("  - Number of seats: "))
            createAirplaneList.append(numberOfSeats)
            odometer = int(input("  - Odometer(number of km the airplane has travelled): "))
            createAirplaneList.append(odometer)
            print("Request sent in...\n")
            #
            #
            #
            result = UIAPI.UIAPI.newPlaneRequest(self.object, createAirplaneList)
            print(result)
            print(self.object)
            #
            #
            #
            #Prints info on the created airplane
            print("--------------------------------------------")
            createMenuInput = Create.createMenu(self)
        elif createMenuInput == "3":
            print('''3. Create Flight Route
--------------------------------------------
Please input the following information:''')
            createFlightRouteList = []
            country = input("  - Country: ")
            createFlightRouteList.append(country)
            airport = input("  - Airport: ")
            createFlightRouteList.append(airport)
            flightDistance = int(input("  - Flight distance(in km f.x. 640): "))
            createFlightRouteList.append(flightDistance)
            travelTime = input("  - Travel time(hours:minutes f.x. 4:20): ")
            createFlightRouteList.append(travelTime)
            emergencyContact = input("  - Emergency contact name: ")
            createFlightRouteList.append(emergencyContact)
            emergencyNumber = int(input("  - Emergency contact phonenumber: "))
            createFlightRouteList.append(emergencyNumber)
            print("Flight Route successfully created!")
            print(createFlightRouteList)
            #Prints the created flight route
            print("--------------------------------------------")
            createMenuInput = Create.createMenu(self)
        elif createMenuInput == "4":
            createVoyageMenuOutput = Create.createVoyageMenu(self)
            if createVoyageMenuOutput == "b":
                createMenuInput = Create.createMenu(self)
            elif createVoyageMenuOutput == "q":
                return createVoyageMenuOutput
            else:
                createMenuInput = Create.createMenu(self)
        elif createMenuInput == "5":
            print('''5. Create Flight
--------------------------------------------
Please input the following information:''')
            flightList = Create.createFlight(self)
            print("Flight successfully created!")
            print(flightList)
            #Prints the created flight
            print("--------------------------------------------")
            createMenuInput = Create.createMenu(self)
        elif createMenuInput == "b":
            return createMenuInput
        elif createMenuInput == "q":
            return createMenuInput
        else:
            print("Wrong input, try again")
            createMenuInput = Create.createMenu(self)
        return createMenuInput

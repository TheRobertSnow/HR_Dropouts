import UIAPI
import datetime

def printObject(name):
    if type(name) == str:
        print(name)
    elif type(name) != list:
        print("")
        print(name)
        print("")
    else:
        print("kukur")
        
class Create():
    def __init__(self):
        self.uiapi = UIAPI.UIAPI()

    def createFlight(self, airplane=None, origin=None, destination=None):
        """format for creating a new flight, used in both create flight and create voyage
            returns a list with all values required for creating a flight"""
        flightList = []
        if airplane == None:
            airplane = input("  - Airplane registration number: ")
            checkReg = UIAPI.UIAPI.viewCertainAirplane(self, airplane)
            if type(checkReg) == str:
                print(checkReg)
                return "failed"
        flightList.append(airplane)
        if origin == None:
            while True:
                origin = input("  - Origin ID: ")
                testOrigin = UIAPI.UIAPI.viewFlightRoute(self, origin)
                if type(testOrigin) != str:
                    break
                print("ID not found, please try again")
        flightList.append(origin)
        if destination == None:
            while True:
                destination = input("  - Destination ID: ")
                testDest = UIAPI.UIAPI.viewFlightRoute(self, destination)
                if type(testDest) != str:
                    break
                print("ID not found, please try again")
        flightList.append(destination)
        hour, minute, day, month, year = None,None,None,None,None
        while True:
            try:
                departureTime = input("  - Departure time from {}(f.x. 12:30): ".format(origin))
                #væri betra að hafa þetta shit í logic
                hour, minute = map(int, departureTime.split(':'))
                break
            except Exception as e:
                print("Wrong time format!")
        while True:
            try:
                departureDate = input("  - Departure date from {}(f.x. 24/12/2019): ".format(origin))
                #þetta líka
                day, month, year = map(int, departureDate.split('/'))
                break
            except Exception as e:
                print("Wrong date format!")

        departureDateTime = datetime.datetime(year, month, day, hour, minute, 00)
        flightList.append(departureDateTime)
        return flightList

    def addCrew(self, flightID, secondFlightID):
        # get date of both flights.
        dateOut = UIAPI.UIAPI.getDateFromFlightID(self, flightID)
        dateBack = UIAPI.UIAPI.getDateFromFlightID(self, secondFlightID)
        print("\nAdd Crew")
        captain = input("  - Captains social security number: ")
        results = UIAPI.UIAPI.verifyStaffForVoyage(self, "Captain", captain, dateOut, dateBack, flightID)
        if type(results) == str:
            print(results)
            print("You can try adding a captain later in the update menu, for now the captain is empty")
            captain = ""
        copilot = input("  - Copilots social security number: ")
        results = UIAPI.UIAPI.verifyStaffForVoyage(self, "Copilot", copilot, dateOut, dateBack, flightID)
        if type(results) == str:
            print(results)
            print("You can try adding a Copilot later in the update menu, for now the captain is empty")
            copilot = ""
        flightServiceManager = input("  - Flight service managers social security number: ")
        results = UIAPI.UIAPI.verifyStaffForVoyage(self, "Flight Service Manager", flightServiceManager, dateOut, dateBack, flightID)
        if type(results) == str:
            print(results)
            print("You can try adding a Manager later in the update menu, for now the captain is empty")
            flightServiceManager = ""
        flightAttendants = ""
        while True:
            flightAttendant = input("  - Flight attendants social security number(q to stop adding attendants): ")
            flightAttendant = flightAttendant.lower()
            if flightAttendant == "q":
                break
            else:
                results = UIAPI.UIAPI.verifyStaffForVoyage(self, "Flight Attendant", flightAttendant, dateOut, dateBack, flightID)
                if type(results) == str:
                    print(results)
                else:
                    if len(flightAttendants) == 0:
                        flightAttendants = flightAttendant
                    else:
                        flightAttendants += "/" + flightAttendant
        return captain, copilot, flightServiceManager, flightAttendants

    def createVoyageMenu(self):
        print('''4. Create voyage
--------------------------------------------
  1. Create voyage using existing flights
  2. Create voyage by creating 2 flights
  3. Create duplicates of an existing voyage.
--------------------------------------------''')
        createVoyageMenuInput = input("Input choice(q to Quit, b for Back): ")
        createVoyageMenuInput = createVoyageMenuInput.lower()
        if createVoyageMenuInput == "1":
            print('''4.1. Create voyage using existing flights
--------------------------------------------
Please input the following information:''')
            voyageList = []
            flightOutId = input("  - Flight from Iceland ID: ")
            # validate flight out id exists and isn't being used
            validID = UIAPI.UIAPI.viewCertainFlightByID(self, flightOutId)
            if type(validID) == str:
                print("\nError! that flight ID doesn't exist.\n")
                return createVoyageMenuInput
            usedID = UIAPI.UIAPI.checkIfAlreadyUsed(self, flightOutId)
            if usedID:
                print("\nError! that flight ID is already being used by another voyage.\n")
                return createVoyageMenuInput
            voyageList.append(flightOutId)
            flightBackId = input("  - Flight to Iceland ID: ")
            # validate flight back id exists and isn't being used
            validID = UIAPI.UIAPI.viewCertainFlightByID(self, flightBackId)
            if type(validID) == str:
                print("\nError! that flight ID doesn't exist.\n")
                return createVoyageMenuInput
            usedID = UIAPI.UIAPI.checkIfAlreadyUsed(self, flightBackId)
            if usedID:
                print("\nError! that flight ID is already being used by another voyage.\n")
                return createVoyageMenuInput
            voyageList.append(flightBackId)


            # adds crew
            addCrewInput = input("  - Do you want to add a crew to the voyage? (y/n)")
            if addCrewInput.lower() == "y":
                captain, copilot, flightServiceManager, flightAttendants = Create.addCrew(self, flightOutId, flightBackId)
            elif addCrewInput.lower() == "n":
                captain, copilot, flightServiceManager, flightAttendants = "", "", "", ""
            # prints out crew info
            print(captain, copilot, flightServiceManager, flightAttendants)
            voyageList.insert(2, captain)
            voyageList.insert(3, copilot)
            voyageList.insert(4, flightServiceManager)
            voyageList.insert(5, flightAttendants)
            voyageInstance = UIAPI.UIAPI.createNewVoyage(self, voyageList)
            # Prints out Voyage info
            printObject(voyageInstance)
            print("--------------------------------------------")
            return createVoyageMenuInput

        elif createVoyageMenuInput == "2":
            print('''4.2. Create voyage by creating 2 flights
--------------------------------------------
Please input the following information:''')
            voyageList2 = []
            print("\nFlight from Iceland")
            # Get a list of information for the flight
            flightList = "failed"
            while flightList == "failed":
                flightList = Create.createFlight(self, None, "1")  # Sends in the id of Reykjavik airport
            # creates flight1
            flightInstance1 = UIAPI.UIAPI.createNewFlight(self, flightList)
            print(flightInstance1)
            # finds id of created flight
            try:
                voyageList2.append(flightInstance1.flightID)
            except AttributeError:
                return createVoyageMenuInput
            # voyageList2.append(flightOutId)
            #print("Flight 1 successfully created!")

            print("\nFlight to Iceland")
            # Get a list of information for the flight
            flightList2 = "failed"
            while flightList2 == "failed":
                flightList2 = Create.createFlight(self, flightList[0], flightList[2], flightList[1])
            # creates flight2
            flightInstance2 = UIAPI.UIAPI.createNewFlight(self, flightList2)
            printObject(flightInstance2)
            # finds id of created flight
            try:
                voyageList2.append(flightInstance2.flightID)
            except AttributeError:
                return createVoyageMenuInput
            # voyageList2.append(flightBackId)
            #print("Flight 2 successfully created!")
            # print(flightBackList)
            addCrewInput = input("  - Do you want to add a crew to the voyage? (y/n)")
            if addCrewInput.lower() == "y":
                # get flight ids
                supposedNextID = UIAPI.UIAPI.nextFlightID(self)
                flight1ID = int(supposedNextID)-1
                flight2ID = int(supposedNextID)-2
                captain, copilot, flightServiceManager, flightAttendants = Create.addCrew(self, flight1ID, flight2ID)
            elif addCrewInput.lower() == "n":
                captain, copilot, flightServiceManager, flightAttendants = "", "", "", ""
            # prints out crew info
            print(captain, copilot, flightServiceManager, flightAttendants)
            voyageList2.insert(2, captain)
            voyageList2.insert(3, copilot)
            voyageList2.insert(4, flightServiceManager)
            voyageList2.insert(5, flightAttendants)
            voyageInstance = UIAPI.UIAPI.createNewVoyage(self, voyageList2)
            # Prints out Voyage info
            printObject(voyageInstance)
            return createVoyageMenuInput

        elif createVoyageMenuInput == "3":  # Duplicate old voyage.
            print("""Create duplicate voyage(s) from existing voyages.
Begin by selecting ID of a existing voyage.
--------------------------------------------""")
            userInput = input(" - Input voyage ID: ")
            while True:
                voyageExists = UIAPI.UIAPI.checkVoyageExists(self, userInput)
                if voyageExists == True:
                    break
                else:
                    userInput = input("Voyage does not exist...\n - Input voyage ID: ")
            dateList = []
            while True:
                dateInput = input(" - Input date(e.g. 07/03/2019, s to stop): ")
                if dateInput.lower() == "s":
                    break
                else:
                    try:
                        day, month, year = map(int, dateInput.split('/'))
                        dateInput = datetime.datetime(year, month, day)
                        dateList.append(dateInput)
                    except:
                        print("Invalid date input, please try again!")
            argumentList = [userInput, dateList]
            returnMessage = UIAPI.UIAPI.createDuplicateVoyages(self, argumentList)
            printObject(returnMessage)
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
            ssn = input("  - Social security number: ")
            createWorkerList.append(ssn)
            name = input("  - Name: ")
            createWorkerList.append(name)
            print('''\n  Select worker position
    1. Captain
    2. Copilot
    3. Flight Service Manager
    4. Flight Attendant
    5. Staff Manager
    6. Trip Manager''')
            position = input("  - Input choice: ")
            planeLicence = ""
            if position == "1":
                createWorkerList.append("Captain")
                planeLicence = input("  - Plane licence: ")
            elif position == "2":
                createWorkerList.append("Copilot")
                planeLicence = input("  - Plane licence: ")
            elif position == "3":
                createWorkerList.append("Flight Service Manager")
            elif position == "4":
                createWorkerList.append("Flight Attendant")
            elif position == "5":
                createWorkerList.append("Staff Manager")
            elif position == "6":
                createWorkerList.append("Trip Manager")
            else:
                createWorkerList.append("Stupid User")
            createWorkerList.append(planeLicence)
            address = input("  - Address: ")
            createWorkerList.append(address)
            #ekki int
            phone = input("  - Phone: ")
            createWorkerList.append(phone)
            #ekki int
            cellphone = input("  - Cellphone: ")
            createWorkerList.append(cellphone)
            #email error checka ?
            email = input("  - Email: ")
            createWorkerList.append(email)
            result = UIAPI.UIAPI.createNewWorker(self, createWorkerList)
            printObject(result)
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
            numberOfSeats = input("  - Number of seats: ")
            createAirplaneList.append(numberOfSeats)
            odometer = input("  - Odometer(number of km the airplane has travelled): ")
            createAirplaneList.append(odometer)
            result = UIAPI.UIAPI.createNewAirplane(self, createAirplaneList)
            printObject(result)
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
            flightDistance = input("  - Flight distance(in km f.x. 640): ")
            createFlightRouteList.append(flightDistance)
            travelTime = input("  - Travel time(hours:minutes f.x. 4:20): ")
            createFlightRouteList.append(travelTime)
            emergencyContact = input("  - Emergency contact name: ")
            createFlightRouteList.append(emergencyContact)
            emergencyNumber = input("  - Emergency contact phonenumber: ")
            createFlightRouteList.append(emergencyNumber)
            result = UIAPI.UIAPI.createNewFlightRoute(self, createFlightRouteList)
            printObject(result)
            # Prints the created flight route
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

            flightRouteList = UIAPI.UIAPI.viewAllFlightRoutes(self)
            for item in flightRouteList:
                print(item.flightRouteID, item.country)
            flightList = "failed"
            while flightList == "failed":
                flightList = Create.createFlight(self)  # Creates a list for createNewFlight
            result = UIAPI.UIAPI.createNewFlight(self, flightList)
            printObject(result)
            createMenuInput = Create.createMenu(self)
        elif createMenuInput == "b":
            return createMenuInput
        elif createMenuInput == "q":
            return createMenuInput
        else:
            print("Wrong input, try again")
            createMenuInput = Create.createMenu(self)
        return createMenuInput

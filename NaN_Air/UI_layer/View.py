import UIAPI

def printObjects(self, name):
    for count, theObject in enumerate(name):
        if len(name) > 4:
            if count >= 4:
                if count % 4 == 0:
                    printNext = input("\nPress any key to see next(q to quit)")
                    printNext = printNext.lower()
                    if printNext == "q":
                        return None
        print(theObject)
        print()

class View():
    def __init__(self):
        self.uiapi = UIAPI.UIAPI()
    
    def viewMenu(self):
        print('''View Data
--------------------------------------------
  1. View Worker
  2. View Airplane
  3. View Flight routes
  4. View Voyages
  5. View Flight
--------------------------------------------''')

        viewMenuInput = input("Input choice (q to Quit, b for Back): ")
        viewMenuInput = viewMenuInput.lower()
        if viewMenuInput == "1":
            viewWorkerOutput = View.viewWorker(self)
            if viewWorkerOutput == "b":
                viewMenuInput = View.viewMenu(self)
                pass
        elif viewMenuInput == "2":
            viewAirplaneOutput = View.viewAirplane(self)
            if viewAirplaneOutput == "b":
                viewMenuInput = View.viewMenu(self)
        elif viewMenuInput == "3":
            viewFlightRoutesOutput = View.viewFlightRoutes(self)
            if viewFlightRoutesOutput == "b":
                viewMenuInput = View.viewMenu(self)
        elif viewMenuInput == "4":
            viewVoyagesOutput = View.viewVoyages(self)
            if viewVoyagesOutput == "b":
                viewMenuInput = View.viewMenu(self)
        elif viewMenuInput == "5":
            viewFlightOutput = View.viewFlight(self)
            if viewFlightOutput == "b":
                viewMenuInput = View.viewMenu(self)
        elif viewMenuInput == "b":
            return viewMenuInput
        elif viewMenuInput == "q":
            return viewMenuInput
        else:
            print("Wrong input, try again!")
            viewMenuInput = View.viewMenu(self)
        return viewMenuInput

    def viewWorker(self): #Pæling hvort að við sleppum view all Bosses??
        print('''1. View Worker
--------------------------------------------
  1. View Pilots
  2. View Attendants
  3. View Bosses
  4. View All Staff
--------------------------------------------''')

        viewWorkerInput = input("Input choice (q to Quit, b for Back): ")
        viewWorkerInput = viewWorkerInput.lower()
        if viewWorkerInput == "1":
            viewPilotsOutput = View.viewPilots(self)
            if viewPilotsOutput == "b":
                viewWorkerInput = View.viewWorker(self)
            elif viewPilotsOutput == "q":
                return viewWorkerInput
            else:
                viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "2":
            viewAttendantsOutput = View.viewAttendants(self)
            if viewAttendantsOutput == "b":
                viewWorkerInput = View.viewWorker(self)
            elif viewAttendantsOutput == "q":
                return viewWorkerInput
            else:
                viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "3":
            viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "4":
            allStaff = UIAPI.UIAPI.viewAllWorkers(self)
            printObjects(self, allStaff)
            viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "b":
            return viewWorkerInput
        elif viewWorkerInput == "q":
            return viewWorkerInput
        else:
            print("Wrong input, try again")
            viewWorkerInput = View.viewWorker(self)
        return viewWorkerInput

# Pilots
    def viewPilots(self):
        print('''1.1. View Pilots
--------------------------------------------
  1. View specific pilot
  2. View all pilots
  3. View all pilots who are not working on 
     specific date
  4. View all pilots who are working on 
     specific date
--------------------------------------------''')
        viewPilotsInput = input("Input choice (q to Quit, b for Back): ")
        viewPilotsInput = viewPilotsInput.lower()
        if viewPilotsInput == "1":
            pilotSSN = input("Input SSN: ")
            pilot = UIAPI.UIAPI.viewWorkerBySSn(self, pilotSSN, "Pilot")
            printObjects(self, pilot)
            return viewPilotsInput
        elif viewPilotsInput == "2":
            allPilots = UIAPI.UIAPI.viewWorkerByPOS(self, "Pilot")
            printObjects(self, allPilots)
            return viewPilotsInput
        elif viewPilotsInput == "3":
            pilotDate = input("Input date: ")
            availablePilots = UIAPI.UIAPI.listAvailableWorkersbydate(self, pilotDate, "Pilot")
            printObjects(self, availablePilots)
            return viewPilotsInput
        elif viewPilotsInput == "4":
            pilotDate = input("Input date: ")
            unavailableAttendants = UIAPI.UIAPI.listUnavailableWorkersbydate(self, pilotDate, "Attendant")
            printObjects(self,unavailableAttendants)
            return viewPilotsInput
        elif viewPilotsInput == "b":
            return viewPilotsInput
        elif viewPilotsInput == "q":
            return viewPilotsInput
        else:
            print("Wrong input, try again")
        return viewPilotsInput

    def viewAttendants(self):
        print('''1.2. View Attendants
--------------------------------------------
  1. View specific attendant
  2. View all attendants
  3. View all attendants who are not working on 
     specific date
  4. View all attendants who are working on 
     specific date
--------------------------------------------''')
        viewAttendantsInput = input("Input choice (q to Quit, b for Back): ")
        viewAttendantsInput = viewAttendantsInput.lower()
        if viewAttendantsInput == "1":
            attendantSSN = input("Input SSN: ")
            Attendant = UIAPI.UIAPI.viewWorkerBySSn(self, attendantSSN, "Attendant")
            printObjects(self, Attendant)
            return viewAttendantsInput
        elif viewAttendantsInput == "2":
            allAttendants = UIAPI.UIAPI.viewWorkerByPOS(self, "Attendant")
            printObjects(self, allAttendants)
            return viewAttendantsInput
        elif viewAttendantsInput == "3":
            attendantDate = input("Input date: ")
            availableAttendants = UIAPI.UIAPI.listAvailableWorkersbydate(self, attendantDate, "Attendant")
            printObjects(self, availableAttendants)
            return viewAttendantsInput
        elif viewAttendantsInput == "4":
            attendantDate = input("Input date: ")
            unavailableAttendants = UIAPI.UIAPI.listUnavailableWorkersbydate(self, attendantDate, "Attendant")
            printObjects(self, unavailableAttendants)
            return viewAttendantsInput
        elif viewAttendantsInput == "b":
            return viewAttendantsInput
        elif viewAttendantsInput == "q":
            return viewAttendantsInput
        else:
            print("Wrong input, try again!")
        return viewAttendantsInput

    def viewAirplane(self):
        print('''2. View Airplane
--------------------------------------------
  1. View specific airplane
  2. View all airplanes
--------------------------------------------''')

        viewAirplaneInput = input("Input choice (q to Quit, b for Back): ")
        viewAirplaneInput = viewAirplaneInput.lower()
        if viewAirplaneInput == "1":
            AirplaneReg= input("Please input airplane registration: ")
            Airplane = UIAPI.UIAPI.viewCertainAirplane(self, AirplaneReg) #Ekki alveg búið fæ ekki self.__planereg = dictionary["Plane registration"] til að virka í Airplane.py
            printObjects(self, Airplane)
            return viewAirplaneInput
        elif viewAirplaneInput == "2":
            allPlanes = UIAPI.UIAPI.viewAllAirplanes(self)
            printObjects(self, allPlanes)
            return viewAirplaneInput
        elif viewAirplaneInput == "b":
            return viewAirplaneInput
        elif viewAirplaneInput == "q":
            return viewAirplaneInput
        else:
            print("Wrong input, try again!")
        return viewAirplaneInput

    def viewFlightRoutes(self):
        print('''3. View Flight Routes
--------------------------------------------
  1. View specific route
  2. View all flight routes
--------------------------------------------''')

        viewFlightRoutesInput = input("Input choice (q to Quit, b for Back): ")
        viewFlightRoutesInput = viewFlightRoutesInput.lower()
        if viewFlightRoutesInput == "1":
            flightRouteID = input("Input Flight Route ID: ")
            flightRoute = UIAPI.UIAPI.viewFlightRoute(self, flightRouteID)
            printObjects(self, flightRoute)
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        elif viewFlightRoutesInput == "2":
            allFlightRoutes = UIAPI.UIAPI.viewAllFlightRoutes(self)
            for flightRoute in allFlightRoutes:
                print(flightRoute)
                print("")
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        elif viewFlightRoutesInput == "b":
            return viewFlightRoutesInput
        elif viewFlightRoutesInput == "q":
            return viewFlightRoutesInput
        else:
            print("Wrong input, try again!")
        return viewFlightRoutesInput

    def viewVoyages(self):
        print('''4. View Voyages
--------------------------------------------
  1. View a specific voyage
  2. View all voyages
--------------------------------------------''')

        viewVoyagesInput = input("Input choice (q to Quit, b for Back): ")
        viewVoyagesInput = viewVoyagesInput.lower()
        if viewVoyagesInput == "1":
            voyageID = input("Input Voyage ID: ")
            voyage = UIAPI.UIAPI.viewVoyage(self, voyageID)
            printObjects(self, voyage)
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "2":
            voyages = UIAPI.UIAPI.viewAllVoyages(self)
            printObjects(self, voyages)
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "b":
            return viewVoyagesInput
        elif viewVoyagesInput == "q":
            return viewVoyagesInput
        else:
            print("Wrong input, try again!")
            viewVoyagesInput = View.viewVoyages(self)
        return viewVoyagesInput

    def viewFlight(self):
        print('''5. View Flights
--------------------------------------------
  1. View specific flight
  2. View all flights
  3. View active flights
  4. View cancelled flights
--------------------------------------------''')

        viewFlightInput = input("Input choice (q to Quit, b for Back): ")
        viewFlightInput = viewFlightInput.lower()
        if viewFlightInput == "1":
            flightNumber = input("Input flight number: ")
            viewFlight = UIAPI.UIAPI.viewCertainFlight(self, flightNumber)
            printObjects(self, viewFlight)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "2":
            allFlights = UIAPI.UIAPI.viewAllFlights(self)
            printObjects(self, allFlights)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "3":
            viewActiveFlights = UIAPI.UIAPI.viewFlightsByStatus(self, "Active")
            printObjects(self, viewActiveFlights)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "4":
            viewCancelledFlights = UIAPI.UIAPI.viewFlightsByStatus(self, "Cancelled")
            printObjects(self, viewCancelledFlights)
            viewFlightInput = View.viewFlight(self)
        elif viewFlightInput == "b":
            return viewFlightInput
        elif viewFlightInput == "q":
            return viewFlightInput
        else:
            print("Wrong input, try again!")
            viewFlightInput = View.viewFlight(self)
        return viewFlightInput

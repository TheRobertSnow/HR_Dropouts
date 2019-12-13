import UIAPI
import datetime

def printObjects(name):
    if type(name) == str:
        print(name)
    elif type(name) != list:
        print("")
        print(name)
        print("")
    else:
        for count, theObject in enumerate(name):
            if len(name) > 4:
                if count >= 4:
                    if count % 4 == 0:
                        printNext = input("\nPress enter to see next (q to quit):")
                        printNext = printNext.lower()
                        if printNext == "q":
                            return None
            print("")
            print(theObject)
        print("")

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

        viewMenuInput = input("Input choice (q to Quit, b for back): ")
        viewMenuInput = viewMenuInput.lower()
        if viewMenuInput == "1":
            viewWorkerOutput = View.viewWorker(self)
            if viewWorkerOutput == "b":
                viewMenuInput = View.viewMenu(self)
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

    def viewWorker(self):  
        print('''1. View Worker
--------------------------------------------
  1. View Pilots
  2. View Attendants
  3. View Managers
  4. View All Staff
--------------------------------------------''')

        viewWorkerInput = input("Input choice (q to Quit, b for back): ")
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
            if viewWorkerInput == "b":
                viewWorkerInput = View.viewWorker(self)
            elif viewAttendantsOutput == "q":
                return viewWorkerInput
            else:
                viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "3":
            viewManagersInput = View.viewManagers(self)
            if viewManagersInput == "b":
                viewWorkerInput = View.viewWorker(self)
            elif viewManagersInput == "q":
                return viewWorkerInput
            viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "4":
            allStaff = UIAPI.UIAPI.viewAllWorkers(self)
            printObjects(allStaff)
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
  5. View all voyages of a pilot in a given 
     week
  6. View all Pilots with certain 
     plane license
--------------------------------------------''')
        viewPilotsInput = input("  - Input choice (q to Quit, b for back): ")
        viewPilotsInput = viewPilotsInput.lower()
        if viewPilotsInput == "1":
            pilotSSN = input("Input SSN with no spaces in between: ")
            pilot = UIAPI.UIAPI.viewWorkerBySSn(self, pilotSSN, "Pilot")
            printObjects(pilot)
            return viewPilotsInput
        elif viewPilotsInput == "2":
            allPilots = UIAPI.UIAPI.viewWorkerByPOS(self, "Pilot")
            printObjects(allPilots)
            return viewPilotsInput
        elif viewPilotsInput == "3":
            day, month, year = None, None, None
            viewPilotDate = ""
            while True:
                viewPilotDate = input("  - Input date(f.x. 24/12/2019), b for back: ")
                if viewPilotDate == "b":
                    return viewPilotsInput
                else:
                    try:
                        day, month, year = map(int, viewPilotDate.split('/'))
                        if year > 0 and year < 3000:
                            break
                    except Exception:
                        print("Wrong input, try again!")
            viewPilotDate = datetime.datetime(year, month, day)
            availablePilots = UIAPI.UIAPI.listWorkersbydate(self, viewPilotDate, "Pilot", "Available")
            printObjects(availablePilots)
            return viewPilotsInput
        elif viewPilotsInput == "4":
            day, month, year = None, None, None
            viewPilotDate = ""
            while True:
                viewPilotDate = input("  - Input date(f.x. 24/12/2019), b for back: ")
                if viewPilotDate == "b":
                    return viewPilotsInput
                else:
                    try:
                        day, month, year = map(int, viewPilotDate.split('/'))
                        if year > 0 and year < 3000:
                            break
                    except Exception:
                        print("Wrong input, try again!")
            viewPilotDate = datetime.datetime(year, month, day)
            unavailablePilots = UIAPI.UIAPI.listWorkersbydate(self, viewPilotDate, "Pilot", "Unavailable")
            printObjects(unavailablePilots)
            return viewPilotsInput
        elif viewPilotsInput == "5":
            while True:
                pilotSSN = input("  - Input SSN with no spaces in between, b for back: ")
                if pilotSSN == "b":
                    return viewPilotsInput
                pilotYear = input("  - Input year, b for back: ")
                if pilotYear == "b":
                    return viewPilotsInput
                pilotWeek = input("  - Input week of the year, b for back: ")
                if pilotWeek == "b":
                    return viewPilotsInput
            pilotWeeklyVoyages = UIAPI.UIAPI.viewallVoyagesInWeek(self, pilotSSN, pilotYear, pilotWeek, "Pilot")
            printObjects(pilotWeeklyVoyages)
            return viewPilotsInput
        elif viewPilotsInput == "6":
            pilotLicence = input(" - Input Plane Licence: ")
            planePilots = UIAPI.UIAPI.viewWorkersByPlaneLicence(self, pilotLicence)
            printObjects(planePilots)
        elif viewPilotsInput == "b":
            return viewPilotsInput
        elif viewPilotsInput == "q":
            return viewPilotsInput
        else:
            print("Wrong input, try again")
            viewPilotsInput = View.viewPilots(self)
            #return viewPilotsInput
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
  5. View all voyages of an attendant in a given 
     week
--------------------------------------------''')
        viewAttendantsInput = input("Input choice (q to Quit, b for back): ")
        viewAttendantsInput = viewAttendantsInput.lower()
        if viewAttendantsInput == "1":
            attendantSSN = input("  - Input SSN with no spaces in between: ")
            Attendant = UIAPI.UIAPI.viewWorkerBySSn(self, attendantSSN, "Attendant")
            printObjects(Attendant)
            return viewAttendantsInput
        elif viewAttendantsInput == "2":
            allAttendants = UIAPI.UIAPI.viewWorkerByPOS(self, "Attendant")
            printObjects(allAttendants)
            return viewAttendantsInput
        elif viewAttendantsInput == "3":
            day, month, year = None, None, None
            viewAttendantDate = ""
            while True:
                viewAttendantDate = input("  - Input date(f.x. 24/12/2019), b for back: ")
                if viewAttendantDate == "b":
                    return viewAttendantsInput
                else:
                    try:
                        day, month, year = map(int, viewAttendantDate.split('/'))
                        if year > 0 and year < 3000:
                            break
                    except Exception:
                        print("Wrong input, try again!")
            viewAttendantDate = datetime.datetime(year, month, day)
            availableAttendants = UIAPI.UIAPI.listWorkersbydate(self, viewAttendantDate, "Attendant", "Available")
            printObjects(availableAttendants)
            return viewAttendantsInput
        elif viewAttendantsInput == "4":
            day, month, year = None, None, None
            viewAttendantDate = ""
            while True:
                viewAttendantDate = input("  - Input date(f.x. 24/12/2019), b for back: ")
                if viewAttendantDate == "b":
                    return viewAttendantsInput
                else:
                    try:
                        day, month, year = map(int, viewAttendantDate.split('/'))
                        if year > 0 and year < 3000:
                            break
                    except Exception:
                        print("Wrong input, try again!")
            viewAttendantDate = datetime.datetime(year, month, day)
            unavailableAttendants = UIAPI.UIAPI.listWorkersbydate(self, viewAttendantDate, "Attendant", "Unavailable")
            printObjects(unavailableAttendants)
            return viewAttendantsInput
        elif viewAttendantsInput == "5":
            attendantSSN = input("  - Input SSN with no spaces in between: ")
            attendantYear = input("  - Input year: ")
            attendantWeek = input("  - Input week of the year: ")
            attendantWeeklyVoyages = UIAPI.UIAPI.viewallVoyagesInWeek(self, attendantSSN, attendantYear, attendantWeek, "Attendant")
            printObjects(attendantWeeklyVoyages)
            return viewAttendantsInput
        elif viewAttendantsInput == "b":
            return viewAttendantsInput
        elif viewAttendantsInput == "q":
            return viewAttendantsInput
        else:
            print("Wrong input, try again!")
            viewAttendantsInput = View.viewAttendants(self)
        return viewAttendantsInput

    def viewManagers(self):
        print('''1.2. View Managers
--------------------------------------------
  1. View specific manager
  2. View all managers
--------------------------------------------''')
        viewManagersInput = input("Input choice (q to Quit, b for Back): ")
        viewManagersInput = viewManagersInput.lower()
        if viewManagersInput == "1":
            managerSSN = input("  - Input SSN with no spaces in between: ")
            Manager = UIAPI.UIAPI.viewWorkerBySSn(self, managerSSN, "Manager")
            printObjects(Manager)
            return viewManagersInput
        elif viewManagersInput == "2":
            allManagers = UIAPI.UIAPI.viewWorkerByPOS(self, "Manager")
            printObjects(allManagers)
            return viewManagersInput
        elif viewManagersInput == "b":
            return viewManagersInput
        elif viewManagersInput == "q":
            return viewManagersInput
        else:
            print("Wrong input, try again!")
            viewManagersInput = View.viewManagers(self)
        return viewManagersInput

    def viewAirplane(self):
        print('''2. View Airplane
--------------------------------------------
  1. View specific airplane
  2. View all airplanes
--------------------------------------------''')

        viewAirplaneInput = input("Input choice (q to Quit, b for Back): ")
        viewAirplaneInput = viewAirplaneInput.lower()
        if viewAirplaneInput == "1":
            AirplaneReg = input("  - Input airplane registration: ")
            Airplane = UIAPI.UIAPI.viewCertainAirplane(self, AirplaneReg)  
            printObjects(Airplane)
            viewAirplaneInput = View.viewAirplane(self)
        elif viewAirplaneInput == "2":
            allPlanes = UIAPI.UIAPI.viewAllAirplanes(self)
            printObjects(allPlanes)
            viewAirplaneInput = View.viewAirplane(self)
        elif viewAirplaneInput == "b":
            return viewAirplaneInput
        elif viewAirplaneInput == "q":
            return viewAirplaneInput
        else:
            print("Wrong input, try again!")
            viewAirplaneInput = View.viewAirplane(self)
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
            flightRouteID = input("  - Input Flight Route ID: ")
            flightRoute = UIAPI.UIAPI.viewFlightRoute(self, flightRouteID)
            printObjects(flightRoute)
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        elif viewFlightRoutesInput == "2":
            allFlightRoutes = UIAPI.UIAPI.viewAllFlightRoutes(self)
            printObjects(allFlightRoutes)
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        elif viewFlightRoutesInput == "b":
            return viewFlightRoutesInput
        elif viewFlightRoutesInput == "q":
            return viewFlightRoutesInput
        else:
            print("Wrong input, try again!")
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        return viewFlightRoutesInput

    def viewVoyages(self):
        print('''4. View Voyages
--------------------------------------------
  1. View a specific voyage
  2. View all voyages
  3. View all voyages on a given day
  4. View all voyages in a given week
--------------------------------------------''')

        viewVoyagesInput = input("Input choice (q to Quit, b for Back): ")
        viewVoyagesInput = viewVoyagesInput.lower()
        if viewVoyagesInput == "1":
            voyageID = input("  - Input Voyage ID: ")
            voyage = UIAPI.UIAPI.viewVoyage(self, voyageID)
            printObjects(voyage)
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "2":
            voyages = UIAPI.UIAPI.viewallVoyages(self)
            printObjects(voyages)
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "3":
            day, month, year = None, None, None
            voyageDate = ""
            while True:
                voyageDate = input("  - Input date(f.x. 24/12/2019), b for Back: ")
                if voyageDate == "b":
                    viewVoyagesInput = View.viewVoyages(self)
                else:
                    try:
                        day, month, year = map(int, voyageDate.split('/'))
                        if year > 0 and year < 3000:
                            break
                    except Exception:
                        print("Wrong input, try again!")
            voyageDate = datetime.datetime(year, month, day)
            allVoyagesDay = UIAPI.UIAPI.viewallVoyagesDay(self, voyageDate)
            printObjects(allVoyagesDay)
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "4":
            voyageYear = input("  - Input year: ")
            voyagetWeek = input("  - Input week of the year: ")
            allVoyagesWeek = UIAPI.UIAPI.viewallVoyagesWeek(self, voyageYear, voyagetWeek)
            printObjects(allVoyagesWeek)
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
  4. View cancelled/landed flights
--------------------------------------------''')

        viewFlightInput = input("Input choice (q to Quit, b for Back): ")
        viewFlightInput = viewFlightInput.lower()
        if viewFlightInput == "1":
            flightNumber = input("  - Input flight number: ")
            flightDay = input("  - Input date (f.x. 31/12/2019): ")
            day, month, year = map(int, flightDay.split('/'))
            flightDate = datetime.datetime(year, month, day)
            viewFlight = UIAPI.UIAPI.viewCertainFlight(self, flightNumber, flightDate)
            printObjects(viewFlight)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "2":
            allFlights = UIAPI.UIAPI.viewAllFlights(self)
            printObjects(allFlights)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "3":
            viewActiveFlights = UIAPI.UIAPI.viewFlightsByStatuses(self, ["On schedule", "Loading", "In-Air"])
            printObjects(viewActiveFlights)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "4":
            viewCancelledFlights = UIAPI.UIAPI.viewFlightsByStatuses(self, ["Landed", "Cancelled"])
            printObjects(viewCancelledFlights)
            viewFlightInput = View.viewFlight(self)
        elif viewFlightInput == "b":
            return viewFlightInput
        elif viewFlightInput == "q":
            return viewFlightInput
        else:
            print("Wrong input, try again!")
            viewFlightInput = View.viewFlight(self)
        return viewFlightInput

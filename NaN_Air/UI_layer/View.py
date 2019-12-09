import UIAPI
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
            print(str(allStaff) + "\n")
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
--------------------------------------------''')
        viewPilotsInput = input("Input choice (q to Quit, b for Back): ")
        viewPilotsInput = viewPilotsInput.lower()
        if viewPilotsInput == "1":
            pilotSSN = input("Input SSN: ")
            Pilot = UIAPI.UIAPI.viewWorkerBySSn(self, pilotSSN, "Pilot")
            print("\n" + str(Pilot) + "\n")
            return viewPilotsInput
        elif viewPilotsInput == "2":
            allPilots = UIAPI.UIAPI.viewWorkerByPOS(self, "Pilot")
            for instances in allPilots:
                print("\n" + str(instances) + "\n")
            return viewPilotsInput
        elif viewPilotsInput == "3":
            pilotDate = input("Input date: ")
            availablePilots = UIAPI.UIAPI.listAvailableWorkersbydate(self, pilotDate, "Pilot")
        elif viewPilotsInput == "b":
            return viewPilotsInput
        elif viewPilotsInput == "q":
            return viewPilotsInput
        else:
            print("Wrong input, try again")
            #viewPilotsInput = View.viewPilots(self) ???
        return viewPilotsInput

#Attendants
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
            print("\n" + str(Attendant) + "\n")
            return viewAttendantsInput
        elif viewAttendantsInput == "2":
            allAttendants = UIAPI.UIAPI.viewWorkerByPOS(self, "Attendant")
            for instances in allAttendants:
                print("\n" + str(instances) + "\n")
            return viewAttendantsInput
        elif viewAttendantsInput == "3":
            attendantDate = input("Input date: ")
            availableAttendants = UIAPI.UIAPI.listAvailableWorkersbydate(self, attendantDate, "Attendant")
            return viewAttendantsInput
        elif viewAttendantsInput == "4":
            attendantDate = input("Input date: ")
            unavailableAttendants = UIAPI.UIAPI.listUnavailableWorkersbydate(self, attendantDate, "Attendant")
            return viewAttendantsInput
        elif viewAttendantsInput == "b":
            return viewAttendantsInput
        elif viewAttendantsInput == "q":
            return viewAttendantsInput
        else:
            print("Wrong input, try again!")
            viewAttendantsInput = View.viewAttendants(self)
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
            print("\n" + str(Airplane) + "\n")
            viewAirplaneInput = self.uiapi.viewXplane(self, AirplaneID)
            print(viewAirplaneInput)
            viewAirplaneInput = self.viewAirplane()
        elif viewAirplaneInput == "2":
            viewAirplaneInput = GFSDGSFDGSDGSDGSDGDS
            print(viewAirplaneInput)
            for count, plane in enumerate(viewAirplaneInput):
                if len(viewAirplaneInput) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next") #HVERNIG LÍTUR ENTER ÚT?????
                print(plane)
                print()
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
            FlightRouteID = input("Input Flight Route ID: ")
            print(FlightRouteID)
            #FlightRoute = getFlightRoute(FlightRouteID)
            #print(FlightRoute)
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        elif viewFlightRoutesInput == "2":
            allFlightRoutes = UIAPI.UIAPI.viewAllFlightRoutes(self)
            print(str(allFlightRoutes) + "\n")
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
--------------------------------------------''')

        viewVoyagesInput = input("Input choice (q to Quit, b for Back): ")
        viewVoyagesInput = viewVoyagesInput.lower()
        if viewVoyagesInput == "1":
            SSN = input("Input Voyage ID: ")
            # VoyageInfo = getVoyageInfo(SSN)
            # print(VoyageInfo)
            print(SSN)
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "2":
            print("")
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
            viewFlight = View.uiapi.viewXflight(self, flightNumber)
            print(viewFlight)
            #FlightInfo = getSpecificFlight(SSN)
            #print(FlightInfo)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "2":
            # print(getAllFlights())
            allFlights = UIAPI.UIAPI.viewAllFlights()
            print(str(allStaff) + "\n")
            for count, flight in enumerate(allFlights):
                if len(viewAllFlights) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(flight)
                print()
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "3":
            viewActiveFlights = View.uiapi.viewActiveFlights(self)
            for count, flight in enumerate(viewActiveFlights):
                if len(viewActiveFlights) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(flight)
                print()
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "4":
            viewCancelledFlights = View.uiapi.viewCancelledFlights(self)
            for count, flight in enumerate(viewCancelledFlights):
                if len(viewCancelledFlights) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(flight)
                print()
            viewFlightInput = View.viewFlight(self)
        elif viewFlightInput == "b":
            return viewFlightInput
        elif viewFlightInput == "q":
            return viewFlightInput
        else:
            print("Wrong input, try again!")
            viewFlightInput = View.viewFlight(self)
        return viewFlightInput

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

        viewMenuInput = input("Input choice(q to Quit, b for Back): ")
        viewMenuInput = viewMenuInput.lower()
        if viewMenuInput == "1":
            viewWorkerOutput = self.viewWorker()
            if viewWorkerOutput == "b":
                viewMenuInput = self.viewMenu()
        elif viewMenuInput == "2":
            viewAirplaneOutput = self.viewAirplane()
            if viewAirplaneOutput == "b":
                viewMenuInput = self.viewMenu()
        elif viewMenuInput == "3":
            viewFlightRoutesOutput = self.viewFlightRoutes()
            if viewFlightRoutesOutput == "b":
                viewMenuInput = self.viewMenu()
        elif viewMenuInput == "4":
            viewVoyagesOutput = self.viewVoyages()
            if viewVoyagesOutput == "b":
                viewMenuInput = self.viewMenu()
        elif viewMenuInput == "5":
            viewFlightOutput = self.viewFlight()
            if viewFlightOutput == "b":
                viewMenuInput = self.viewMenu()
        elif viewMenuInput == "b":
            return viewMenuInput
        elif viewMenuInput == "q":
            return viewMenuInput
        else:
            print("Wrong input, try again")
            viewMenuInput = self.viewMenu()
        return viewMenuInput

    def viewWorker(self):
        print('''1. View Worker
--------------------------------------------
  1. View Pilots
  2. View Attendants
  3. View Bosses
  4. View All Staff
--------------------------------------------''')

        viewWorkerInput = input("Input choice(q to Quit, b for Back): ")
        viewWorkerInput = viewWorkerInput.lower()
        if viewWorkerInput == "1":
            viewPilotsOutput = self.viewPilots()
            if viewPilotsOutput == "b":
                viewWorkerInput = self.viewWorker()
            elif viewPilotsOutput == "q":
                return viewWorkerInput
            else:
                viewWorkerInput = self.viewWorker()
        elif viewWorkerInput == "2":
            viewAttendantsOutput = self.viewAttendants()
            if viewAttendantsOutput == "b":
                viewWorkerInput = self.viewWorker()
            elif viewAttendantsOutput == "q":
                return viewWorkerInput
            else:
                viewWorkerInput = self.viewWorker()
        elif viewWorkerInput == "3":
            # BossInfo = getAllBosses()
            # print(BossInfo)
            print("")
            viewWorkerInput = self.viewWorker()
        elif viewWorkerInput == "4":
            # print(getAllStaff())
            print("")
            viewWorkerInput = self.viewWorker()
        elif viewWorkerInput == "b":
            return viewWorkerInput
        elif viewWorkerInput == "q":
            return viewWorkerInput
        else:
            print("Wrong input, try again")
            viewWorkerInput = self.viewWorker()
        return viewWorkerInput

# Pilots
    def viewPilots(self):
        print('''1.1. View Pilots
--------------------------------------------
  1. View specific pilot
  2. View all pilots
--------------------------------------------''')
        viewPilotsInput = input("Input choice(q to Quit, b for Back): ")
        viewPilotsInput = viewPilotsInput.lower()
        if viewPilotsInput == "1":
            pilotSSN = input("  - Please input SSN: ")
            print(pilotSSN)
            # PilotInfo = getPilotInfo(PilotSSN)
            # print(pilotInfo)
            self.uiapi.view_worker('Pilot', pilotSSN)
            return viewPilotsInput
        elif viewPilotsInput == "2":
            print("")
            pilotSSN = ""
            self.uiapi.view_worker("Pilot")

            # print(AllPilots)
            # View.viewWorker()
            return viewPilotsInput
        elif viewPilotsInput == "b":
            return viewPilotsInput
        elif viewPilotsInput == "q":
            return viewPilotsInput
        else:
            print("Wrong input, try again")
            viewPilotsInput = self.viewPilots()
        return viewPilotsInput

#Attendants
    def viewAttendants(self):
        print('''1.2. View Attendants
--------------------------------------------
  1. View specific attendant
  2. View all attendants
--------------------------------------------''')
        viewAttendantsInput = input("Input choice(q to Quit, b for Back): ")
        viewAttendantsInput = viewAttendantsInput.lower()
        if viewAttendantsInput == "1":
            attendantSSN = input("  - Please input SSN: ")
            print(attendantSSN)
            self.uiapi.view_worker(ssn, 'Attendant')
            # AttendantInfo = getAttendantInfo(AttendantSSN)
            return viewAttendantsInput
        elif viewAttendantsInput == "2":
            # print(getAllAttendants())
            self.uiapi.view_worker(ssn="", 'Attendant')
            print("")
            return viewAttendantsInput
        elif viewAttendantsInput == "b":
            return viewAttendantsInput
        elif viewAttendantsInput == "q":
            return viewAttendantsInput
        else:
            print("Wrong input, try again")
            viewAttendantsInput = self.viewAttendants()
        return viewAttendantsInput

    def viewAirplane(self):
        print('''2. View Airplane
--------------------------------------------
  1. View specific airplane
  2. View all airplanes
--------------------------------------------''')

        viewAirplaneInput = input("Input choice(q to Quit, b for Back): ")
        viewAirplaneInput = viewAirplaneInput.lower()
        if viewAirplaneInput == "1":
            AirplaneID = input("  - Please input Airplane ID: ")
            # AirplaneInfo = getAirplaneInfo(AirplaneID)

            # print(AirplaneInfo)
            viewAirplaneInput = self.uiapi.viewXplane(self, AirplaneID)
            print(viewAirplaneInput)
            viewAirplaneInput = self.viewAirplane()
        elif viewAirplaneInput == "2":
            # AllAirplanesInfo = getAllAirplanes()
            # print(AllAirplanesInfo)
            #viewAirplaneInput = self.instance.viewAllPlanes()
            viewAirplaneInput = self.uiapi.viewAllPlanes()
            print(viewAirplaneInput)
            for count, plane in enumerate(viewAirplaneInput):
                if len(viewAirplaneInput) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(plane)
            viewAirplaneInput = self.viewAirplane()
        elif viewAirplaneInput == "b":
            return viewAirplaneInput
        elif viewAirplaneInput == "q":
            return viewAirplaneInput
        else:
            print("Wrong input, try again")
            viewAirplaneInput = self.viewAirplane()
        return viewAirplaneInput

    def viewFlightRoutes(self):
        print('''3. View Flight Routes
--------------------------------------------
  1. Specific route
  2. All flight routes
--------------------------------------------''')

        viewFlightRoutesInput = input("Input choice(q to Quit, b for Back): ")
        viewFlightRoutesInput = viewFlightRoutesInput.lower()
        if viewFlightRoutesInput == "1":
            FlightRouteID = input("  - Please input Flight Route ID: ")
            print(FlightRouteID)
            #FlightRoute = getFlightRoute(FlightRouteID)
            #print(FlightRoute)
            viewFlightRoutesInput = self.viewFlightRoutes()
        elif viewFlightRoutesInput == "2":
            #print(getAllFlightRoutes)
            print("")
            viewFlightRoutesInput = self.viewFlightRoutes()
        elif viewFlightRoutesInput == "b":
            return viewFlightRoutesInput
        elif viewFlightRoutesInput == "q":
            return viewFlightRoutesInput
        else:
            print("Wrong input, try again")
            viewFlightRoutesInput = self.viewFlightRoutes()
        return viewFlightRoutesInput

    def viewVoyages(self):
        print('''4. View Voyages
--------------------------------------------
  1. View a specific voyage
  2. View all voyages
--------------------------------------------''')

        viewVoyagesInput = input("Input choice(q to Quit, b for Back): ")
        viewVoyagesInput = viewVoyagesInput.lower()
        if viewVoyagesInput == "1":
            SSN = input('  - Please input Voyage ID: ')
            # VoyageInfo = getVoyageInfo(SSN)
            # print(VoyageInfo)
            print(SSN)
            viewVoyagesInput = self.viewVoyages()
        elif viewVoyagesInput == "2":
            print("")
            #print(getAllVoyages())
            viewVoyagesInput = self.viewVoyages()
        elif viewVoyagesInput == "b":
            return viewVoyagesInput
        elif viewVoyagesInput == "q":
            return viewVoyagesInput
        else:
            print("Wrong input, try again")
            viewVoyagesInput = self.viewVoyages()
        return viewVoyagesInput

    def viewFlight(self):
        print('''5. View Flights
--------------------------------------------
  1. View specific flight
  2. View all flights
  3. View active flights
  4. View cancelled flights
--------------------------------------------''')

        viewFlightInput = input("Input choice(q to Quit, b for Back): ")
        viewFlightInput = viewFlightInput.lower()
        if viewFlightInput == "1":
            flightNumber = input('  - Please input flight number: ')
            viewFlight = self.uiapi.viewXflight(self, flightNumber)
            print(viewFlight)
            #FlightInfo = getSpecificFlight(SSN)
            #print(FlightInfo)
            viewFlightInput = self.viewFlight()
        if viewFlightInput == "2":
            # print(getAllFlights())
            viewAllFlights = self.uiapi.viewAllFlights(self)
            for count, flight in enumerate(viewAllFlights):
                if len(viewAllFlights) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(flight)
                print()
            viewFlightInput = self.viewFlight()
        if viewFlightInput == "3":
            viewActiveFlights = self.uiapi.viewActiveFlights(self)
            for count, flight in enumerate(viewActiveFlights):
                if len(viewActiveFlights) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(flight)
                print()
            viewFlightInput = self.viewFlight()
        if viewFlightInput == "4":
            viewCancelledFlights = self.uiapi.viewCancelledFlights(self)
            for count, flight in enumerate(viewCancelledFlights):
                if len(viewCancelledFlights) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(flight)
                print()
            viewFlightInput = self.viewFlight()
        elif viewFlightInput == "b":
            return viewFlightInput
        elif viewFlightInput == "q":
            return viewFlightInput
        else:
            print("Wrong input, try again")
            viewFlightInput = self.viewFlight()
        return viewFlightInput

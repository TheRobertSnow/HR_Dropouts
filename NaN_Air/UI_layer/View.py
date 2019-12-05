import UIAPI
class View():
    def __init__(self):
        self.object = UIAPI.UIAPI()

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
            print("Wrong input, try again")
            viewMenuInput = View.viewMenu(self)
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
        if viewWorkerInput == "1":
            viewPilotsOutput = View.viewPilots()
            if viewPilotsOutput == "b":
                viewWorkerInput = View.viewWorker(self)
            elif viewPilotsOutput == "q":
                return viewWorkerInput
            else:
                viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "2":
            viewAttendantsOutput = View.viewAttendants()
            if viewAttendantsOutput == "b":
                viewWorkerInput = View.viewWorker(self)
            elif viewAttendantsOutput == "q":
                return viewWorkerInput
            else:
                viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "3":
            # BossInfo = getAllBosses()
            # print(BossInfo)
            print("")
            viewWorkerInput = View.viewWorker(self)
        elif viewWorkerInput == "4":
            # print(getAllStaff())
            print("")
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
--------------------------------------------''')
        viewPilotsInput = input("Input choice(q to Quit, b for Back): ")
        if viewPilotsInput == "1":
            pilotSSN = input("  - Please input SSN: ")
            print(pilotSSN)
            # PilotInfo = getPilotInfo(PilotSSN)
            # print(pilotInfo)
            # View.viewWorker()
            return viewPilotsInput
        elif viewPilotsInput == "2":
            print("")
            # AllPilots = getAllPilots()
            # print(AllPilots)
            # View.viewWorker()
            return viewPilotsInput
        elif viewPilotsInput == "b":
            return viewPilotsInput
        elif viewPilotsInput == "q":
            return viewPilotsInput
        else:
            print("Wrong input, try again")
            viewPilotsInput = View.viewPilots(self)
        return viewPilotsInput    

#Attendants
    def viewAttendants(self):
        print('''1.2. View Attendants
--------------------------------------------
  1. View specific attendant
  2. View all attendants
--------------------------------------------''')
        viewAttendantsInput = input("Input choice(q to Quit, b for Back): ")
        if viewAttendantsInput == "1":
            attendantSSN = input("  - Please input SSN: ")
            print(attendantSSN)
            # AttendantInfo = getAttendantInfo(AttendantSSN)
            return viewAttendantsInput
        elif viewAttendantsInput == "2":
            # print(getAllAttendants())
            print("")
            return viewAttendantsInput
        elif viewAttendantsInput == "b":
            return viewAttendantsInput
        elif viewAttendantsInput == "q":
            return viewAttendantsInput
        else:
            print("Wrong input, try again")
            viewAttendantsInput = View.viewAttendants(self)
        return viewAttendantsInput
        
    def viewAirplane(self):     
        print('''2. View Airplane
--------------------------------------------
  1. View specific airplane
  2. View all airplanes
--------------------------------------------''')

        viewAirplaneInput = input("Input choice(q to Quit, b for Back): ")
        if viewAirplaneInput == "1":
            AirplaneID = input("  - Please input Airplane ID: ")
            # AirplaneInfo = getAirplaneInfo(AirplaneID)
            # print(AirplaneInfo)
            viewAirplaneInput = UIAPI.UIAPI.viewXplane(self, AirplaneID)
            print(viewAirplaneInput)
            viewAirplaneInput = View.viewAirplane(self)
        elif viewAirplaneInput == "2":
            # AllAirplanesInfo = getAllAirplanes()
            # print(AllAirplanesInfo)
            #viewAirplaneInput = self.instance.viewAllPlanes()
            viewAirplaneInput = UIAPI.UIAPI.viewAllPlanes(self)
            print(viewAirplaneInput)
            for count, plane in enumerate(viewAirplaneInput):
                if len(viewAirplaneInput) > 4:
                    if count >= 4:
                        if count % 4 == 0:
                            input("\nPress enter to see next")
                print(plane)
            viewAirplaneInput = View.viewAirplane(self)
        elif viewAirplaneInput == "b":
            return viewAirplaneInput
        elif viewAirplaneInput == "q":
            return viewAirplaneInput
        else:
            print("Wrong input, try again")
            viewAirplaneInput = View.viewAirplane(self)
        return viewAirplaneInput

    def viewFlightRoutes(self):
        print('''3. View Flight Routes
--------------------------------------------
  1. Specific route
  2. All flight routes
--------------------------------------------''')

        viewFlightRoutesInput = input("Input choice(q to Quit, b for Back): ")
        if viewFlightRoutesInput == "1":
            FlightRouteID = input("  - Please input Flight Route ID: ")
            print(FlightRouteID)
            #FlightRoute = getFlightRoute(FlightRouteID)
            #print(FlightRoute)
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        elif viewFlightRoutesInput == "2":
            #print(getAllFlightRoutes)
            print("")   
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        elif viewFlightRoutesInput == "b":
            return viewFlightRoutesInput
        elif viewFlightRoutesInput == "q":
            return viewFlightRoutesInput
        else:
            print("Wrong input, try again")
            viewFlightRoutesInput = View.viewFlightRoutes(self)
        return viewFlightRoutesInput

    def viewVoyages(self):
        print('''4. View Voyages
--------------------------------------------
  1. View a specific voyage
  2. View all voyages
--------------------------------------------''')

        viewVoyagesInput = input("Input choice(q to Quit, b for Back): ")
        if viewVoyagesInput == "1":
            SSN = input('  - Please input Voyage ID: ')
            # VoyageInfo = getVoyageInfo(SSN)
            # print(VoyageInfo)
            print(SSN)
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "2":
            print("")
            #print(getAllVoyages())
            viewVoyagesInput = View.viewVoyages(self)
        elif viewVoyagesInput == "b":
            return viewVoyagesInput
        elif viewVoyagesInput == "q":
            return viewVoyagesInput
        else:
            print("Wrong input, try again")
            viewVoyagesInput = View.viewVoyages(self)
        return viewVoyagesInput
      
    def viewFlight(self):
        print('''5. View Flights
--------------------------------------------
  1. View specific flight
  2. View all fLights
  3. View active flights
  4. View cancelled flights
--------------------------------------------''')

        viewFlightInput = input("Input choice(q to Quit, b for Back): ")
        if viewFlightInput == "1":
            SSN = input('  - Please input Voyage ID: ')
            print(SSN)
            #FlightInfo = getSpecificFlight(SSN)
            #print(FlightInfo)
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "2":
            # print(getAllFlights())
            print("")
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "3":
            # print(getActiveFlights())
            print("")
            viewFlightInput = View.viewFlight(self)
        if viewFlightInput == "4":
            # print(getCancelledFlights)
            print("")
            viewFlightInput = View.viewFlight(self)
        elif viewFlightInput == "b":
            return viewFlightInput
        elif viewFlightInput == "q":
            return viewFlightInput
        else:
            print("Wrong input, try again")
            viewFlightInput = View.viewFlight(self)
        return viewFlightInput

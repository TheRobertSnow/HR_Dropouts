class View():
    def viewMenu():
        print('''View Data
--------------------------------------------
  1. View worker
  2. View Airplane
  3. View Flight routes
  4. View Voyages
  5. View Flight 
--------------------------------------------''')

        viewMenuInput = input("Input choice(q to Quit, b for Back): ")
        viewMenuInput = viewMenuInput.lower()
        if viewMenuInput == "1":
            print("")
            View.viewWorker()
            View.viewMenu()
        elif viewMenuInput == "2":
            print("")
            View.viewAirplane()
            View.viewMenu()
            
        elif viewMenuInput == "3":
            print("")
            View.viewFlightRoutes()
            View.viewMenu()
        elif viewMenuInput == "4":
            print("")
            View.viewVoyages()
            View.viewMenu()
        elif viewMenuInput == "5":
            print("")
            View.viewFlight()
            View.viewMenu()
        elif viewMenuInput == "b":
            return None
        elif viewMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            View.viewMenu()
        return viewMenuInput
    
    def viewWorker():
        print('''       View Worker
-----------------------------------------
    1 View Pilots
    2 View Attendants
    3 View Bosses
    4 View All Staff''')
        viewWorkerInput = input("Input choice(q to Quit, b for Back): ")
        if viewWorkerInput == "1":
            View.viewPilots()

            View.viewWorker()
        
        elif viewWorkerInput == "2":
            View.viewAttendants()
        
        elif viewWorkerInput == "3":
            View.viewBosses() 

        elif viewWorkerInput == "4":
            View.viewAllStaff()
############################################
# Pilots
    def viewPilots():
        print('''1 View Specific Pilot
2 View All Pilots''') 
        viewPilotsInput = input("Input choice(q to Quit, b for Back): ")
        if viewPilotsInput == "1":
            View.viewSpecificPilot()
        elif viewPilotsInput == "2":
            View.viewAllPilots()

    def viewSpecificPilot():
        PilotSSN = input("  - Please input SSN: ")
        PilotInfo = getPilotInfo(PilotSSN)
        print(pilotInfo)
    def viewAllPilots():
        AllPilots = getAllPilots()
        print(AllPilots)
#attendants
    def viewAttendants():
        print('''-----------------------------------------
        View Attendants
-----------------------------------------
    1 View Specific Attendant
    2 View All Attendants''')
        ViewAttendantsInput = input("Input choice(q to Quit, b for Back): ")
        if ViewAttendantsInput == "1":
            View.viewSpecificAttendant()
        elif ViewAttendantsInput == "2":
            View.viewAllAttendants()
    def viewSpecificAttendant():
        AttendantSSN = input("  - Please input SSN: ")
        AttendantInfo = getAttendantInfo(AttendantSSN)
        print(AttendantInfo)

    def viewAllAttendants():
        print(getAllAttendants())
#Bosses

    def viewBosses():
        print('''-----------------------------------------
        View Bosses
----------------------------------------- ''')

        BossInfo = getAllBosses()
        print(BossInfo)

    def viewAllStaff():
        print(getAllStaff())

#AllWorkers    
############################################
        

    def viewAirplane():
        
        print('''-----------------------------------------
        View Airplane
-----------------------------------------

1 View specific airplane
2 View All Airplanes
''')

        viewAirplaneInput = input("Input choice(q to Quit, b for Back): ")
        if viewAirplaneInput == "1":
            viewSpecificAirplane()
        elif viewAirplaneInput == "2":
            viewAllAirplanes()
        
    def viewSpecificAirplane():
        AirplaneID = input("  - Please input Airplane ID: ")
        AirplaneInfo = getAirplaneInfo(AirplaneID)
        print(AirplaneInfo)

    def viewAllAirplanes():
        AllAirplanesInfo = getAllAirplanes()
        print(AllAirplanesInfo)


############################################
    def viewFlightRoutes():
        print('''-----------------------------------------
        View Flight Routes
-----------------------------------------
1 Specific Route
2 All Flight Routes
''')
        viewFlightRoutesInput = input("Input choice(q to Quit, b for Back): ")
        if viewFlightRoutesInput == "1":
            View.viewSpecificRoute()
        elif viewFlightRoutesInput == "2":
            View.viewAllRoutes()

    def viewSpecificRoute():
        FlightRouteID = input("  - Please input Flight Route ID: ")

        FlightRoute = getFlightRoute(FlightRouteID)
        print(FlightRoute)

    def viewAllRoutes():
        print(getAllFlightRoutes)

        

############################################
    def viewVoyages():
        print('''1 View a Specific Voyage
2 View all Voyages
3''')
        viewVoyagesInput = input("Input choice(q to Quit, b for Back): ")
        if viewVoyagesInput == "1":
            View.viewSpecificVoyage()
        elif viewVoyagesInput == "2":
            View.viewAllVoyages()

    def viewSpecificVoyage():

        SSN = input('  - Please input Voyage ID: ')
        VoyageInfo = getVoyageInfo(SSN)
        print(VoyageInfo)

    def viewAllVoyages():
        print(getAllVoyages())



############################################
    def viewFlight():
        print('''1 View specific Flight
2 View All FLights
3 View Active Flights
4 View Cancelled Flights''')

        viewFlightInput = input("Input choice(q to Quit, b for Back): ")

        if viewFlightINput == "1":
            View.viewSpecificFlight()
        if viewFlightINput == "2":
            View.viewAllFlights()
        if viewFlightINput == "3":
            View.viewActiveFlights()
        if viewFlightINput == "4":
            View.viewCancelledFlights()

        def viewSpecificFlight():
            SSN = input('  - Please input Voyage ID: ')
            FlightInfo = getSpecificFlight(SSN)
            print(FlightInfo)

        def viewAllFlights():
            print(getAllFlights())

        def viewActiveFLights():
            print(getActiveFlights())

        def viewCancelledFlights():
            print(getCancelledFlights)
        
    


View.viewMenu()

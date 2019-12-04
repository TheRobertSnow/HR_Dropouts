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
            viewMenuInput = View.viewWorker()
        elif viewMenuInput == "2":
            viewMenuInput = View.viewAirplane()
        elif viewMenuInput == "3":
            viewMenuInput = View.viewFlightRoutes()
        elif viewMenuInput == "4":
            viewMenuInput = View.viewVoyages()
        elif viewMenuInput == "5":
            viewMenuInput = View.viewFlight()
        elif viewMenuInput == "b":
            return viewMenuInput
        elif viewMenuInput == "q":
            return viewMenuInput
        else:
            print("Wrong input, try again")
            viewMenuInput = View.viewMenu()
        return viewMenuInput
    
    def viewWorker():
        print('''View Worker
--------------------------------------------
  1. View Pilots
  2. View Attendants
  3. View Bosses
  4. View All Staff
--------------------------------------------''')

        viewWorkerInput = input("Input choice(q to Quit, b for Back): ")
        if viewWorkerInput == "1":
            viewWorkerInput = View.viewPilots()
        elif viewWorkerInput == "2":
            viewWorkerInput = View.viewAttendants()
        elif viewWorkerInput == "3":
            viewWorkerInput = View.viewBosses() 
        elif viewWorkerInput == "4":
            viewWorkerInput = View.viewAllStaff()
        elif viewWorkerInput == "b":
            viewWorkerInput = View.viewMenu()
        elif viewWorkerInput == "q":
            return viewWorkerInput
        else:
            print("Wrong input, try again")
            viewWorkerInput = View.viewWorker()
        return viewWorkerInput        
    
# Pilots
    def viewPilots():
        print('''1. View Pilots
--------------------------------------------
  1. View Specific Pilot
  2. View All Pilots
--------------------------------------------''') 
        viewPilotsInput = input("Input choice(q to Quit, b for Back): ")
        if viewPilotsInput == "1":
            pilotSSN = input("  - Please input SSN: ")
            print(pilotSSN)
            #PilotInfo = getPilotInfo(PilotSSN)
            #print(pilotInfo)
            return viewPilotsInput  
        elif viewPilotsInput == "2":
            print("")
            #AllPilots = getAllPilots()
            #print(AllPilots)
            return viewPilotsInput  
        elif viewPilotsInput == "b":
            viewPilotsInput = View.viewWorker()
        elif viewPilotsInput == "q":
            return viewPilotsInput
        else:
            print("Wrong input, try again")
            viewPilotsInput = View.viewPilots()
        return viewPilotsInput    

#Attendants
    def viewAttendants():
        print('''2. View Attendants
--------------------------------------------
  1. View Specific Attendant
  2. View All Attendants
--------------------------------------------''')
        viewAttendantsInput = input("Input choice(q to Quit, b for Back): ")
        if viewAttendantsInput == "1":
            attendantSSN = input("  - Please input SSN: ")
            print(attendantSSN)
            #AttendantInfo = getAttendantInfo(AttendantSSN)
            return viewAttendantsInput
        elif viewAttendantsInput == "2":
            #print(getAllAttendants())
            print("")
            return viewAttendantsInput
        elif viewAttendantsInput == "b":
            viewAttendantsInput = View.viewWorker()
        elif viewAttendantsInput == "q":
            return viewAttendantsInput
        else:
            print("Wrong input, try again")
            viewAttendantsInput = View.viewAttendants()
        return viewAttendantsInput

#Bosses
    def viewBosses():
        print('''3. View Bosses
--------------------------------------------''')
        #BossInfo = getAllBosses()
        #print(BossInfo)
        print("")
        return ""

#All staff
    def viewAllStaff():
        print('''4. View All Staff
--------------------------------------------''')
        #print(getAllStaff())
        print("")
        return ""


        
    def viewAirplane():     
        print('''2. View Airplane
--------------------------------------------
  1. View specific airplane
  2. View All Airplanes
--------------------------------------------''')

        viewAirplaneInput = input("Input choice(q to Quit, b for Back): ")
        if viewAirplaneInput == "1":
            AirplaneID = input("  - Please input Airplane ID: ")
            #AirplaneInfo = getAirplaneInfo(AirplaneID)
            #print(AirplaneInfo)
            print(AirplaneID)
            return viewAirplaneInput
        elif viewAirplaneInput == "2":
            #AllAirplanesInfo = getAllAirplanes()
            #print(AllAirplanesInfo)
            print("")
            return viewAirplaneInput
        elif viewAirplaneInput == "b":
            viewAirplaneInput = View.viewMenu()
        elif viewAirplaneInput == "q":
            return viewAirplaneInput
        else:
            print("Wrong input, try again")
            viewAirplaneInput = View.viewAirplane()
        return viewAirplaneInput

    def viewFlightRoutes():
        print('''3. View Flight Routes
--------------------------------------------
  1. Specific Route
  2. All Flight Routes
--------------------------------------------''')
        
        viewFlightRoutesInput = input("Input choice(q to Quit, b for Back): ")
        if viewFlightRoutesInput == "1":
            FlightRouteID = input("  - Please input Flight Route ID: ")
            print(FlightRouteID)
            #FlightRoute = getFlightRoute(FlightRouteID)
            #print(FlightRoute)
            return viewFlightRoutesInput
        elif viewFlightRoutesInput == "2":
            #print(getAllFlightRoutes)
            print("")   
            return viewFlightRoutesInput
        elif viewFlightRoutesInput == "b":
            viewFlightRoutesInput = View.viewMenu()
        elif viewFlightRoutesInput == "q":
            return viewFlightRoutesInput
        else:
            print("Wrong input, try again")
            viewFlightRoutesInput = View.viewFlightRoutes()
        return viewFlightRoutesInput

    def viewVoyages():
        print('''4. View Voyages
--------------------------------------------
  1. View a Specific Voyage
  2. View all Voyages
--------------------------------------------''')
        
        viewVoyagesInput = input("Input choice(q to Quit, b for Back): ")
        if viewVoyagesInput == "1":
            SSN = input('  - Please input Voyage ID: ')
            #VoyageInfo = getVoyageInfo(SSN)
            #print(VoyageInfo)
            print(SSN)
            return viewVoyagesInput
        elif viewVoyagesInput == "2":
            print("")
            #print(getAllVoyages())
            return viewVoyagesInput
        elif viewVoyagesInput == "b":
            viewVoyagesInput = View.viewMenu()
        elif viewVoyagesInput == "q":
            return viewVoyagesInput
        else:
            print("Wrong input, try again")
            viewVoyagesInput = View.viewVoyages()
        return viewVoyagesInput
    
    def viewFlight():
        print('''5. View Flights
--------------------------------------------
  1. View specific Flight
  2. View All FLights
  3. View Active Flights
  4. View Cancelled Flights
--------------------------------------------''')

        viewFlightInput = input("Input choice(q to Quit, b for Back): ")
        if viewFlightInput == "1":
            SSN = input('  - Please input Voyage ID: ')
            print(SSN)
            #FlightInfo = getSpecificFlight(SSN)
            #print(FlightInfo)
            return viewFlightInput
        if viewFlightInput == "2":
            #print(getAllFlights())
            print("")
            return viewFlightInput
        if viewFlightInput == "3":
            #print(getActiveFlights())
            print("")
            return viewFlightInput
        if viewFlightInput == "4":
            #print(getCancelledFlights)
            print("")
            return viewFlightInput
        elif viewFlightInput == "b":
            viewFlightInput = View.viewMenu()
        elif viewFlightInput == "q":
            return viewFlightInput
        else:
            print("Wrong input, try again")
            viewFlightInput = View.viewFlight()
        return viewFlightInput
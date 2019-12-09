import UIAPI



class Update:
    def __init__(self):
        self.UIAPI = UIAPI.UIAPI()

    def update_Worker(self, workerSSN):
        print("""1. Update Worker
--------------------------------------------
  1. Home Address: 
  2. Home Phone Number:
  3. Mobile Phone Number:
  4. E-mail Address
--------------------------------------------""")
        updateWorkerMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        updateWorkerMenuInput = updateWorkerMenuInput.lower()

        if updateWorkerMenuInput == "1":
            newHomeAddress = input("Input new home address: ")
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Address", newHomeAddress))
            return updateWorkerMenuInput

        elif updateWorkerMenuInput == "2":
            newPhoneNumber = int(input("Input new phone number: "))
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Phone", newPhoneNumber))
            return updateWorkerMenuInput

        elif updateWorkerMenuInput == "3":
            newCellNumber = int(input("Input new cellphone number: "))
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Cellphone", newCellNumber))
            return updateWorkerMenuInput

        elif updateWorkerMenuInput == "4":
            newEmail = input("Input new E-mail Address: ")
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Email", newEmail))
            return updateWorkerMenuInput

        elif updateWorkerMenuInput == "b":
            Update.updateMenu(self)
        elif updateWorkerMenuInput == "q":
            print("Forriti lokað!")
            return updateWorkerMenuInput
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.update_Worker(self, workerSSN)

    def updateairplaneStatus(self, airplane_reg_num_Input):
        print("""2. Update Airplane Status
    Select Airplane Status
--------------------------------------------
  1. Working
  2. Engine failure
  3. On Repair
  4. Needs inspection
--------------------------------------------""")
        updateairplanestatusMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        options = ["Working", "Engine failure", "On repair", "Needs inspection"]
        if updateairplanestatusMenuInput == "1" or "2" or "3" or "4":
            if updateairplanestatusMenuInput == "1":
                result = UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[0])
            elif updateairplanestatusMenuInput == "2":
                result = UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[1])
            elif updateairplanestatusMenuInput == "3":
                result = UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[2])
            elif updateairplanestatusMenuInput == "4":
                result = UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[3])
            print(result)
        elif updateairplanestatusMenuInput == "b":
            Update.updateMenu(self)
        elif updateairplanestatusMenuInput == "m":
            Update.updateMenu(self)
        elif updateairplanestatusMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateairplaneStatus(self, airplane_reg_num_Input)
        Update.updateMenu(self)
        # return airplane reg num og key

    def updatecurrentflightRoutes(self):
        flightrouteID = input("Input flight route ID: ")  # Þetta ákveðna tilvik af flight route fundið
        print("Country: Iceland\nAirport: Keflavik\nFlight Distance: 700 km\nTravel time: 75 minutes\n")
        print("""3. Update Current Flights Routes
--------------------------------------------
  1. Update Country
  2. Update Airport
  3. Update Flight Distance
  4. Update Travel time
  5. Update Emergency contact 
  6. Update Emergency contact number
--------------------------------------------""")
        updateflightrouteMenuInput = input(
            "Input choice (q to Quit, b for Back, m for Main Menu): ")  # Á að taka inn int
        if updateflightrouteMenuInput == "1":
            print("Current country: Greece ")
            countryInput = input("Input new country: ")
            print("Country succesfully changed!\nNew country: {}\n".format(countryInput))
        elif updateflightrouteMenuInput == "2":
            print("Current airport: Antetekounmpo airport")
            airportInput = input("Input name of new airport: ")
            print("Airport succesfully changed!\nNew aiport: {}\n".format(airportInput))
        elif updateflightrouteMenuInput == "3":
            print("Current Flight Distance: 500 km\n")
            flightdistanceInput = input("Input new flight distance in kilometers: ")
            print("Flight Distance succesfully changed!\nNew flight distance: {} km\n".format(flightdistanceInput))
        elif updateflightrouteMenuInput == "4":
            print("Current travel time: 120 minutes")
            traveltimeInput = input("Input new travel time in minutes: ")
            print("Travel Time succesfully changed!\nNew travel time: {} minutes\n".format(traveltimeInput))
        elif updateflightrouteMenuInput == "5":
            print("Current Emergency Contact: Gunni")
            emergencycontactInput = input("Input new value: ")
            print("Emergency Contact succesfully changed!\nNew emergency contact: {}\n".format(emergencycontactInput))
        elif updateflightrouteMenuInput == "6":
            print("Current Emergency Contact number: 5812345")
            emergencycontactnumInput = input("Input new value: ")
            print("Emergency Contact number succesfully changed!\nNew emergency contact number: {}\n".format(
                emergencycontactnumInput))
        elif updateflightrouteMenuInput == "b":
            Update.updateMenu()
        elif updateflightrouteMenuInput == "m":
            Update.updateMenu()
        elif updateflightrouteMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("Invalid input")
            updatecurrentflightRoutes()
        print("")
        # Update.updateMenu(Update) HVAÐ Á ÉG AÐ CALLA HÉR???

    def updateVoyage(self, voyageID):
        print("""Voyage ID: {}
        Flight out ID: NA21x
        Flight back ID:NA21(x+1)
        Pilots: [John - 123456789, Hooper - 2607962249]
        Crew: [Emma - 12436576, Jónsi - 3434656539]
        Flight route ID: 23
        Departure from Iceland: datetime
        Departure to Iceland: datetime\n""".format(voyageID))
        print("""4. Update Voyage 
--------------------------------------------
  1. Update Pilots
  2. Update Crew
  3. Update Departure from Iceland
  4. Update Departure to Iceland
  5. Cancel Voyage
--------------------------------------------""")
        updatevoyageMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")  # Á að taka inn int
        if updatevoyageMenuInput == "1":
            print("Current Pilots: [John - 123456789, Hooper - 2607962249]\n")
            print("""1. Update Pilots 
--------------------------------------------
  1. Add Pilot(s)
  2. Remove Pilot(s)
--------------------------------------------""")
            updatepilotMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
            if updatepilotMenuInput == "1":
                print("""
  1. Add Pilot
--------------------------------------------""")
                pilottoaddInput = input(
                    "Input Social Security Number of Pilot to add: ")  # Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Pilot succesfully added!
Current Pilots: [John - 123456789, Hooper - 2607962249]
--------------------------------------------\n""")
            elif updatepilotMenuInput == "2":
                print("""
            2. Remove Pilots
--------------------------------------------""")
                pilottoremoveInput = input(
                    "Input Social Security Number of Pilot to remove: ")  # Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Pilot succesfully removed!
Current Pilots: [John - 123456789]
--------------------------------------------\n""")

        elif updatevoyageMenuInput == "2":
            print("Current Crew members: [Sansa - 123456789, Bertha - 2607962249]\n")
            print("""1. Update Cew 
--------------------------------------------
  1. Add Crew member
  2. Remove Crew member
--------------------------------------------""")
            updatecrewMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ")
            if updatecrewMenuInput == "1":
                print("""
            1. Add Crew member
--------------------------------------------""")
                pilottoaddInput = input(
                    "Input Social Security Number of Crew member to add: ")  # Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Crew member succesfully added!
                Current Crew members: [Sansa - 123456789, Bertha - 2607962249]
                --------------------------------------------\n""")
            elif updatecrewMenuInput == "2":
                print("""
            2. Remove Crew member
--------------------------------------------""")
                pilottoremoveInput = input(
                    "Input Social Security Number of Crew member to remove: ")  # Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Crew member succesfully removed!
                Current Crew members: [[Sansa - 123456789]
                --------------------------------------------\n""")

        elif updatevoyageMenuInput == "3":
            print("""3. Update Departure from Iceland
--------------------------------------------""")
            print("""Current departure time: 05/29/2015 05:50""")
            departuretimeInput = input("Input new departure time with slashes in between: ")
            print("Departure time succesfully changed!\nNew Departure time: {}\n".format(departuretimeInput))

        elif updatevoyageMenuInput == "4":
            print("""4. Update Departure to Iceland
--------------------------------------------""")
            print("""Current departure time: 05/29/2015 11:20""")
            departuretimeInput = input("Input new departure time with slashes in between: ")
            print("Departure time succesfully changed!\nNew Departure time: {}\n".format(departuretimeInput))

        elif updatevoyageMenuInput == "5":
            voyageID = input("Input voyage ID of the voyage you wish to cancel: ")
            # Route cancelled, return nauðsynlegu info
            print("Voyage succesfully cancelled!\n")

        elif updatevoyageMenuInput == "b":
            Update.updateVoyage(voyageID)
        elif updatevoyageMenuInput == "m":
            Update.updateMenu()
        elif updatevoyageMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("Invalid input")
            updatecurrentflightRoutes()
        # Update.updateMenu(Update) HVAÐ Á ÉG AÐ CALLA HÉR???

    def updateFlights(self):
        print("""5. Update Flights 
--------------------------------------------
  1. Update Flight Status
  2. Update Departure Time
--------------------------------------------""")
        updateflightMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        if updateflightMenuInput == "1":
            flightID = input("Input the ID of the Flight you wish to change: ")
            print("""1. Update Flight Status
Flight - {}: Select Flight Status
--------------------------------------------
  1. Loading 
  2. In-Air
  3. Landed:
  4. Cancelled
--------------------------------------------""".format(flightID))
            updateflightstatusMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
            if updateflightstatusMenuInput == "1":
                currentStatus = "Loading"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID,
                                                      currentStatus))  # Fundið statusinn í þessu sérstaka tilviki
            elif updateflightstatusMenuInput == "2":
                currentStatus = "In-Air"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID,
                                                      currentStatus))  # Fundið statusinn í þessu sérstaka tilviki
            elif updateflightstatusMenuInput == "3":
                currentStatus = "Landed"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID,
                                                      currentStatus))  # Fundið statusinn í þessu sérstaka tilviki
            elif updateflightstatusMenuInput == "4":
                currentStatus = "Cancelled"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID,
                                                      currentStatus))  # Fundið statusinn í þessu sérstaka tilviki
            elif updateairplanestatusMenuInput == "b":
                Update.updateFlights()
            elif updateairplanestatusMenuInput == "q":
                print("Forriti lokað!")
            else:
                print("WRONG INPUT, TRY AGAIN")
                Update.updateFlights()

        elif updateflightMenuInput == "2":
            print("""2. Update Departure from #Destination
--------------------------------------------""")
            print("""Current departure time: 01/01/2015 01:50""")
            departuretimeInput = input("Input new departure time with slashes in between: ")
            print("Departure time succesfully changed!\nNew Departure time: {}\n".format(departuretimeInput))

        elif updateflightMenuInput == "b":
            Update.updateFlights()
        elif updateflightMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateFlights()

    def updateMenu(self):
        print('''Update Data
--------------------------------------------
  1. Update Worker
  2. Update Airplane Status
  3. Update Current Flights routes
  4. Update Voyages
  5. Update Flights
--------------------------------------------''')
        updateMenuInput = input("Input choice (q to Quit, b for Back): ")
        updateMenuInput = updateMenuInput.lower()

        if updateMenuInput == "1":
            ssnInput = Update.confirmSSN(self)
            if ssnInput:
                Update.update_Worker(self, ssnInput)
            else:
                updateMenuInput = Update.updateMenu(self)

        elif updateMenuInput == "2":
            airplaneReg = Update.confirmPlaneReg(self)
            if airplaneReg:
                Update.updateairplaneStatus(self, airplaneReg)
            else:
                updateMenuInput = Update.updateMenu(self)

        elif updateMenuInput == "3":
            flightRouteID = Update.confirmFlightRoute(self)
            if flightRouteID:
                Update.update_Worker(self, flightRouteID)
            else:
                updateMenuInput = Update.updateMenu(self)

        elif updateMenuInput == "4":
            voyageID = Update.confirmVoyageID(self)
            if voyageID:
                Update.update_Worker(self, voyageID)
            else:
                updateMenuInput = Update.updateMenu(self)

        elif updateMenuInput == "5":
            flightID = Update.confirmFlightID(self)
            if flightID:
                Update.update_Worker(self, flightID)
            else:
                updateMenuInput = Update.updateMenu(self)
        elif updateMenuInput == "b":
            return updateMenuInput
        elif updateMenuInput == "q":
            return None
        else:
            print("Wrong input, try again")
            updateMenuInput = Update.updateMenu()
        print("")
        return updateMenuInput

    def confirmSSN(self):
        def validate(ssn):
            return UIAPI.UIAPI.viewWorkerBySSn(self, ssn)

        ssn = input("Input the the Social Security Number of the worker you wish to change (b to back): ")
        if ssn.lower() == "b":
            return False
        result = validate(ssn)
        print(result)
        if result == " not found!":
            Update.confirmSSN(self)
        else:
            return ssn

    def confirmPlaneReg(self):
        def validate(planeReg):
            return UIAPI.UIAPI.viewCertainAirplane(self, planeReg)

        planeReg = input("Input the the Register of the plane you wish to change (b to back): ")
        if planeReg.lower() == "b":
            return False
        result = validate(planeReg)
        print(result)
        if result == "Airplane not found!":
            Update.confirmPlaneReg(self)
        else:
            return planeReg

    def confirmFlightRoute(self):  # vantar virkni í flightRouteLL
        def validate(flightRoute):
            return UIAPI.UIAPI.viewCertainFlightRoute(self, flightRoute)

        flightRouteID = input("Input the the id of the flight route you wish to change (b to back): ")
        if flightRouteID.lower() == "b":
            return False
        result = validate(flightRouteID)
        print(result)
        if result == " not found!":
            Update.confirmPlaneReg(self)
        else:
            return flightRouteID

    def confirmVoyageID(self):  # þarf að útfæra VoyageLL
        print("not yet ready, this is located in Update.py line ~410, ConfirmVoyageID method")

    def confirmFlightID(self):
        def validate(flightID):
            return UIAPI.UIAPI.viewCertainFlight(self, flightID)

        flightID = input("Input the the number of the flight you wish to change (b to back): ")
        if flightID.lower() == "b":
            return False
        result = validate(flightID)
        print(result)
        if result == "Flight not found!":
            Update.confirmFlightID(self)
        else:
            return flightID

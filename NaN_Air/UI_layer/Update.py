import UIAPI
import datetime


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
            print("Exiting program!")
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
        elif updateairplanestatusMenuInput.lower() == "b":
            Update.updateMenu(self)
        elif updateairplanestatusMenuInput.lower() == "m":
            Update.updateMenu(self)
        elif updateairplanestatusMenuInput.lower() == "q":
            print("Exiting program!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateairplaneStatus(self, airplane_reg_num_Input)
        Update.updateMenu(self)

    def updatecurrentflightRoutes(self, flightRouteID):
        print("""3. Update Current Flights Routes
--------------------------------------------
  1. Update Country
  2. Update Airport
  3. Update Flight Distance
  4. Update Travel time
  5. Update Emergency contact 
  6. Update Emergency contact number
--------------------------------------------""")
        updateflightrouteMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        if updateflightrouteMenuInput == "1":
            countryInput = input("Input new country: ")
            flightRouteList = [flightRouteID, "Country", countryInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
        elif updateflightrouteMenuInput == "2":
            airportInput = input("Input name of new airport: ")
            flightRouteList = [flightRouteID, "Airport", airportInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
        elif updateflightrouteMenuInput == "3":
            flightdistanceInput = input("Input new flight distance in kilometers: ")
            flightRouteList = [flightRouteID, "Flight distance", flightdistanceInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
        elif updateflightrouteMenuInput == "4":
            traveltimeInput = input("Input new travel time(f.x. 4:30): ")
            flightRouteList = [flightRouteID, "Travel time", traveltimeInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
        elif updateflightrouteMenuInput == "5":
            emergencycontactInput = input("Input new emergency contact name: ")
            flightRouteList = [flightRouteID, "Emergency contact", emergencycontactInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
        elif updateflightrouteMenuInput == "6":
            emergencycontactnumInput = input("Input new emergency contact number: ")
            flightRouteList = [flightRouteID, "Emergency number", emergencycontactnumInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
        elif updateflightrouteMenuInput == "b":
            Update.updateMenu(self)
        elif updateflightrouteMenuInput == "m":
            Update.updateMenu(self)
        elif updateflightrouteMenuInput == "q":
            print("Exiting program!")
        else:
            print("Invalid input")
            Update.updatecurrentflightRoutes(self, flightRouteID)
        Update.updatecurrentflightRoutes(self, flightRouteID)

    def updateVoyage(self, voyageID):
        print("""4. Update Voyage 
--------------------------------------------
  1. Update Pilots
  2. Update Crew
  3. Update Departure from Iceland
  4. Update Departure to Iceland
  5. Cancel Voyage
--------------------------------------------""")
        updatevoyageMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        if updatevoyageMenuInput == "1":
            UIAPI.UIAPI.requestVoyagePilots(self, voyageID)
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
                pilotToAddInput = input("Input Social Security Number of Pilot to add: ")
                # TODO check if the ssn exists, and is a pilot

                # method call here to verify ssn.. worker related
                print(UIAPI.UIAPI.addPilotVoyage(self, voyageID, pilotToAddInput))
                print("--------------------------------------------")
            elif updatepilotMenuInput == "2":
                print("""
            2. Remove Pilots
--------------------------------------------""")
                pilotToRemoveInput = input("Input Social Security Number of Pilot to remove: ")
                print(UIAPI.UIAPI.removePilotVoyage(self, voyageID, pilotToRemoveInput))
                print("--------------------------------------------")

        elif updatevoyageMenuInput == "2":
            print(UIAPI.UIAPI.requestVoyageCrew(self, voyageID))
            print("""1. Update Crew 
--------------------------------------------
  1. Add Crew member
  2. Remove Crew member
--------------------------------------------""")
            updatecrewMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ")
            if updatecrewMenuInput == "1":
                print("""
            1. Add Crew member
--------------------------------------------""")
                crewToAddInput = input("Input Social Security Number of Crew member to add: ")
                # TODO 'method call here to verify ssn and position'
                print(UIAPI.UIAPI.addCrewVoyage(self, voyageID, crewToAddInput))
                print("--------------------------------------------")
            elif updatecrewMenuInput == "2":
                print("""
            2. Remove Crew member
--------------------------------------------""")
                crewToRemoveInput = input("Input Social Security Number of Crew member to remove: ")
                print(UIAPI.UIAPI.removeCrewVoyage(self, voyageID, crewToRemoveInput))
                print("--------------------------------------------")

        elif updatevoyageMenuInput == "3":
            print("""3. Update Departure from Iceland
--------------------------------------------""")
            flightNumber = UIAPI.UIAPI.requestFromIceFlightNumb(self, voyageID)
            departuretimeInput = input("Input new departure time with slashes in between: ")
            updateList = [flightNumber, "Departure time"]
            print(UIAPI.UIAPI.updateFlightDepartureTime(self, flightNumber, departuretimeInput))

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
            Update.updateVoyage(self, voyageID)
        elif updatevoyageMenuInput == "m":
            Update.updateMenu(self)
        elif updatevoyageMenuInput == "q":
            print("Exiting program!")
        else:
            print("Invalid input")
            Update.updateVoyage(self, voyageID)
        Update.updateVoyage(self, voyageID)

    def updateFlights(self, flightNumber, flightDay):
        print("""5. Update Flights 
--------------------------------------------
  1. Update Flight Status
  2. Update Departure Time
--------------------------------------------""")
        updateflightMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        if updateflightMenuInput == "1":
            print("""1. Update Flight Status
    Select Flight Status
--------------------------------------------
  1. On schedule
  2. Loading 
  3. In-Air
  4. Landed
  5. Cancelled
--------------------------------------------""")
            updateflightstatusMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
            options = ["On schedule", "Loading", "In-Air", "Landed", "Cancelled"]
            if updateflightstatusMenuInput == "1" or "2" or "3" or "4" or "5":
                flight = UIAPI.UIAPI.updateFlightStatus(self, [flightNumber, flightDay, "Flight status", options[int(updateflightstatusMenuInput)-1]])
                print(flight)
                Update.updateFlights(self, flightNumber, flightDay)
            elif updateflightstatusMenuInput == "b":
                Update.updateFlights(self, flightNumber, flightDay)
            elif updateflightstatusMenuInput == "q":
                print("exiting program!")
            else:
                print("WRONG INPUT, TRY AGAIN")
                Update.updateFlights(self, flightNumber, flightDay)

        elif updateflightMenuInput == "2":
            print("""2. Update Departure time
--------------------------------------------""")
            departureTime = input("  - Updated departure time(f.x. 12:30): ")
            hour, minute = map(int, departureTime.split(':'))
            departureDate = input("  - Updated departure date(f.x. 24/12/2019): ")
            day, month, year = map(int, departureDate.split('/'))
            departureDateTime = datetime.datetime(year, month, day, hour, minute, 00)
            departureTimeList = [flightNumber, flightDay, "Departure time", departureDateTime]
            flight = UIAPI.UIAPI.updateFlightDepartureTime(self, departureTimeList)
            print(flight)
        elif updateflightMenuInput == "b":
            Update.updateFlights(self, flightNumber)
        elif updateflightMenuInput == "q":
            print("exiting program!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateFlights(self, flightNumber)

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
                Update.updatecurrentflightRoutes(self, flightRouteID)
            else:
                updateMenuInput = Update.updateMenu(self)

        elif updateMenuInput == "4":
            voyageID = Update.confirmVoyageID(self)
            if voyageID:
                Update.update_Worker(self, voyageID)
            else:
                updateMenuInput = Update.updateMenu(self)

        elif updateMenuInput == "5":
            flightNum, flightDay = Update.confirmFlightNumOnDay(self)
            if flightNum:
                Update.updateFlights(self, flightNum, flightDay)
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

    def confirmFlightNumOnDay(self):
        #def validate(flightNum):
            #return UIAPI.UIAPI.viewCertainFlight(self, flightNum)

        flightNum = input("Input the the number of the flight you wish to change (b to back): ")
        flightDay = input("Input the day of the flight you want to update(f.x. 31/12/2019): ")
        day, month, year = map(int, flightDay.split('/'))
        flightDate = datetime.datetime(year, month, day)
        if flightNum.lower() == "b":
            return False
        #result = validate(flightNum)
        #print(result)
        #if result == "Flight not found!":
            #Update.confirmFlightID(self)
        #else:
        return flightNum, flightDate

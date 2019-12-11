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
        updateWorkerMenuInput = input("Input choice (q to Quit, b for Back): ")
        updateWorkerMenuInput = updateWorkerMenuInput.lower()

        if updateWorkerMenuInput == "1":
            newHomeAddress = input("Input new home address: ")
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Address", newHomeAddress))
            return "b"

        elif updateWorkerMenuInput == "2":
            newPhoneNumber = input("Input new phone number: ")
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Phone", newPhoneNumber))
            return "b"

        elif updateWorkerMenuInput == "3":
            newCellNumber = input("Input new cellphone number: ")
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Cellphone", newCellNumber))
            return "b"

        elif updateWorkerMenuInput == "4":
            newEmail = input("Input new E-mail Address: ")
            print(UIAPI.UIAPI.updateWorker(self, workerSSN, "Email", newEmail))
            return "b"

        elif updateWorkerMenuInput == "b":
            return updateWorkerMenuInput
        elif updateWorkerMenuInput == "q":
            print("Exiting program!")
            return updateWorkerMenuInput
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.update_Worker(self, workerSSN)
        return updateWorkerMenuInput

    def updateairplaneStatus(self, airplane_reg_num_Input):
        print("""2. Update Airplane Status
--------------------------------------------
        Select Airplane Status
--------------------------------------------
  1. Working
  2. Engine failure
  3. On Repair
  4. Needs inspection
--------------------------------------------""")
        updateairplanestatusMenuInput = input("Input choice (q to Quit, b for Back): ")
        options = ["Working", "Engine failure", "On repair", "Needs inspection"]
        if updateairplanestatusMenuInput == "1" or "2" or "3" or "4":
            if updateairplanestatusMenuInput == "1":
                print(UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[0]))
                return "b"
            elif updateairplanestatusMenuInput == "2":
                print(UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[1]))
                return "b"
            elif updateairplanestatusMenuInput == "3":
                print(UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[2]))
                return "b"
            elif updateairplanestatusMenuInput == "4":
                print(UIAPI.UIAPI.updateAirplaneStatus(self, airplane_reg_num_Input, options[3]))
                return "b"
        elif updateairplanestatusMenuInput.lower() == "b":
            return updateairplanestatusMenuInput
        elif updateairplanestatusMenuInput.lower() == "q":
            print("Exiting program!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateairplaneStatus(self, airplane_reg_num_Input)
        return updateairplanestatusMenuInput

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
        updateflightrouteMenuInput = input("Input choice (q to Quit, b for Back): ")
        if updateflightrouteMenuInput == "1":
            countryInput = input("Input new country: ")
            flightRouteList = [flightRouteID, "Country", countryInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
            return "b"
        elif updateflightrouteMenuInput == "2":
            airportInput = input("Input name of new airport: ")
            flightRouteList = [flightRouteID, "Airport", airportInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
            return "b"
        elif updateflightrouteMenuInput == "3":
            flightdistanceInput = input("Input new flight distance in kilometers: ")
            flightRouteList = [flightRouteID, "Flight distance", flightdistanceInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
            return "b"
        elif updateflightrouteMenuInput == "4":
            traveltimeInput = input("Input new travel time(f.x. 4:30): ")
            flightRouteList = [flightRouteID, "Travel time", traveltimeInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
            return "b"
        elif updateflightrouteMenuInput == "5":
            emergencycontactInput = input("Input new emergency contact name: ")
            flightRouteList = [flightRouteID, "Emergency contact", emergencycontactInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
            return "b"
        elif updateflightrouteMenuInput == "6":
            emergencycontactnumInput = input("Input new emergency contact number: ")
            flightRouteList = [flightRouteID, "Emergency number", emergencycontactnumInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            Update.updatecurrentflightRoutes(self, flightRouteID)
            return "b"
        elif updateflightrouteMenuInput == "b":
            Update.updateMenu(self)
        elif updateflightrouteMenuInput == "q":
            print("Exiting program!")
        else:
            print("Invalid input")
            Update.updatecurrentflightRoutes(self, flightRouteID)
        return updateflightrouteMenuInput

    def updateVoyage(self, voyageID):
        print("""4. Update Voyage 
--------------------------------------------
  1. Update Crew
  2. Update Departure from Iceland
  3. Update Departure to Iceland
  4. Cancel Voyage
--------------------------------------------""")
        updatevoyageMenuInput = input("Input choice (q to Quit, b for Back): ")
        if updatevoyageMenuInput == "1":
            UIAPI.UIAPI.requestVoyagePilots(self, voyageID)
            print("""1. Update Pilots 
--------------------------------------------
  1. Add Captain
  2. Add Co pilot
  3. Add Flight Service Manager
  4. Add Flight Attendant(s)
--------------------------------------------""")
            updatepilotMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
            if updatepilotMenuInput == "1":
                print("""
  1. Add Pilot
--------------------------------------------""")
                # adding pilot to voyage
                pilotToAddInput = input("Input Social Security Number of Pilot to add: ")
                print(UIAPI.UIAPI.addCaptainVoyage(self, voyageID, pilotToAddInput))

                print("--------------------------------------------")
                return "b"
            elif updatepilotMenuInput == "2":
                print("""
            2. Add Co pilot
--------------------------------------------""")
                pilotToRemoveInput = input("Input Social Security Number of Co Pilot to add: ")
                print(UIAPI.UIAPI.addCoPilotVoyage(self, voyageID, pilotToRemoveInput))
                print("--------------------------------------------")
                return "b"

            elif updatepilotMenuInput == "3":
                print("""
                      3. Add Flight Service Manager
        --------------------------------------------""")
                pilotToRemoveInput = input("Input Social Security Number of Flight Service Manager to add: ")
                print(UIAPI.UIAPI.addMainFlightAttendantVoyage(self, voyageID, pilotToRemoveInput))
                print("--------------------------------------------")
                return "b"

            elif updatepilotMenuInput == "4":
                print("""
                        4. Add Flight Attendant(s)
            --------------------------------------------""")
                pilotToRemoveInput = input("Input Social Security Number of Flight Attendant to add: ")
                print(UIAPI.UIAPI.addFlightAttendantVoyage(self, voyageID, pilotToRemoveInput))
                print("--------------------------------------------")
                return "b"


        elif updatevoyageMenuInput == "2":
            print("""3. Update Departure from Iceland
--------------------------------------------""")
            flightNumber = UIAPI.UIAPI.requestFromIceFlightNumb(self, voyageID)
            departuretimeInput = input("Input new departure time with slashes in between: ")
            updateList = [flightNumber, "Departure time", departuretimeInput]
            print(UIAPI.UIAPI.updateFlightDepartureTime(self, updateList))
            return "b"

        elif updatevoyageMenuInput == "3":
            print("""4. Update Departure to Iceland
--------------------------------------------""")
            flightNumber = UIAPI.UIAPI.requestToIceFlightNumb(self, voyageID)
            departuretimeInput = input("Input new departure time with slashes in between: ")
            updateList = [flightNumber, "Departure time", departuretimeInput]
            print(UIAPI.UIAPI.updateFlightDepartureTime(self, updateList))
            return "b"

        elif updatevoyageMenuInput == "4":
            voyageID = input("Input voyage ID of the voyage you wish to cancel: ")
            print(UIAPI.UIAPI.cancelVoyage(self, voyageID))
            return "b"

        elif updatevoyageMenuInput == "b":
            return updatevoyageMenuInput
        elif updatevoyageMenuInput == "q":
            print("Exiting program!")
        else:
            print("Invalid input")
            Update.updateVoyage(self, voyageID)
        return updatevoyageMenuInput

    def updateFlights(self, flightNumber, flightDay):
        print("""5. Update Flights 
--------------------------------------------
  1. Update Flight Status
  2. Update Departure Time
--------------------------------------------""")
        updateflightMenuInput = input("Input choice (q to Quit, b for Back): ")
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
            updateflightstatusMenuInput = updateflightstatusMenuInput.lower()
            options = ["On schedule", "Loading", "In-Air", "Landed", "Cancelled"]
            if updateflightstatusMenuInput == "1" or "2" or "3" or "4" or "5":
                flight = UIAPI.UIAPI.updateFlightStatus(self, [flightNumber, flightDay, "Flight status", options[int(updateflightstatusMenuInput)-1]])
                print(flight)
                Update.updateFlights(self, flightNumber, flightDay)
                return "b"
            elif updateflightstatusMenuInput == "b":
                return updateflightstatusMenuInput
            elif updateflightstatusMenuInput == "q":
                print("exiting program!")
            else:
                print("WRONG INPUT, TRY AGAIN")
                Update.updateFlights(self, flightNumber, flightDay)
            return updateflightstatusMenuInput

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
            return updateflightMenuInput
        elif updateflightMenuInput == "q":
            print("exiting program!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateFlights(self, flightNumber, flightDay)
        return updateflightMenuInput

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
            instance = ""
            print(UIAPI.UIAPI.viewAllWorkers(self))
            while type(instance) == str:
                ssnInput = input("Input the SSN of the Worker you wish to change properties: ")
                instance = UIAPI.UIAPI.viewWorkerBySSn(self, ssnInput)
                print(instance)
            output = Update.update_Worker(self, ssnInput)
            if output == "b":
                Update.updateMenu(self)
            elif output == "q":
                return output

        elif updateMenuInput == "2":
            instance = ""
            allAirplanes = UIAPI.UIAPI.viewAllAirplanes(self)
            for i in allAirplanes:
                print(i, "\n")

            while type(instance) == str:
                regInput = input("Input the Register of the Plane you wish to change properties: ")
                instance = UIAPI.UIAPI.viewCertainAirplane(self, regInput)
                print(instance)
            output = Update.updateairplaneStatus(self, regInput)
            if output == "b":
                Update.updateMenu(self)
            elif output == "q":
                return output

        elif updateMenuInput == "3":
            instance = ""
            routes = UIAPI.UIAPI.viewAllFlightRoutes(self)
            for route in routes:
                print(route, "\n")
            while type(instance) == str:
                flightrouteID = input("Input the ID of the Flight Route you wish to change properties: ")
                instance = UIAPI.UIAPI.viewFlightRoute(self, flightrouteID)
                print(instance)
            output = Update.updatecurrentflightRoutes(self, flightrouteID)

        elif updateMenuInput == "4":
            instance = ""
            allVoyages = UIAPI.UIAPI.viewallVoyages(self)
            for i in allVoyages:
                print(i)
            while type(instance) == str:
                voyageID = input("Input the ID of the Voyage you wish to change properties: ")
                instance = UIAPI.UIAPI.viewVoyage(self, voyageID)
                print(instance)
            output = Update.updateVoyage(self, voyageID)
            if output == "b":
                Update.updateMenu(self)
            elif output == "q":
                return output

        elif updateMenuInput == "5":
            Test = (UIAPI.UIAPI.viewAllFlights(self))
            for i in Test:
                print(i)
                print("")
            flightNum, flightDay = Update.confirmFlightNumOnDay(self)
            if flightNum:
                output = Update.updateFlights(self, flightNum, flightDay)
                if output == "b":
                    Update.updateMenu(self)
                elif output == "q":
                    return output
            else:
                Update.updateMenu(self)
        elif updateMenuInput == "b":
            print("to the menu")
            return "b"
        elif updateMenuInput == "q":
            return updateMenuInput
        else:
            print("Wrong input, try again")
            Update.updateMenu(self)
        return output

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

import UIAPI
import datetime
class Update:
    def __init__(self):
        self.uiapi = UIAPI.UIAPI()

    def update_Worker(self, ssn):
        print("""1. Update Worker
--------------------------------------------
  1. Home Address: 
  2. Home Phone Number:
  3. Mobile Phone Number:
  4. E-mail Address
--------------------------------------------""")
        workerSSN = input("Input Social Security Number of the worker: ")
        #If ssn exists:
        #Else print("This worker does not exist")
        updateWorkerMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        updateWorkerMenuInput = updateWorkerMenuInput.lower()
        if updateWorkerMenuInput == "1":
           # print("Current Home Address: Rasberry Street 1") Flækir töluvert, spurning hvort að þetta sé must eða hvort að það sé nóg að prenta bara tilvikið eftir að því er breytt
            newhomeAddress = input("Input new home address: ")
            addressUpdate = UIAPI.UIAPI.updateWorker(workerSSN, "Address", newhomeAddress) 
            """if addressUpdate != None:"""
            #Ef við náum að breyta addressunni, chekka í logic layer?
            #print("Home address succesfully changed!\nNew Home Address: {}".format(newhomeAddress))
            print("Home address succesfully changed!\n")
            viewWorkerBySSn(self, workerSSN, pos = "")
            #Vantar að klára updateWorker function
            return updateWorkerMenuInput
        elif updateWorkerMenuInput == "2":
            newhphoneNumber = int(input("Input new phone number: "))
            updatedPhoneNum = UIAPI.UIAPI.updateWorker(self, workerSSN, key, newhphoneNumber)
            Update.update_Worker(ssn)
            #print("Current Phone Number: 5812345")
            print("Phone number succesfully changed!\n")
            viewWorkerBySSn(self, workerSSN, pos = "")
            Update.update_Worker(ssn)
        elif updateWorkerMenuInput == "3":
            #print("Current Mobile Phone Number is: 5812345")
            newhhomeNumber = int(input("Input new home number: "))
            print("Phone number succesfully changed!\n")
            viewWorkerBySSn(self, workerSSN, pos = "")
            Update.update_Worker(ssn)
        elif updateWorkerMenuInput == "4":
            #print("Current E-mail Address is: alexanders19@ru.is")
            newEmail = input("Input new E-mail Address: ")
            print("New E-mail Address is: {}\n".format(newEmail))
            Update.update_Worker(ssn)
        elif updateWorkerMenuInput == "b":
            Update.updateMenu()
        elif updateWorkerMenuInput == "q":
            print("Forriti lokað!")
            return updateWorkerMenuInput
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.update_Worker()
        # return ssn og key,

    def updateairplaneStatus(airplane_reg_num_Input):
        # airplane_reg_num_Input = input("Input Airplane Registration Number: ")
        # Þetta ákveðna tilvik af airplane fundið
        print("""2. Update Airplane Status
Boeing - {}: Select Airplane Status
--------------------------------------------
  1. Loading 
  2. In-Air
  3. Landed:
  4. Cancelled
--------------------------------------------""".format(airplane_reg_num_Input))
        updateairplanestatusMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
        updateairplanestatusMenuInput = updateairplanestatusMenuInput  # Á að taka inn int
        if updateairplanestatusMenuInput == "1":
            current_status = "Loading"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input,
                                                  current_status))  # Fundið statusinn í þessu sérstaka tilviki
        elif updateairplanestatusMenuInput == "2":
            current_status = "In-Air"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input,
                                                  current_status))  # Fundið statusinn í þessu sérstaka tilviki
        elif updateairplanestatusMenuInput == "3":
            current_status = "Landed"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input,
                                                  current_status))  # Fundið statusinn í þessu sérstaka tilviki
        elif updateairplanestatusMenuInput == "4":
            current_status = "Cancelled"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input,
                                                  current_status))  # Fundið statusinn í þessu sérstaka tilviki
        elif updateairplanestatusMenuInput == "b":
            Update.updateMenu()
        elif updateairplanestatusMenuInput == "m":
            Update.updateMenu()
        elif updateairplanestatusMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateairplaneStatus()
        Update.updateMenu()
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
            countryInput = input("Input new country: ")
            flightRouteList = [flightrouteID, "Country", countryInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            updateflightrouteMenuInput = Update.updatecurrentflightRoutes(self)
        elif updateflightrouteMenuInput == "2":
            airportInput = input("Input name of new airport: ")
            flightRouteList = [flightrouteID, "Airport", airportInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            updateflightrouteMenuInput = Update.updatecurrentflightRoutes(self)
        elif updateflightrouteMenuInput == "3":
            flightdistanceInput = input("Input new flight distance in kilometers: ")
            flightRouteList = [flightrouteID, "Flight distance", flightdistanceInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            updateflightrouteMenuInput = Update.updatecurrentflightRoutes(self)
        elif updateflightrouteMenuInput == "4":
            traveltimeInput = input("Input new travel time(f.x. 4:30): ")
            flightRouteList = [flightrouteID, "Travel time", traveltimeInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            updateflightrouteMenuInput = Update.updatecurrentflightRoutes(self)
        elif updateflightrouteMenuInput == "5":
            emergencycontactInput = input("Input new emergency contact name: ")
            flightRouteList = [flightrouteID, "Emergency contact", emergencycontactInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            updateflightrouteMenuInput = Update.updatecurrentflightRoutes(self)
        elif updateflightrouteMenuInput == "6":
            emergencycontactnumInput = input("Input new emergency contact number: ")
            flightRouteList = [flightrouteID, "Emergency number", emergencycontactnumInput]
            flightRoute = UIAPI.UIAPI.updateFlightRoute(self, flightRouteList)
            print(flightRoute)
            updateflightrouteMenuInput = Update.updatecurrentflightRoutes(self)
        elif updateflightrouteMenuInput == "b":
            Update.updateMenu(self)
        elif updateflightrouteMenuInput == "m":
            Update.updateMenu(self)
        elif updateflightrouteMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("Invalid input")
            updatecurrentflightRoutes()
        print("")
        # Update.updateMenu(Update) HVAÐ Á ÉG AÐ CALLA HÉR???

    def updateVoyage(voyageID):
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
                pilottoaddInput = input("Input Social Security Number of Pilot to add: ")  # Bæta við chekki sem kannar hvort að þetta sé main pilot
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
            flightNumber = input("Input the Flight number of the Flight you wish to change: ")
            print("""1. Update Flight Status
Flight - {}: Select Flight Status
--------------------------------------------
  1. Loading 
  2. In-Air
  3. Landed
  4. Cancelled
--------------------------------------------""".format(flightNumber))
            updateflightstatusMenuInput = input("Input choice (q to Quit, b for Back, m for Main Menu): ")
            flightlist = [flightNumber, "Flight status"]
            if updateflightstatusMenuInput == "1":
                flightlist.append("Loading")
                flight = UIAPI.UIAPI.updateFlightStatus(self, flightlist)
                print(flight)
                flightlist.pop()
            elif updateflightstatusMenuInput == "2":
                flightlist.append("In-Air")
                flight = UIAPI.UIAPI.updateFlightStatus(self, flightlist)
                print(flight)
                flightlist.pop()
            elif updateflightstatusMenuInput == "3":
                flightlist.append("Landed")
                flight = UIAPI.UIAPI.updateFlightStatus(self, flightlist)
                print(flight)
                flightlist.pop()
            elif updateflightstatusMenuInput == "4":
                flightlist.append("Cancelled")
                flight = UIAPI.UIAPI.updateFlightStatus(self, flightlist)
                print(flight)
                flightlist.pop()
            elif updateairplanestatusMenuInput == "b":
                Update.updateFlights()
            elif updateairplanestatusMenuInput == "q":
                print("Forriti lokað!")
            else:
                print("WRONG INPUT, TRY AGAIN")
                Update.updateFlights()

        elif updateflightMenuInput == "2":
            print("""2. Update Departure time
--------------------------------------------""")
            flightNumber = input("Input the Flight number of the Flight you wish to change: ")
            departureTime = input("  - Updated departure time(f.x. 12:30): ")
            hour, minute = map(int, departureTime.split(':'))
            departureDate = input("  - Updated departure date(f.x. 24/12/2019): ")
            day, month, year = map(int, departureDate.split('/'))
            departureDateTime = datetime.datetime(year,month, day, hour, minute, 00)
            departureTimeList = [flightNumber, "Departure time", departureDateTime]
            flight = UIAPI.UIAPI.updateFlightDepartureTime(self, departureTimeList)
            print(flight)
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
            ssnInput = int(input("Input the the Social Security Number of the worker you wish to change: "))
            Update.update_Worker(ssnInput)  # Kallar á update worker function
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "2":
            airplane_reg_num_Input = input("Input Airplane Registration Number: ")
            Update.updateairplaneStatus(self)  # Kallar á update airplane status function
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "3":
            Update.updatecurrentflightRoutes(self)
            updateMenuInput = Update.updateMenu(self)
        elif updateMenuInput == "4":
            voyageID = input("Input voyage ID: ")  # Þetta ákveðna tilvik af flight route fundið
            Update.updateVoyage(voyageID)  # Kallar á update voyage function
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "5":
            Update.updateFlights(self)
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

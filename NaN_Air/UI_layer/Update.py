class Update():

    def update_Worker():
        ssnInput = int(input("Input the the Social Security Number of the worker you wish to change: "))
        print("""1. Update Worker
John - {}
--------------------------------------------
1. Home Address: 
2. Home Phone Number:
3. Mobile Phone Number:
4. E-mail Address
--------------------------------------------""".format(ssnInput))
        updateWorkerMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ")
        updateWorkerMenuInput = updateWorkerMenuInput.lower()
        if updateWorkerMenuInput == "1":
            print("Current Home Address: Rasberry Street 1")
            newhomeAddress = input("Input new value: ")
            print("New Home Address: {}".format(newhomeAddress))
            Update.updateMenu()
        elif updateWorkerMenuInput == "2":
            print("Current Phone Number: 5812345")
            newhphoneNumber = int(input("Input Phone Number: "))
            print("New Phone Number is: {}".format(newhphoneNumber))
            Update.updateMenu()
        elif updateWorkerMenuInput == "3":
            print("Current Mobile Phone Number is: 5812345")
            newhhomeNumber = int(input("Input new Home Number: "))
            print("New Phone Number is: {}".format(newhhomeNumber))
            Update.updateMenu()
        elif updateWorkerMenuInput == "4":
            print("Current E-mail Address is: alexanders19@ru.is")
            newEmail = input("Input new E-mail Address: ")
            print("New E-mail Address is: {}\n".format(newEmail))
        elif updateWorkerMenuInput == "b":
            Update.updateMenu()
        elif updateWorkerMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.update_Worker(self)
        #return ssn og key, 
        
                
    def updateairplaneStatus():
        airplane_reg_num_Input = input("Input Airplane Registration Number: ")
        #Þetta ákveðna tilvik af airplane fundið
        print("""2. Update Airplane Status
Boeing - {}: Select Airplane Status
--------------------------------------------
1. Loading 
2. In-Air
3. Landed:
4. Cancelled
--------------------------------------------""".format(airplane_reg_num_Input))
        updateairplanestatusMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ")
        updateairplanestatusMenuInput = updateairplanestatusMenuInput #Á að taka inn int
        if updateairplanestatusMenuInput == "1":
            current_status = "Loading"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input, current_status)) #Fundið statusinn í þessu sérstaka tilviki
        elif updateairplanestatusMenuInput == "2":
            current_status = "In-Air"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input, current_status)) #Fundið statusinn í þessu sérstaka tilviki
        elif updateairplanestatusMenuInput == "3":
            current_status = "Landed"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input, current_status)) #Fundið statusinn í þessu sérstaka tilviki
        elif updateairplanestatusMenuInput == "4":
            current_status = "Cancelled"
            print("Status succesfully updated!")
            print("BOEING {} status: {}\n".format(airplane_reg_num_Input, current_status)) #Fundið statusinn í þessu sérstaka tilviki
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
        #return airplane reg num og key

    def updatecurrentflightRoutes():
        flightrouteID = input("Input flight route ID: ") #Þetta ákveðna tilvik af flight route fundið
        print("Country: Iceland\nAirport: Keflavik\nFlight Distance: 700 km\nTravel time: 75 minutes")
        print("""3. Update Current Flights Routes
--------------------------------------------
1. Update Country
2. Update Airport
3. Update Flight Distance
4. Update Travel time
5. Update Emergency contact 
6. Update Emergency contact number
--------------------------------------------""")
        updateflightrouteMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ") #Á að taka inn int
        if updateflightrouteMenuInput == "1":
            print("Current country: Greece ")
            countryInput = input("Input new country: ")
            print("Country succesfully changed!\nNew country: {}".format(countryInput))
        elif updateflightrouteMenuInput == "2":
            print("Current airport: Antetekounmpo airport")
            airportInput = input("Input name of new airport: ")
            print("Airport succesfully changed!\nNew aiport: {}".format(airportInput))
        elif updateflightrouteMenuInput == "3":
            print("Current Flight Distance: 500 km\n")
            flightdistanceInput = input("Input new flight distance in kilometers: ")
            print("Flight Distance succesfully changed!\nNew flight distance: {} km".format(flightdistanceInput))
        elif updateflightrouteMenuInput == "4":
            print("Current travel time: 120 minutes")
            traveltimeInput = input("Input new travel time in minutes: ")
            print("Travel Time succesfully changed!\nNew travel time: {} minutes".format(traveltimeInput))
        elif updateflightrouteMenuInput == "5":
            print("Current Emergency Contact: Gunni")
            emergencycontactInput = input("Input new value: ")
            print("Emergency Contact succesfully changed!\nNew emergency contact: {}".format(emergencycontactInput))
        elif updateflightrouteMenuInput == "6":
            print("Current Emergency Contact number: 5812345")
            emergencycontactnumInput = input("Input new value: ")
            print("Emergency Contact number succesfully changed!\nNew emergency contact number: {}".format(emergencycontactnumInput))
        elif updateairplanestatusMenuInput == "b":
            Update.updateMenu()
        elif updateairplanestatusMenuInput == "m":
            Update.updateMenu()
        elif updateairplanestatusMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("Invalid input")
            updatecurrentflightRoutes()
        print("")
        #Update.updateMenu(Update) HVAÐ Á ÉG AÐ CALLA HÉR???

    def updateVoyage():
        voyageID = input("Input voyage ID: ") #Þetta ákveðna tilvik af flight route fundið
        print("""Voyage ID: {}
        Flight out ID: NA21x
        Flight back ID:NA21(x+1)
        Pilots: [John - 123456789, Hooper - 2607962249]
        Crew: [Emma - 12436576, Jónsi - 3434656539]
        Flight route ID: 23
        Departure from Iceland: datetime
        Departure to Iceland: datetime""".format(voyageID))
        print("""4. Update Voyage 
--------------------------------------------
1. Update Pilots
2. Update Crew
3. Update Departure from Iceland
4. Update Departure to Iceland
5. Cancel Voyage
--------------------------------------------""")
        updatevoyageMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ") #Á að taka inn int
        if updatevoyageMenuInput == "1":
            print("Current Pilots: [John - 123456789, Hooper - 2607962249]")
            print("""1. Update Pilots 
--------------------------------------------
1. Add Pilot(s)
2. Remove Pilot(s)
--------------------------------------------""")
            updatepilotMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ")
            if updatepilotMenuInput == "1":
                print("""
            1. Add Pilot
--------------------------------------------""")
                pilottoaddInput = input("Input Social Security Number of Pilot to add: ") #Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Pilot succesfully added!
Current Pilots: [John - 123456789, Hooper - 2607962249]
--------------------------------------------""")
            elif updatepilotMenuInput == "2":
                print("""
            2. Remove Pilots
--------------------------------------------""")
                pilottoremoveInput = input("Input Social Security Number of Pilot to remove: ") #Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Pilot succesfully removed!
Current Pilots: [John - 123456789]
--------------------------------------------""")
                
        elif updatevoyageMenuInput == "2":
            print("Current Crew members: [Sansa - 123456789, Bertha - 2607962249]")
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
                pilottoaddInput = input("Input Social Security Number of Crew member to add: ") #Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Crew member succesfully added!
                Current Crew members: [Sansa - 123456789, Bertha - 2607962249]
                --------------------------------------------""")
            elif updatecrewMenuInput == "2":
                print("""
            2. Remove Crew member
--------------------------------------------""")
                pilottoremoveInput = input("Input Social Security Number of Crew member to remove: ") #Bæta við chekki sem kannar hvort að þetta sé main pilot
                print("""Crew member succesfully removed!
                Current Crew members: [[Sansa - 123456789]
                --------------------------------------------""")
        
        elif updatevoyageMenuInput == "3":
            print("""3. Update Departure from Iceland
--------------------------------------------""")
            print("""Current departure time: 05/29/2015 05:50""")
            departuretimeInput = input("Input new departure time with slashes in between: ")
            print("Departure time succesfully changed!\nNew Departure time: {}".format(departuretimeInput))
        
        elif updatevoyageMenuInput == "4":
            print("""4. Update Departure to Iceland
--------------------------------------------""")
            print("""Current departure time: 05/29/2015 11:20""")
            departuretimeInput = input("Input new departure time with slashes in between: ")
            print("Departure time succesfully changed!\nNew Departure time: {}".format(departuretimeInput))
        
        elif updatevoyageMenuInput == "5":
            voyageID = input("Input voyage ID of the voyage you wish to cancel: ") 
            #Route cancelled, return nauðsynlegu info
            print("Voyage succesfully cancelled!")

        elif updatevoyageMenuInput == "b":
            Update.updateVoyage()
        elif updatevoyageMenuInput == "m":
            Update.updateMenu()
        elif updatevoyageMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("Invalid input")
            updatecurrentflightRoutes()
        print("")
        #Update.updateMenu(Update) HVAÐ Á ÉG AÐ CALLA HÉR???

    def updateFlights(): 
        print("""5. Update Flights 
--------------------------------------------
1. Update Flight Status
2. Update Departure Time
--------------------------------------------""")  
        updateflightMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ")
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
            updateflightstatusMenuInput = input("Input choice(q to Quit, b for Back, m for Main Menu): ")
            if updateflightstatusMenuInput == "1":
                currentStatus = "Loading"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID, currentStatus)) #Fundið statusinn í þessu sérstaka tilviki
            elif updateflightstatusMenuInput == "2":
                currentStatus = "In-Air"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID, currentStatus)) #Fundið statusinn í þessu sérstaka tilviki
            elif updateflightstatusMenuInput == "3":
                currentStatus = "Landed"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID, currentStatus)) #Fundið statusinn í þessu sérstaka tilviki
            elif updateflightstatusMenuInput == "4":
                currentStatus = "Cancelled"
                print("Status succesfully updated!")
                print("Flight {} status: {}\n".format(flightID, currentStatus)) #Fundið statusinn í þessu sérstaka tilviki
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
            print("Departure time succesfully changed!\nNew Departure time: {}".format(departuretimeInput))

        elif updateflightMenuInput == "b":
                Update.updateFlights()
        elif updateflightMenuInput == "q":
            print("Forriti lokað!")
        else:
            print("WRONG INPUT, TRY AGAIN")
            Update.updateFlights()

    def updateMenu():
        print('''Update Data
--------------------------------------------
  1. Update Worker
  2. Update Airplane Status
  3. Update Current Flights routes
  4. Update Voyages
  5. Update Flights
--------------------------------------------''')
        updateMenuInput = input("Input choice(q to Quit, b for Back): ")
        updateMenuInput = updateMenuInput.lower()
        
        if updateMenuInput == "1":
            Update.update_Worker() #Kallar á update worker function
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "2":
            Update.updateairplaneStatus() #Kallar á update airplane status function
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "3":
            Update.updatecurrentflightRoutes()
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "4":
            Update.updateVoyage() #Kallar á update voyage function
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "5":
            Update.updateFlights()
            updateMenuInput = Update.updateMenu()
        elif updateMenuInput == "b":
            return updateMenuInput
        elif updateMenuInput == "q":
            return updateMenuInput
        else:
            print("Wrong input, try again")
            updateMenuInput = Update.updateMenu()
        return updateMenuInput

Update.updateairplaneStatus()

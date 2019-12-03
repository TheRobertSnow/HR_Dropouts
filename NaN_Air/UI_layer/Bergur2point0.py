
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
            viewAttendants()
        
        elif viewWorkerInput == "3":
            viewBosses() 

        elif viewWorkerInput == "4":
            viewAllStaff()
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
        PilotSSN = input("  - Please input SSN")
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
    def viewSpecificAttendant():
        AttendantSSN = input("  - Please input SSN")
        AttendantInfo = getAttendantInfo(AttendantSSN)
        print(AttendantInfo)
    def viewAllAttendants
#Bosses

    def viewBosses():
        print('''-----------------------------------------
        View Bosses
----------------------------------------- ''')

        BossInfo = getAllBosses()
        print(BossInfo)


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
            viewSpecificRoute()
        elif viewFlightRoutesInput == "2":
            viewAllRoutes()

        

############################################
  #  def viewVoyages():


############################################
   # def viewFlight():
        
    


View.viewMenu()



################################################################
"""
#View Data menu
print('''-----------------------------------------
        View Data
-----------------------------------------

1 View worker
2 View Airplane
3 View Flight routes
4 View Voyages
5 View Flight
(Input "b" for back or "m" for main menu)
-----------------------------------------''')
# Worker:

print('''       View Worker
-----------------------------------------
    1 View Pilots
    2 View Attendants
    3 View Bosses
    4 View All Staff''')


print('''View Pilots
-----------------------------------------
  1 View Specific Pilot
  2 View All Pilots''')
#1
print('''  - Please Input Staff SSN
''')
#right SSN
print('''Pilot information
-----------------------------------------
Name:
Number:
Gmail:
Licence type:
Availability:
''')
#2
print('''-----------------------------------------
1 Sort by Airplane licence
2 Sort by name
3 View like its in file''')


print('''-----------------------------------------
        View Attendants
-----------------------------------------
    1 View Specific Attendants
    2 View All Attendants''')

print('''-----------------------------------------
        Attendants information
-----------------------------------------
    Name:
    Number:
    Gmail:
    Licence type:
    Availability:
''')


#View airplane

print('''-----------------------------------------
        View Airplane
-----------------------------------------

1 View specific airplane
2 View All Airplanes
''')

#1
print('  - Please input Airplane ID: ')
print('''-----------------------------------------
        View specific airplane
-----------------------------------------
ID: 
Plane register:
Manufacturer:
Model:
Status:
Number of seats:
Odometer:''')

#2
print('''-----------------------------------------
        View All Airplane
-----------------------------------------
1 Sort by Type
2 Sort by (eh) ''')
print('''
        Airplanes
Type:{} 
ID: {} 
Seat Number:{}
Date when available: {}
Current Country: {}
Flight register: {}
''')

#View Flight routes

print('''-----------------------------------------
        View Flight Routes
-----------------------------------------
1 Specific Route
2 All Flight Routes
''')
#1
print('''  - Please input Flight Route ID: ''')
#if its correct
print('''
ID:
Country: 
Airport:
Flight Distance:
Travel Time:
Emergency Contact:
Emergency Number:
''')

# View Voyages


print('''-----------------------------------------
        View Voyages
-----------------------------------------

1 View a Specific Voyage
2 View all Voyages
3 (Möguleiki að hafa cancelled og búin voyage i sér skipun)
4 ()
''')

#1
print('''       
  - Please input Voyage ID:
    
Viewing Voyage 4872949
    
Flight out: (Country eða ID?,frekar Country)
Departure time: (flight out)
Flight in: (Country eða ID?,frekar Country)
Departure time: (flight in)
Pilots: 
Crew:
Flight Route:

''')

#2

print('''
        View All Voyages

Voyage ID,Flight out ID,Flight back ID,Pilots,Crew,Flight route ID,-
Departure from IS Departure to IS

Voyage ID
Flight out ID
Flight back ID
Pilots
Crew
Flight route ID
Departure from IS 
Departure to IS
''')
# pælingin er að infromationið prentast eins og það er í csv
# annað hvort á hlið eða lóðrétt


# Flight

print('''-----------------------------------------
        View Flight
-----------------------------------------

1 View specific Flight
2 View All FLights
3 View Active Flights
4 View Cancelled Flights
''')

#1

print('''
        View specific Flight

  - PleaseFlight ID

Flight Information:
-----------------------------------------
Flight number:
Airplane ID:
Flight route ID:
Flight Status:
Travel Time:
Departure Time:
Arrival Time

''')

"""


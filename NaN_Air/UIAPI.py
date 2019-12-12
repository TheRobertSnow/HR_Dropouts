from logic_layer import WorkerLL, AirplaneLL, FlightLL, FlightRouteLL, VoyageLL


# functions that UI layer calls --
class UIAPI:
    def __init__(self):
        self.workerLL = WorkerLL.WorkerLL()
        self.flightLL = FlightLL.FlightLL()
        self.airplaneLL = AirplaneLL.AirplaneLL()
        self.flightRouteLL = FlightRouteLL.FlightRouteLL()
        self.voyageLL = VoyageLL.VoyageLL()

    def get_airplanes(self):
        [print(instance) for instance in self.airplaneLL.get_airplane_list()]

    #
    # plane related
    #
    def createNewAirplane(self, airplaneList):
        """takes in airplaneList, and you return us the created instance"""
        returnString = self.airplaneLL.createNewAirplane(airplaneList)
        return returnString

    def viewCertainAirplane(self, airplaneReg):
        """we give you the airplaneReg and you return us the instance of that airplane"""
        returnData = self.airplaneLL.getCertainAirplane(airplaneReg)
        return returnData

    def viewAllAirplanes(self):
        """give us all airplane instances, would be nice if we can get 5 at a time or something instead of all at once"""
        returnData = self.airplaneLL.getAllAirplanes()
        return returnData

    def updateAirplaneStatus(self, airplaneReg, newStatus):
        """takes in airplaneReg and newStatus and you have to change the status of that airplane and return the airplane object"""
        returnData = self.airplaneLL.updateAirplaneStatus(airplaneReg, newStatus)
        return returnData

    #
    # worker related
    #
    def createNewWorker(self, workerList):
        """takes in workerList, but ID, Active and Available are not in this list so they have to be automatically filled by you guys"""
        returnData = self.workerLL.createNewWorker(workerList)
        return returnData

    def viewWorkerBySSn(self, ssn, pos = ""):
        """Finds an instance of a worker, can take position to check if that instance is of that position"""
        returnData = self.workerLL.findWorkerBySSN(ssn, pos)
        return returnData

    def viewWorkerByPOS(self, positionWeWantToPrint):
        """give us all workers that have a certain position"""
        returnData = self.workerLL.findWorkerByPOS(positionWeWantToPrint)
        return returnData


    def viewAllWorkers(self):
        """give us all worker instances, would be nice if we can get 5 at a time or something instead of all at once"""
        returnData = self.workerLL.viewAllWorkers()
        for instance in returnData:
            print(str(instance) + "\n")
        returnstring = "\n"
        return returnstring

    def updateWorker(self, socialSecurityNumber, akey, newValue):
        """we give you a ssn, the key we want to change and the new value of that key, give us back the worker changed"""
        returnData = self.workerLL.updateWorker(socialSecurityNumber, akey, newValue)
        return returnData

    def listAvailableWorkersbydate(self, date, pos = ""):
        """We give you a date and you return to us all workers who are not active and available on that date.
        Can also take in position to filter staff type we want to return"""
        returnData = self.workerLL.listAvailableWorkersbydate(date, pos)
        return returnData

    def listUnavailableWorkersbydate(self, date, pos = ""):
        """We give you a date and you return to us all workers who are active on that date.
        Can also take in position to filter staff type we want to return"""
        returnData = self.workerLL.listUnavailableWorkersbydate(date, pos)
        return returnData

    def viewallVoyagesInWeek(self, week, pos):
        """We give you a week and position, either "Pilot" or "Attendant" and you return all
        voyages of that pilot or attendant in a given week. If the """
        pass

    #
    # flight related
    #

    def createNewFlight(self, flightList):
        """flightList is only Airplane reg, Origin ID, Destination ID and Departure time, all other info must be generated by you guys"""
        returnData = self.flightLL.createNewFlight(flightList)
        return returnData

    def viewCertainFlight(self, flightNumber, flightDate):
        """we give you a flightnumber and you need to return a error if it does not exist, otherwise you return the instance"""
        returnData = self.flightLL.getCertainflight(flightNumber, flightDate)
        return returnData

    def viewAllFlights(self):
        """give us all flight instances, would be nice if we can get 5 at a time or something instead of all at once"""
        returnData = self.flightLL.getAllFlights()
        return returnData

    def viewFlightsByStatus(self, status):
        """give us all flight instances that dont have a certain status"""
        returnData = self.flightLL.viewFlightsByStatus(status)
        return returnData

    def updateFlightStatus(self, flightlist):
        """we give you a new status of a certain flight and you update the instance and the csv file according to that"""
        returnData = self.flightLL.updateFlightStatus(flightlist)
        return returnData

    def updateFlightDepartureTime(self, newDepartureTime):
        """we give you a new departure time and you update the instance and the csv file according to that"""
        returnData = self.flightLL.updateFlightDepartureTime(newDepartureTime)
        return returnData
    #
    # voyage related
    #
    def createNewVoyage(self, dataList):
        return self.voyageLL.createNewVoyage(dataList)

    def viewVoyage(self, voyageID):
        """Uses voyageID to view a certain voyage"""
        returnData = self.flightRouteLL.viewFlightRoute(voyageID)
        return returnData

    def viewallVoyages(self):
        returnData = self.voyageLL.viewallVoyages()
        return returnData

    def viewallVoyagesDay(self, day):
        """Listar öll voyages á ákveðnum degi og hvort að þau séu fullmönnuð, svo
        við þurfum að fá lista eða dict með hverju voyage tilviki og svo upplýsingum
        um hvort að það sé fullmannað á þeim degi"""
        returnData = self.voyageLL.viewallVoyagesDay(day)
        return returnData

    def viewallVoyagesWeek(self, week):
        """Listar öll voyages í ákveðinni viku og hvort að þau séu fullmönnuð, svo
        við þurfum að fá lista eða dict með hverju voyage tilviki og svo upplýsingum
        um hvort að það sé fullmannað í þeirri viku"""
        returnData = self.voyageLL.viewallVoyagesWeek(week)
        return returnData

    def copyPreviousVoyage(self, voyageID):
        """afrita skráningu á vinnuferð fyrir sama áfangastað og tíma yfir á marga daga sem gerast með reglulegu millibili"""
        #returnData = self.voyageLL.copyPreviousVoyage(self, voyagedID)
        # TODO
        pass

    def requestVoyagePilots(self, voyageID):
        """asks to be returned the instances of pilots related to the ID i send"""
        return self.voyageLL.requestPilots(voyageID)

    def addPilotVoyage(self, voyageID, pilotToAddInput):
        """requests to add a new pilot to in the voyageID sent, return the updated Voyage instance"""
        # TODO
        pass

    def removePilotVoyage(self, voyageID, pilotToRemoveInput):
        """requests to remove a pilot from a Voyage, return the updated voyage instance"""
        # TODO
        pass

    def requestVoyageCrew(self, voyageID):
        """requests to be returned all instances of crew members on a specific voyageID"""
        # TODO
        pass

    def addCrewVoyage(self, voyageID, crewToAddInput):
        """requests to add a new crew member in the voyageID, returns the updated voyage instance"""
        # TODO
        pass

    def removeCrewVoyage(self, voyageID, crewToRemoveInput):
        """requests to remove crew member"""
        # TODO
        pass

    def requestFromIceFlightNumb(self, voyageID):
        """requests to be returned the flight Number that departures from Iceland"""
        # TODO
        pass

    def requestToIceFlightNumb(self, voyageID):
        """requests to be returned the flight number that departs TO iceland"""
        # TODO
        pass

    def cancelVoyage(self, voyageID):
        """requests to cancel a voyage with the given ID, returns the result"""
        # TODO
        pass

    def checkVoyageExists(self, voyageID):
        return self.voyageLL.checkVoyageExists(voyageID)

    def createDuplicateVoyages(self, argumentList):
        return self.voyageLL.createDuplicateVoyages(argumentList)

    #
    # flight route related
    #

    def createNewFlightRoute(self, flightRouteList):
        """Takes in list with flight route ID, country, airport, flight distance, travel time, emergecy contact and emergency number and creates Flight Route """
        returnData = self.flightRouteLL.createNewFlightRoute(flightRouteList)
        return returnData

    def updateFlightRoute(self, flightRouteList):
        """Uses flightRouteID to find the instance and uses the key to update the instance with a new value"""
        returnData = self.flightRouteLL.updateFlightRoute(flightRouteList)
        return returnData

    def viewFlightRoute(self, flightRouteID):
        """Uses flightRouteID to view a certain flightRouteID"""
        returnData = self.flightRouteLL.find_flight_route_by_id(flightRouteID)
        return returnData

    def viewAllFlightRoutes(self):
        """Prints all FLight Routes"""
        returnData = self.flightRouteLL.getAllFlightRoutes()
        return returnData

    def viewAllDestinations(self):
        """Listar öll destinations, viljum fá lista eða dict með "Country: Airport", ef það meikar sens"""
        pass

    def viewCertainFlightRoute(self, flightRouteID):
        """ TODO i need to be returned the flight route instance, if it doesn't exist return a the string 'Flight route doesn't exist'"""
        pass


# ++++++++++ Test Case ++++++++++
# UIAPI = UIAPI()
# UIAPI.get_airplanes()

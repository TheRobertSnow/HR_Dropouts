import IOAPI
from datetime import datetime
from logic_layer import FlightLL

class VoyageLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()
        self.voyage = self.IOAPI.request_voyages()
        self.flightLL = FlightLL.FlightLL()

    def get_voyage_list(self):
        return self.IOAPI.request_voyages()

    def createNewVoyage(self, dataList):
        return self.IOAPI.createNewVoyage(dataList)

    def find_voyage_by_ID(self, id):
        for instance in self.voyage:
            if instance.voyageID == id:
                return instance

    def checkVoyageExists(self, voyageID):
        voyageExists = False
        voyageList = self.get_voyage_list()
        for voyage in voyageList:
            if int(voyage.voyageID) == int(voyageID):
                voyageExists = True
        return voyageExists

    def createDuplicateVoyages(self, argumentList):
        """Method that creates duplicate voyages.
        argumentList = [voyageID, list_of_dates]"""
        desiredVoyage, flightOut, flightBack, voyageDict = None, None, None, None
        for voyage in self.voyage:
            if voyage.voyageID == argumentList[0]:
                desiredVoyage = voyage
        flights = self.IOAPI.getAllFlightInstances()
        for flight in flights:
            if flight.flightID == desiredVoyage.flightOutID:
                flightOut = flight
            elif flight.flightID == desiredVoyage.flightBackID:
                flightBack = flight
        for date in argumentList[1]:
            flightOutList = []
            flightOutList.append(flightOut.airplaneRegistrationNumber)
            flightOutList.append(flightOut.originID)
            flightOutList.append(flightOut.destinationID)
            oldDate, time = flightOut.departureTime.split()
            timeList = time.split(":")
            newDepartureTime = datetime(int(date.year), int(date.month), int(date.day), int(timeList[0]), int(timeList[1]), int(timeList[2]))
            # newNewDepartureTime = newDepartureTime.__str__()
            flightOutList.append(newDepartureTime)
            flightOutInstance = self.flightLL.createNewFlight(flightOutList)

            flightBackList = []
            flightBackList.append(flightBack.airplaneRegistrationNumber)
            flightBackList.append(flightBack.originID)
            flightBackList.append(flightBack.destinationID)
            oldDate, time = flightBack.departureTime.split()
            timeList = time.split(":")
            newDepartureTime = datetime(int(date.year), int(date.month), int(date.day), int(timeList[0]), int(timeList[1]), int(timeList[2]))
            flightBackList.append(newDepartureTime)
            flightBackInstance = self.flightLL.createNewFlight(flightBackList)

            voyageList = []
            voyageList.append(flightOutInstance.flightID)
            voyageList.append(flightBackInstance.flightID)
            voyageList.append(desiredVoyage.mainPilot)
            voyageList.append(desiredVoyage.assistingPilot)
            voyageList.append(desiredVoyage.mainFlightAttendant)
            voyageList.append(desiredVoyage.flightAttendants)
            # voyageList.append(desiredVoyage.flightRouteID)
            # voyageList.append(flightOutInstance.departureTime)
            # voyageList.append(flightBackInstance.departureTime)
            print("Voyage list before creating voyage: ",voyageList)
            voyageDict = self.createNewVoyage(voyageList)
        return "Succesfully created all voyages"



    def create_empty_voyage(self):
        """creates a empty voyage from 2 flights"""
        pass

    def requestPilots(self, voyageID):
        """returns pilots related to the voyage ID you send."""
        pass


    def viewallVoyagesDay(self, day):
        voyages = self.IOAPI.request_voyages()
        returnString = ""
        mannedString = ""
        print("")
        for voyage in voyages:
            departureFromIS = datetime.strptime(voyage.departureFromIS, '%Y-%m-%d %H:%M:%S')
            departureToIS = datetime.strptime(voyage.departureToIS, '%Y-%m-%d %H:%M:%S')
            mannedString = ""
            if day.date() == departureFromIS.date() or day.date() == departureToIS.date():
                manned = 0
                if len(voyage.mainPilot) != 0:
                    manned += 1
                if len(voyage.assistingPilot) != 0:
                    manned += 1
                if len(voyage.mainFlightAttendant) != 0:
                    manned += 1
                if manned >= 3:
                    mannedString = " is sufficently manned!"
                elif manned < 3:
                    mannedString = " is not sufficently manned!"
                returnString += ("Voyage with ID " + str(voyage.voyageID) + " flying from Iceland " + str(departureFromIS) + " and back " + str(departureToIS) + str(mannedString) + "\n")
        if len(returnString) == 0:
            returnString = "No voyages found on that date!\n"  
        return returnString


    def viewallVoyagesWeek(self, year, week):
        weekdays = []
        voyages = self.IOAPI.request_voyages()
        returnString = "Voyages in week {}\n--------------------------------------------\n".format(week)
        mannedString = ""
        day = "{}-W{}".format(year, week)
        firstWeekday = datetime.strptime(day + '-1', "%Y-W%W-%w")
        for i in range(7):
            weekdays.append(firstWeekday + timedelta(days = i))
        print("")
        for voyage in voyages:
            departureFromIS = datetime.strptime(voyage.departureFromIS, '%Y-%m-%d %H:%M:%S')
            departureToIS = datetime.strptime(voyage.departureToIS, '%Y-%m-%d %H:%M:%S')
            for days in weekdays:
                mannedString = ""
                manned = 0
                if days.date() == departureFromIS.date() or days.date() == departureToIS.date():
                    if len(voyage.mainPilot) != 0:
                        manned += 1
                    if len (voyage.assistingPilot) != 0:
                        manned += 1
                    if len (voyage.mainFlightAttendant) != 0:
                        manned += 1
                    if manned >= 3:
                        mannedString = " is sufficently manned!"
                    elif manned < 3:
                        mannedString = " is not sufficently manned!"
                    returnString += ("Voyage with ID " + str(voyage.voyageID) + " flying from Iceland " + str(departureFromIS) + " and back " +str(departureToIS) + str(mannedString) + "\n")
        if len(returnString) == 0:
            returnString = "There were no voyages found in this week!\n" 
        return returnString

            

    def listWorkerVoyagesByWeek(self, ssn, year, week, pos): 
        weekdays = []
        day = "{}-W{}".format(year, week)
        firstWeekday = datetime.strptime(day + '-1', "%Y-W%W-%w")
        for i in range(7):
            weekdays.append(firstWeekday + timedelta(days = i))
        destinationNameList = []
        string = ""
        workerInfo = ""
        workerList = WorkerLL.get_worker_list(self) #All workers
        voyageList = self.IOAPI.request_voyages() #All voyages
        flightRouteList = self.IOAPI.getAllFlightRouteInstances()         
        for voyage in voyageList:
            departureFromIS = datetime.strptime(voyage.departureFromIS, '%Y-%m-%d %H:%M:%S')
            departureToIS = datetime.strptime(voyage.departureToIS, '%Y-%m-%d %H:%M:%S')
            destinationID = voyage.flightRouteID
            for flightroute in flightRouteList:
                if flightroute.flightRouteID == destinationID:
                    destinationNameList.append(flightroute.country)
            if departureFromIS.date() in [i.date() for i in weekdays] or departureToIS.date() in [i.date() for i in weekdays]:
                for worker in workerList:
                    if worker.socialSecurityNumber == ssn:
                        workerInfo = "\n{:10s} | {}".format(worker.socialSecurityNumber,worker.name)
                    if pos == "Pilot":
                        if worker.position == "Captain":
                            if worker.socialSecurityNumber == voyage.mainPilot:
                                if worker.socialSecurityNumber == ssn:
                                    print(ssn)
                        elif worker.position == "Copilot":
                            if worker.socialSecurityNumber == voyage.assistingPilot:
                                if worker.socialSecurityNumber == ssn:
                                    print(ssn)
                    elif pos == "Attendant":
                        if worker.position == "Flight Service Manager":
                            if worker.socialSecurityNumber == voyage.mainFlightAttendant:
                                if worker.socialSecurityNumber == ssn:
                                    string += "\n{} | {} | {}".format(departureFromIS, departureToIS, destinationNameList[int(destinationID)])
                        elif worker.position == "Flight Attendant":
                            for i in voyage.getflightAttendants():
                                if i == worker.socialSecurityNumber:
                                    if worker.socialSecurityNumber == ssn:
                                        string += "\n{} | {} | {}".format(departureFromIS, departureToIS, destinationNameList[int(destinationID)])
        print(workerInfo, string)
        return "HALLO"
        
        
            


    def viewallVoyages(self):
        return self.IOAPI.request_voyages()

    def viewVoyage(self, voyageID):
        """takes in the instance and a voyageID you wish to find, returns the instance with that ID if it exists"""
        print(len(self.voyage))
        self.voyage = self.IOAPI.request_voyages()
        print(len(self.voyage))
        for instance in self.voyage:
            if str(instance.voyageID) == str(voyageID):
                return instance
        return "Voyage with that ID doesnt exist"

    def addCaptainToVoyage(self, voyageID, pilotToAddInput):
        """adds a pilot to a voyage, required the ID of the voyage and the SSN of the worker to add"""
        # verifying the pilot exists and is actually a captain
        doesntExist = True
        workerList = self.IOAPI.request_workers()
        planeLicence = ""
        for worker in workerList:
            if worker.socialSecurityNumber == pilotToAddInput:
                doesntExist = False
                if worker.position != "Captain":
                    return "Error! that worker doesn't have the correct position."
                planeLicence = str(worker.planeLicence)
        if doesntExist:
            return "Error! we couldn't find any worker with that SSN."

        # verify that the pilot is available
        voyageList = self.IOAPI.request_voyages()
        # get the current date
        date = ""
        instance = ""
        for i in voyageList:
            if str(i.voyageID) == str(voyageID):
                date = i.departureFromIS
                instance = i
        date = date.split(" ")[0]
        # check if the dates overlap for the same pilot
        flightID = ""
        for i in voyageList:
            dateCompare = i.departureFromIS
            dateCompare = dateCompare.split(" ")[0]
            if dateCompare == date:
                if i.mainPilot == pilotToAddInput:  # check if already booked
                    return "Error! that pilot is booked for that day."
                if i.voyageID == voyageID:
                    flightID = i.flightOutID
        if type(instance) == str:
            return "Voyage was not found"
        # verify plane licence
        requiredLicence = ""
        planeReg = ""
        flightList = self.IOAPI.getAllFlightInstances()
        for i in flightList:
            if i.flightID == flightID:
                planeReg = i.airplaneRegistrationNumber
        planeList = self.IOAPI.request_airplanes()
        for i in planeList:
            if i.planeRegistration == planeReg:
                requiredLicence = str(i.manufacturer) + str(i.model)
        if requiredLicence != planeLicence:
            return "Error! pilot does not have the required licence"
        # request to update the file and instance.
        return self.IOAPI.updateVoyage(instance, "Main pilot", pilotToAddInput)

    def addCopilotToVoyage(self, voyageID, pilotToAddInput):
        """adds a pilot to a voyage, required the ID of the voyage and the SSN of the worker to add"""
        # verifying the pilot exists and is actually a co pilot
        doesntExist = True
        workerList = self.IOAPI.request_workers()
        planeLicence = ""
        for worker in workerList:
            if worker.socialSecurityNumber == pilotToAddInput:
                doesntExist = False
                if worker.position != "Copilot":
                    return "Error! that worker doesn't have the correct position."
                planeLicence = str(worker.planeLicence)
        if doesntExist:
            return "Error! we couldn't find any worker with that SSN."

        # verify that the pilot is available
        voyageList = self.IOAPI.request_voyages()
        # get the current date
        date = ""
        instance = ""
        for i in voyageList:
            if str(i.voyageID) == str(voyageID):
                date = i.departureFromIS
                instance = i
        date = date.split(" ")[0]
        # check if the dates overlap for the same pilot
        flightID = ""
        for i in voyageList:
            dateCompare = i.departureFromIS
            dateCompare = dateCompare.split(" ")[0]
            if dateCompare == date:
                if i.assistingPilot == pilotToAddInput:  # check if already booked
                    return "Error! that pilot is booked for that day."
            if i.voyageID == voyageID:
                flightID = i.flightOutID
        if type(instance) == str:
            return "Voyage was not found"
        # verify plane licence
        requiredLicence = ""
        planeReg = ""
        flightList = self.IOAPI.getAllFlightInstances()
        for i in flightList:
            if i.flightID == flightID:
                planeReg = i.airplaneRegistrationNumber
        planeList = self.IOAPI.request_airplanes()
        for i in planeList:
            if i.planeRegistration == planeReg:
                requiredLicence = str(i.manufacturer) + str(i.model)
        if requiredLicence != planeLicence:
            return "Error! pilot does not have the required licence"
        # request to update the file and instance.
        return self.IOAPI.updateVoyage(instance, "Assisting pilot", pilotToAddInput)

    def addMainFlightAttendantToVoyage(self, voyageID, pilotToAddInput):
        """adds a pilot to a voyage, required the ID of the voyage and the SSN of the worker to add"""
        # verifying the pilot exists and is actually a co pilot
        doesntExist = True
        workerList = self.IOAPI.request_workers()
        for worker in workerList:
            if worker.socialSecurityNumber == pilotToAddInput:
                doesntExist = False
                if worker.position != "Flight Service Manager":
                    return "Error! that worker doesn't have the correct position."
        if doesntExist:
            return "Error! we couldn't find any worker with that SSN."

        # verify that the pilot is available
        voyageList = self.IOAPI.request_voyages()
        # get the current date
        date = ""
        instance = ""
        for i in voyageList:
            if str(i.voyageID) == str(voyageID):
                date = i.departureFromIS
                instance = i
        date = date.split(" ")[0]
        # check if the dates overlap for the same pilot
        for i in voyageList:
            dateCompare = i.departureFromIS
            dateCompare = dateCompare.split(" ")[0]
            if dateCompare == date:
                if i.mainFlightAttendant == pilotToAddInput:  # check if already main pilot
                    return "Error! that Main Flight attendant is booked for that day."
        if type(instance) == str:
            return "Voyage was not found"
        # request to update the file and instance.
        return self.IOAPI.updateVoyage(instance, "Main flight attendant", pilotToAddInput)

    def addFlightAttendantToVoyage(self, voyageID, pilotToAddInput):
        """adds a pilot to a voyage, required the ID of the voyage and the SSN of the worker to add"""
        # verifying the pilot exists and is actually a co pilot
        doesntExist = True
        workerList = self.IOAPI.request_workers()
        for worker in workerList:
            if worker.socialSecurityNumber == pilotToAddInput:
                doesntExist = False
                if worker.position != "Flight Attendant":
                    return "Error! that worker doesn't have the correct position."
        if doesntExist:
            return "Error! we couldn't find any worker with that SSN."

        # verify that the pilot is available
        voyageList = self.IOAPI.request_voyages()
        # get the current date
        date = ""
        instance = ""
        for i in voyageList:
            if str(i.voyageID) == str(voyageID):
                date = i.departureFromIS
                instance = i
        date = date.split(" ")[0]
        # check if the dates overlap for the same pilot
        for i in voyageList:
            dateCompare = i.departureFromIS
            dateCompare = dateCompare.split(" ")[0]
            if dateCompare == date:
                flightAttendantList = i.flightAttendants
                try:
                    flightAttendantList = flightAttendantList.split("/")
                except ValueError:
                    pass
                if pilotToAddInput in flightAttendantList:  # check if already main pilot
                    return "Error! that flight attendant is booked for that day."
        if type(instance) == str:
            return "Voyage was not found"
        # request to update the file and instance.
        return self.IOAPI.updateVoyage(instance, "Flight attendants", pilotToAddInput)

    def checkIfIdUsed(self, flightID):
        voyageList = self.IOAPI.request_voyages()
        for voyage in voyageList:
            if voyage.flightBackID == flightID:
                return True
            elif voyage.flightOutID == flightID:
                return True
        return False

    def verifyStaff(self, theKey, SSN, dateOut, dateBack, flightID):
        """checks if a worker is eligible for the voyage you are trying to add him to, returns a string with
            a error message if it doesnt, otherwise we return None"""
        # check if staff member has the correct position
        doesntExist = True
        planeLicence = ""  # for checking plane licence
        workerList = self.IOAPI.request_workers()
        for worker in workerList:
            if worker.socialSecurityNumber == SSN:
                doesntExist = False
                if str(worker.position) != str(theKey):
                    return "Error! that worker doesn't have the correct position."
                planeLicence = worker.planeLicence
        if doesntExist:
            return "Error! we couldn't find any worker with that SSN."
        # check if the staff member is already booked for those days
        voyageList = self.IOAPI.request_voyages()
        # check if the dates overlap for the same pilot
        for i in voyageList:
            dateCompare = i.departureFromIS
            dateCompare = dateCompare.split(" ")[0]
            if dateCompare == dateOut or dateCompare == dateBack:
                if theKey == "Captain":
                    if i.mainPilot == SSN:  # check if already booked
                        return "Error! that pilot is booked for that day."
                elif theKey == "Copilot":
                    if i.assistingPilot == SSN:  # check if already booked
                        return "Error! that pilot is booked for that day."
                elif theKey == "Flight Service Manager":
                    if i.mainFlightAttendant == SSN:  # check if already main pilot
                        return "Error! that Flight Service Manager is booked for that day."
                elif theKey == "Flight Attendant":
                    flightAttendantList = i.flightAttendants
                    try:
                        flightAttendantList = flightAttendantList.split("/")
                    except ValueError:
                        pass
                    if SSN in flightAttendantList:  # check if already main pilot
                        return "Error! that pilot is booked for that day."
        if theKey == "Captain" or theKey == "Copilot": # checking plane licence
            flightList = self.IOAPI.getAllFlightInstances()
            requiredLicence = ""
            planeReg = ""
            # get the plane reg
            for i in flightList:
                if i.flightOutID == flightID:
                    planeReg = i.planeRegistration
            # get the plane licence required
            planeList = self.IOAPI.request_airplanes()
            for i in planeList:
                if planeReg == i.planeRegistration:
                    requiredLicence = str(i.manufacturer) + str(i.model)
            if requiredLicence != planeLicence:
                return "Error! pilot doesn't have the required licence"
        return None

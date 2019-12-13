import IOAPI
from datetime import datetime
from datetime import timedelta
from logic_layer import FlightLL

class VoyageLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()
        self.voyage = self.IOAPI.request_voyages()
        self.flightLL = FlightLL.FlightLL()

    def get_voyage_list(self):
        """gets voyage in the form of a list"""
        return self.IOAPI.request_voyages()

    def createNewVoyage(self, dataList):
        """creates new voyage by sending a list with information on the new voyage"""
        return self.IOAPI.createNewVoyage(dataList)

    def find_voyage_by_ID(self, id):
        """searches for voyage with id"""
        for instance in self.voyage:
            if instance.voyageID == id:
                return instance

    def checkVoyageExists(self, voyageID):
        """tries to find voyage by sending id"""
        voyageExists = False
        voyageList = self.get_voyage_list()
        for voyage in voyageList:
            if int(voyage.voyageID) == int(voyageID):
                voyageExists = True
        return voyageExists

    def createDuplicateVoyages(self, argumentList):
        """Method that creates duplicate voyages.
        argumentList = [voyageID, list_of_dates]"""
        self.voyage = self.IOAPI.request_voyages()
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
            voyageDict = self.createNewVoyage(voyageList)
        return "Succesfully created all voyages"

    def viewallVoyagesDay(self, day):
        """views all voyages on a particular day"""
        voyages = self.IOAPI.request_voyages()
        printString = "\nVoyages on day {}\n".format(day)
        printString += "\n{:3s} | {}  | {} | {} | {}\n".format("ID", "ORIGIN", "DEPARTURE TIME FROM IS", "DEPARTURE TIME TO IS", "SUFFICIENTLY MANNED")
        printString += "-" * 83 + "\n"
        returnString = ""
        mannedString = ""
        for voyage in voyages:
            if type(voyage.departureFromIS) == str:
                departureFromIS = datetime.strptime(voyage.departureFromIS, '%Y-%m-%d %H:%M:%S')
            else:
                departureFromIS = voyage.departureFromIS
            if type(voyage.departureToIS) == str:
                departureToIS = datetime.strptime(voyage.departureToIS, '%Y-%m-%d %H:%M:%S')
            else:
                departureToIS = voyage.departureToIS
            if day.date() == departureFromIS.date() or day.date() == departureToIS.date():
                manned = 0
                if len(voyage.mainPilot) != 0:
                    manned += 1
                if len(voyage.assistingPilot) != 0:
                    manned += 1
                if len(voyage.mainFlightAttendant) != 0:
                    manned += 1
                if manned >= 3:
                    mannedString = "YES"
                elif manned < 3:
                    mannedString = "NO"
                returnString += "{:3s} | {} | {}    | {}  | {}\n".format(voyage.voyageID, "Iceland", departureFromIS, departureToIS, mannedString)
        if len(returnString) == 0:
            return "\nNo voyages found on that date!\n"  
        else:
            return printString + returnString

    def viewallVoyagesWeek(self, year, week):
        """views all voyages in a particular week of a year"""
        weekdays = []
        voyages = self.IOAPI.request_voyages()
        printString = "\nVoyages in week {}\n".format(week)
        printString += "\n{:3s} | {}  | {} | {} | {}\n".format("ID", "ORIGIN", "DEPARTURE TIME FROM IS", "DEPARTURE TIME TO IS", "SUFFICIENTLY MANNED")
        printString += "-" * 83 + "\n"
        returnString = ""
        mannedString = ""
        day = "{}-W{}".format(year, week)
        firstWeekday = datetime.strptime(day + '-1', "%Y-W%W-%w")
        for i in range(7):
            weekdays.append(firstWeekday + timedelta(days = i))
        for voyage in voyages:
            if type(voyage.departureFromIS) == str:
                departureFromIS = datetime.strptime(voyage.departureFromIS, '%Y-%m-%d %H:%M:%S')
            else:
                departureFromIS = voyage.departureFromIS
            if type(voyage.departureToIS) == str:
                departureToIS = datetime.strptime(voyage.departureToIS, '%Y-%m-%d %H:%M:%S')
            else:
                departureToIS = voyage.departureToIS
            for days in weekdays:
                manned = 0
                if days.date() == departureFromIS.date() or days.date() == departureToIS.date():
                    if len(voyage.mainPilot) != 0:
                        manned += 1
                    if len (voyage.assistingPilot) != 0:
                        manned += 1
                    if len (voyage.mainFlightAttendant) != 0:
                        manned += 1
                    if manned >= 3:
                        mannedString = "YES"
                    elif manned < 3:
                        mannedString = "NO"
                    returnString += "{:3s} | {} | {}    | {}  | {}\n".format(voyage.voyageID, "Iceland", departureFromIS, departureToIS, mannedString)
        if len(returnString) == 0:
            return "\nThere were no voyages found in this week!\n" 
        else:
            return printString + returnString
        
    def viewallVoyages(self):
        """ views all voyages """
        return self.IOAPI.request_voyages()

    def viewVoyage(self, voyageID):
        """takes in the instance and a voyageID you wish to find, returns the instance with that ID if it exists"""
        #print(len(self.voyage))
        self.voyage = self.IOAPI.request_voyages()
        #print(len(self.voyage))
        for instance in self.voyage:
            if str(instance.voyageID) == str(voyageID):
                return instance
        return "\nVoyage with that ID doesnt exist\n"

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
                    return "\nError! That worker doesn't have the correct position.\n"
                planeLicence = str(worker.planeLicence)
        if doesntExist:
            return "\nError! we couldn't find any worker with that SSN.\n"
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
                    return "\nError! that pilot is booked for that day.\n"
                if i.voyageID == voyageID:
                    flightID = i.flightOutID
        if type(instance) == str:
            return "\nVoyage was not found\n"
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
            return "\nError! pilot does not have the required licence\n"
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
                    return "\nError! that worker doesn't have the correct position.\n"
                planeLicence = str(worker.planeLicence)
        if doesntExist:
            return "\nError! we couldn't find any worker with that SSN.\n"
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
                    return "\nError! that pilot is booked for that day.\n"
            if i.voyageID == voyageID:
                flightID = i.flightOutID
        if type(instance) == str:
            return "\nVoyage was not found\n"
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
            return "\nError! pilot does not have the required licence\n"
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
                    return "\nError! that worker doesn't have the correct position.\n"
        if doesntExist:
            return "\nError! we couldn't find any worker with that SSN.\n"
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
                    return "\nError! that Main Flight attendant is booked for that day.\n"
        if type(instance) == str:
            return "\nVoyage was not found\n"
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
                    return "\nError! that worker doesn't have the correct position.\n"
        if doesntExist:
            return "\nError! we couldn't find any worker with that SSN.\n"
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
                    return "\nError! that flight attendant is booked for that day.\n"
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
                    return "\nError! that worker doesn't have the correct position.\n"
                planeLicence = worker.planeLicence
        if doesntExist:
            return "\nError! we couldn't find any worker with that SSN.\n"
        # check if the staff member is already booked for those days
        voyageList = self.IOAPI.request_voyages()
        # check if the dates overlap for the same pilot
        for i in voyageList:
            dateCompare = i.departureFromIS
            dateCompare = dateCompare.split(" ")[0]
            if dateCompare == dateOut or dateCompare == dateBack:
                if theKey == "Captain":
                    if i.mainPilot == SSN:  # check if already booked
                        return "\nError! that pilot is booked for that day.\n"
                elif theKey == "Copilot":
                    if i.assistingPilot == SSN:  # check if already booked
                        return "\nError! that pilot is booked for that day.\n"
                elif theKey == "Flight Service Manager":
                    if i.mainFlightAttendant == SSN:  # check if already main pilot
                        return "\nError! that Flight Service Manager is booked for that day.\n"
                elif theKey == "Flight Attendant":
                    flightAttendantList = i.flightAttendants
                    try:
                        flightAttendantList = flightAttendantList.split("/")
                    except ValueError:
                        pass
                    if SSN in flightAttendantList:  # check if already main pilot
                        return "\nError! that pilot is booked for that day.\n"
        if theKey == "Captain" or theKey == "Copilot": # checking plane licence
            flightList = self.IOAPI.getAllFlightInstances()
            requiredLicence = ""
            planeReg = ""
            # get the plane reg
            for i in flightList:
                if i.flightID == flightID:
                    planeReg = i.planeRegistration
            # get the plane licence required
            planeList = self.IOAPI.request_airplanes()
            for i in planeList:
                if planeReg == i.planeRegistration:
                    requiredLicence = str(i.manufacturer) + str(i.model)
            if requiredLicence != planeLicence:
                return "\nError! pilot doesn't have the required licence\n"
        return None

import sys
sys.path.append('..')
import IOAPI
from datetime import datetime
from datetime import timedelta

class WorkerLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()

    def get_worker_list(self):
        self.worker = self.IOAPI.request_workers()
        return self.worker

    def checkSSN(self, ssn):
        """Takes in a social security and checks if it is of the right length and the correct format.
        It then returns the ssn if it is correct and an error if it is not."""
        if len(ssn) != 10:
            ssn = "\nThat social security number is not correct, try again!"

        try:
            intCheck = int(ssn)
        except ValueError:
            ssn = "\nThat social security number is not correct, try again!"
        return ssn

    def checkNewValue(self, theKey, newValue):
        testValue = ""
        validValue = ""
        error = ""
        if theKey == "Address":
            try:
                testValue = newValue.split(" ")
            except ValueError:
                validValue = False
                error = "Home address"
            try:
                testValue = int(testValue[1])
            except IndexError:
                validValue = False
                error = "Home address"
        if theKey == "Phone":
            try:
                testValue = int(newValue)
            except ValueError:
                validValue = False
                error = "Phone number"
        if theKey == "Cellphone":
            try:
                testValue = int(newValue)
            except ValueError:
                validValue = False
                error = "Cellphone number"
        if theKey == "Email":
            if "@" not in newValue:
                validValue = False
                error = "Email"
        return validValue, error

    def findWorkerBySSN(self, ssn, pos):
        """Takes social security number and position and returns an instance of a worker in that position
        with that ssn if it exists."""
        ssn = WorkerLL.checkSSN(self, ssn)
        if ssn != "\nThat social security number is not correct, try again!!":
            self.worker = self.IOAPI.request_workers()
            for instance in self.worker:
                if pos == "":
                    if instance.socialSecurityNumber == ssn:
                        return instance
                elif pos == "Pilot":
                    if instance.position == "Captain" or instance.position == "Copilot":
                        if instance.socialSecurityNumber == ssn:
                            return instance
                elif pos == "Attendant":
                    if instance.position == "Flight Attendant" or instance.position == "Flight Service Manager":
                        if instance.socialSecurityNumber == ssn:
                            return instance
                elif pos == "Manager":
                    if instance.position == "Staff manager" or instance.position == "Trip manager":
                        if instance.socialSecurityNumber == ssn:
                            return instance
        #if ssn != "\nSocial security numbers are shown above!":
            #ssn = "\n{} Social security numbers are shown above!\n".format(pos)
        return ssn

    def findWorkerByPOS(self, position):
        """Takes in a position and return a list of all workers in that position."""
        self.worker = self.IOAPI.request_workers()
        positionList = []
        if position == "Pilot":
            for instance in self.worker:
                if instance.position == "Captain" or instance.position == "Copilot":
                    positionList.append(instance)


        elif position == "Attendant":
            for instance in self.worker:
                if instance.position == "Flight Service Manager" or instance.position == "Flight Attendant":
                    positionList.append(instance)
        elif position == "Manager":
            for instance in self.worker:
                if instance.position == "Staff manager" or instance.position == "Trip manager":
                    positionList.append(instance)
        if len(positionList) == 0:
            positionList = "\nNo {}'s found!\n".format(position)
        return positionList

    def findWorkerByPlaneLicence(self, plane_Licence):
        """Takes in a plane license and returns a list with all Pilots with that specific license."""
        workerList = []
        worker = self.get_worker_list()
        for instance in worker:
            if instance.planeLicence == plane_Licence:
                workerList.append(instance)
        if len(workerList) == 0:
            print("No pilot has licence for {}".format(plane_Licence))
        return workerList

    def updateWorker(self, socialSecurityNumber, theKey, newValue):
        """Takes in a social security number, key and value, finds a worker instance and
        then uses key and value and to update the values of that worker instance if it exists.
        It then returns that instance (if it exists)"""
        ssn = WorkerLL.checkSSN(self, socialSecurityNumber)
        validValue = True
        error = ""
        if ssn != "\nThat social security number is not correct, try again!":
            validValue, error = self.checkNewValue(theKey, newValue)
        if validValue != False:
            self.worker = WorkerLL.get_worker_list(self)
            for instance in self.worker:
                if instance.socialSecurityNumber == socialSecurityNumber:
                    updatedWorker = self.IOAPI.updateWorker(instance, theKey, newValue)
                    self.worker = WorkerLL.get_worker_list(self)
                    print("Worker succesfully updated!\n")
                    return updatedWorker
        return "\n{} could not be updated, please try again!\n".format(error)

    def viewAllWorkers(self):
        """Returns all workers"""
        self.worker = self.IOAPI.request_workers()
        return self.worker

    def createNewWorker(self, createWorkerList):
        """Takes in a list of worker qualities and creates an instance of that worker and returns the worker"""
        createWorkerList.append("TRUE")
        createWorkerList.append("TRUE")
        #0 check social security number
        try:
            self.checkSSN(createWorkerList[0])
        except ValueError:
            return "\nError!: SSN should be a whole number!\n"
        #2 checking position

        if createWorkerList[2] == "Stupid User":
            return "\nError!: Position not picked\n"
        #5 Phone
        try:
            int(createWorkerList[5])
        except ValueError:
            return "\nError!: Phone number should be a numbers\n"
        #6 Cellphone
        try:
            int(createWorkerList[6])
        except ValueError:
            return "\nError!: Phone number should be a number\n"

        worker = self.IOAPI.createNewWorker(createWorkerList)
        return worker

    def listWorkersbydate(self, date, pos, status):
        """Takes in a position and a list of workers who are unavailable on that date from
        the "listUnavailableWorkersbydate" function"""
        dashString = "-"
        flightAttendantList = []
        newFlightAttendantList = []
        mainFlightAttendantList = []
        mainPilotList = []
        assistingPilotList = []
        destinationNameList = []
        avaialbleWorkerString = ""
        unAvaialbleWorkerString = ""
        workerList = WorkerLL.get_worker_list(self) #All workers
        voyages = self.IOAPI.request_voyages() #All voyages
        flightRoutes = self.IOAPI.getAllFlightRouteInstances()
        printString = "\n{} {}s on date: {}".format(status, pos, date.date())
        if status == "Available":
            printString += "\n\n{:^10s} | {:^20s} | {:^22s}\n".format("SSN", "NAME", "POSITION")
        elif status == "Unavailable":
            printString += "\n\n{:^10s} | {:^20s} | {:^22s}\n".format("SSN", "NAME", "FLIGHT DESTINATION")
        printString += dashString * 60
        for voyage in voyages:
            destinationID = voyage.flightRouteID
            departureFromIS = datetime.strptime(voyage.departureFromIS, '%Y-%m-%d %H:%M:%S')
            #departureToIS = datetime.strptime(voyage.departureToIS, '%Y-%m-%d %H:%M:%S')
            for flightroute in flightRoutes:
                if flightroute.flightRouteID == destinationID:
                    destinationNameList.append(flightroute.country)
            if date.date() == departureFromIS.date():
                mainPilotList.append(voyage.mainPilot)
                assistingPilotList.append(voyage.assistingPilot)
                mainFlightAttendantList.append(voyage.mainFlightAttendant)
                flightAttendantList = voyage.flightAttendants.split("/")
                newFlightAttendantList.append(flightAttendantList)

        for worker in workerList:
            if pos == "Pilot":
                if worker.position == "Captain" and worker.socialSecurityNumber not in mainPilotList:
                    avaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,worker.position)
                elif worker.position == "Captain" and worker.socialSecurityNumber in mainPilotList:
                    for i in range(len(mainPilotList)):
                        if mainPilotList[i] == worker.socialSecurityNumber:
                            unAvaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,destinationNameList[i])
                elif worker.position == "Copilot" and worker.socialSecurityNumber not in assistingPilotList:
                    avaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,worker.position)
                elif worker.position == "Copilot" and worker.socialSecurityNumber in assistingPilotList:
                    for i in range(len(assistingPilotList)):
                        if assistingPilotList[i] == worker.socialSecurityNumber:
                            unAvaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,destinationNameList[i])
            elif pos == "Attendant":
                if worker.position == "Flight Service Manager" and worker.socialSecurityNumber not in mainFlightAttendantList:
                    avaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,worker.position)
                elif worker.position == "Flight Service Manager" and worker.socialSecurityNumber in mainFlightAttendantList:
                    for i in range(len(mainFlightAttendantList)):
                        if mainFlightAttendantList[i] == worker.socialSecurityNumber:
                            unAvaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,destinationNameList[i])
                elif worker.position == "Flight Attendant" and worker.socialSecurityNumber not in [j for i in newFlightAttendantList for j in i]:
                    avaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,worker.position)
                elif worker.position == "Flight Attendant" and worker.socialSecurityNumber in [j for i in newFlightAttendantList for j in i]:
                    for i in range(len(newFlightAttendantList)):
                        if worker.socialSecurityNumber in newFlightAttendantList[i]:
                            unAvaialbleWorkerString += "\n{:10s} | {:20s} | {:22s}".format(worker.socialSecurityNumber,worker.name,destinationNameList[i])
        if status == "Unavailable":
            if len(unAvaialbleWorkerString) == 0:
                return "\nThere are no workers working on that date!\n"
            else:
                return printString + unAvaialbleWorkerString + "\n"
        elif status == "Available":
            if len(avaialbleWorkerString) == 0:
                return "\nAll workers seem to be unavailable at this date!\n"
            else:
                return printString + avaialbleWorkerString + "\n"

    def listWorkerVoyagesByWeek(self, ssn, year, week, pos):
        weekdays = []
        day = "{}-W{}".format(year, week)
        firstWeekday = datetime.strptime(day + '-1', "%Y-W%W-%w")
        for i in range(7):
            weekdays.append(firstWeekday + timedelta(days = i))
        destinationNameList = []
        workerVoyageString = ""
        workerInfo = ""
        workerList = WorkerLL.get_worker_list(self) #All workers
        voyageList = self.IOAPI.request_voyages() #All voyages
        flightRouteList = self.IOAPI.getAllFlightRouteInstances()
        for worker in workerList:
            if worker.socialSecurityNumber == ssn:
                workerInfo += "\nAll voyages of worker in week {} of year {}".format(week, year)
                workerInfo += "\nSSN: {:10s} | NAME: {}\n".format(worker.socialSecurityNumber,worker.name)
                workerInfo += "\n{} | {} | {}".format("DEPARTURE TIME FROM IS", "DEPARTURE TIME TO IS", "DESTINATION")
        for voyage in voyageList:
            departureFromIS = datetime.strptime(voyage.departureFromIS, '%Y-%m-%d %H:%M:%S')
            departureToIS = datetime.strptime(voyage.departureToIS, '%Y-%m-%d %H:%M:%S')
            destinationID = voyage.flightRouteID
            for flightroute in flightRouteList:
                if flightroute.flightRouteID == destinationID:
                    destinationNameList.append(flightroute.country)
            if departureFromIS.date() in [i.date() for i in weekdays] or departureToIS.date() in [i.date() for i in weekdays]:
                for worker in workerList:
                    if pos == "Pilot":
                        if worker.position == "Captain":
                            if worker.socialSecurityNumber == voyage.mainPilot:
                                if worker.socialSecurityNumber == ssn:
                                    workerVoyageString += "\n{}    | {}  | {}".format(departureFromIS, departureToIS, destinationNameList[int(destinationID)-1])
                        elif worker.position == "Copilot":
                            if worker.socialSecurityNumber == voyage.assistingPilot:
                                if worker.socialSecurityNumber == ssn:
                                    workerVoyageString += "\n{}    | {}  | {}".format(departureFromIS, departureToIS, destinationNameList[int(destinationID)-1])
                    elif pos == "Attendant":
                        if worker.position == "Flight Service Manager":
                            if worker.socialSecurityNumber == voyage.mainFlightAttendant:
                                if worker.socialSecurityNumber == ssn:
                                    workerVoyageString += "\n{}    | {}  | {}".format(departureFromIS, departureToIS, destinationNameList[int(destinationID)-1])
                        elif worker.position == "Flight Attendant":
                            flightAttendantList = voyage.flightAttendants.split("/")
                            for i in flightAttendantList:
                                if i == worker.socialSecurityNumber:
                                    if worker.socialSecurityNumber == ssn:
                                        workerVoyageString += "\n{}    | {}  | {}".format(departureFromIS, departureToIS, destinationNameList[int(destinationID)-1])
        if len(workerInfo) == 0:
            return "\nNo worker found with that id!\n"
        elif len(workerVoyageString) == 0:
            return "\nWorker with that id has no voyages on schedule!\n"
        else:
            return workerInfo + workerVoyageString + "\n"

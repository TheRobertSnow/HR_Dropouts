import sys
sys.path.append('..')
import IOAPI

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
        if theKey == "Address":
            try:
                testValue = newValue.split(" ")
            except ValueError:
                validValue = False
                error = "Home address"
            try:
                testValue = int(testValue[1])
            except ValueError:
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
            try:
                testValue = testValue.split('@')
            except ValueError:
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
        if ssn != "\nSocial security numbers are shown above!":
            ssn = "\n{} Social security numbers are shown above!\n".format(pos)
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
            positionList = "No {}'s found!.".format(position)
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
        return "{} could not be updated, please try again!".format(error)

    def viewAllWorkers(self):
        """Returns all workers"""
        self.worker = self.IOAPI.request_workers()
        return self.worker

    def createNewWorker(self, createWorkerList):
        """Takes in a list of worker qualities and creates an instance of that worker and retuns the worker"""
        createWorkerList.append("TRUE")
        createWorkerList.append("TRUE")
        #0 check social security number
        try:
            int(createWorkerList[0])
        except ValueError:
            return "Error!: SSN should be a whole number!"
        #2 checking position
        
        if createWorkerList[2] == "Stupid User":
            return "Error!: Position not picked"
        

        #5 Phone
        try:
            int(createWorkerList[5])
        except ValueError:
            return "Error!: Phone number should be a numbers"
        #6 Cellphone
        try:
            int(createWorkerList[6])
        except ValueError:
            return "Error!: Phone number should be a number"
        
        worker = self.IOAPI.createNewWorker(createWorkerList)
        return worker

    def listUnavailableWorkersbydate(self, date, pos): 
        """Takes in a date and position and returns a list with each worker who is working on that date
         and the worker's destination."""
        unavailableList = []
        destinationName = ""
        workerList = WorkerLL.get_worker_list(self) #All workers
        voyages = self.IOAPI.request_voyagestoWorker() #All voyages
        flightRoutes = self.IOAPI.getAllFlightRouteInstances() #All flight Routes
        for voyage in voyages:
            destinationID = voyage.flightRouteID 
            for flightroute in flightRoutes:
                if flightroute.flightRouteID == destinationID:
                    destinationName = flightroute.country
            if date in voyage.departureFromIS or date in voyage.departureToIS:
                for worker in workerList:
                    if pos == "Pilot":
                        if voyage.mainPilot == worker.socialSecurityNumber:
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append(str(worker.name) + " is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList)
                        elif voyage.assistingPilot == worker.socialSecurityNumber:
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append(str(worker.name) + " is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList)
                    elif pos == "Attendant":
                        if voyage.mainFlightAttendant == worker.socialSecurityNumber:
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append(str(worker.name) + " is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList) 
                        elif worker.socialSecurityNumber in voyage.getflightAttendants():
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append(str(worker.name) + " is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList) 
        if len(unavailableList) == 0:
            unavailableList = "There are no workers working on that date."
        return unavailableList

    def listAvailableWorkersbydate(self, pos, unavailableList):  
        """Takes in a position and a list of workers who are unavailable on that date from 
        the "listUnavailableWorkersbydate" function"""
        availableList = []
        workerList = WorkerLL.get_worker_list(self)
        voyages = self.IOAPI.request_voyagestoWorker()
        for instance in workerList:
            if pos == "Pilot":
                if instance.position == "Captain" or instance.position == "Copilot" and instance not in unavailableList:
                    availableList.append(instance)
            elif pos == "Attendant":
                if instance.position == "Flight Service Manager" or instance.position == "Flight Attendant" and instance not in unavailableList:
                    availableList.append(instance)
        return availableList

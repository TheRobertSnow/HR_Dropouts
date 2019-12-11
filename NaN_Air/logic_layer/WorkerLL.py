import sys
sys.path.append('..')
import IOAPI

class WorkerLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()

    def get_worker_list(self):
        self.worker = self.IOAPI.request_workers()
        return self.worker

    def findWorkerBySSN(self, ssn, pos):
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

        notFoundString = "{} not found!\n".format(pos)
        return notFoundString

    def findWorkerByPOS(self, position):
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
        workerList = []
        worker = self.get_worker_list()
        for instance in worker:
            if instance.planeLicence == plane_Licence:
                workerList.append(instance)
        if len(workerList) == 0:
            print("No pilot has licence for {}".format(plane_Licence))
        return workerList



    def updateWorker(self, socialSecurityNumber, theKey, newValue):
        print("LL worker")
        self.worker = WorkerLL.get_worker_list(self)
        for instance in self.worker:
            if instance.socialSecurityNumber == socialSecurityNumber:
                updatedWorker = self.IOAPI.updateWorker(instance, theKey, newValue)
                self.worker = WorkerLL.get_worker_list(self)
                print("Worker succesfully updated!\n")
                return updatedWorker
        return "Worker could not be updated"


    def viewAllWorkers(self):
        self.worker = self.IOAPI.request_workers()
        return self.worker

    def createNewWorker(self, createWorkerList):
        createWorkerList.append("TRUE")
        createWorkerList.append("TRUE")
        worker = self.IOAPI.createNewWorker(createWorkerList)
        return worker

    def listUnavailableWorkersbydate(self, date, pos): #Galli að ef að worker eru alltaf skráðir available, spurning
        #um að TAKA ACTIVE OG AVAILABLE ÚT ÞEGAR ER VERIÐ AÐ PRENTA WORKER INSTANCE????
        #BÆTA VIÐ TIL HVAÐA ÁFANGASTAÐAR ÞEIR ERU AÐ FARA!!!!!!
        unavailableList = []
        destinationName = ""
        workerList = WorkerLL.get_worker_list(self) #All workers
        voyages = self.IOAPI.request_voyagestoWorker() #All voyages
        flightRoutes = self.IOAPI.getAllFlightRouteInstances() #All flight Routes
        #flights = self.IOAPI.getAllFlightInstances()
        for voyage in voyages:
            destinationID = voyage.flightRouteID 
            for flightroute in flightRoutes:
                if flightroute.flightRouteID == destinationID:
                    destinationName = flightroute.country
                #Finna flight route id í flight route og skila flight route country
            if date in voyage.departureFromIS or date in voyage.departureToIS:
                for worker in workerList:
                    if pos == "Pilot":
                        if voyage.mainPilot == worker.socialSecurityNumber:
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append("Worker is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList) #Bæta við destinationName
                        elif voyage.assistingPilot == worker.socialSecurityNumber:
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append("Worker is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList) #Bæta við destinationName
                    elif pos == "Attendant":
                        if voyage.mainFlightAttendant == worker.socialSecurityNumber:
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append("Worker is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList) #Bæta við destinationName
                        elif worker.socialSecurityNumber in voyage.getflightAttendants():
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append("Worker is going to " + str(destinationName) + " on " + str(date) + "!")
                            unavailableList.append(toAddList) #Bæta við destinationName
        if len(unavailableList) == 0:
            unavailableList = "There are no workers working on that date."
        return unavailableList

    def listAvailableWorkersbydate(self, pos, unavailableList):  
        availableList = []
        workerList = WorkerLL.get_worker_list(self)
        voyages = self.IOAPI.request_voyagestoWorker()
        print(voyages)
        for instance in workerList:
            if pos == "Pilot":
                if instance.position == "Captain" or instance.position == "Copilot" and instance not in unavailableList:
                    availableList.append(instance)
            elif pos == "Attendant":
                if instance.position == "Flight Service Manager" or instance.position == "Flight Attendant" and instance not in unavailableList:
                    availableList.append(instance)
        return availableList

        """def listUnavailableWorkersbydate(self, date, pos): #Galli að ef að worker eru alltaf skráðir available, spurning
        #um að TAKA ACTIVE OG AVAILABLE ÚT ÞEGAR ER VERIÐ AÐ PRENTA WORKER INSTANCE????
        #BÆTA VIÐ TIL HVAÐA ÁFANGASTAÐAR ÞEIR ERU AÐ FARA!!!!!!
        unavailableList = []
        destinationName = ""
        workerList = WorkerLL.get_worker_list(self)
        voyages = self.IOAPI.request_voyagestoWorker()
        flightRoutes = self.IOAPI.getAllFlightRouteInstances()
        print(flightRoutes)
        #flights = self.IOAPI.getAllFlightInstances()
        for voyage in voyages:
            destinationID = voyage.flightRouteID 
            for flightroute in flightRoutes:
                if flightroute.flightRouteID == destinationID:
                    destinationName = flightroute.country
                #Finna flight route id í flight route og skila flight route country
            if date in voyage.departureFromIS or date in voyage.departureToIS:
                for worker in workerList:
                    if pos == "Pilot":
                        if voyage.mainPilot == worker.socialSecurityNumber:
                            toAddList = []
                            toAddList.append(worker)
                            toAddList.append("\n is going to " + str(destinationName))
                            unavailableList.append([str(worker) + "\n is going to " + str(destinationName)]) #Bæta við destinationName
                        elif voyage.assistingPilot == worker.socialSecurityNumber:
                            unavailableList.append([str(worker) + "\n is going to " + str(destinationName)])
                    elif pos == "Attendant":
                        if voyage.mainFlightAttendant == worker.socialSecurityNumber:
                            unavailableList.append([str(worker) + "\n is going to " + str(destinationName)]) #Bæta við destinationName
                        elif voyage.socialSecurityNumber in voyage.getflightAttendants():
                            unavailableList.append([str(worker) + "\n is going to " + str(destinationName)])
        return unavailableList"""
        
     
    """def listAvailableWorkersbydate(self, date, pos, unavailableList):
        availableList = []
        workerList = WorkerLL.get_worker_list(self)
        voyages = self.IOAPI.request_voyagestoWorker()
        for instance in voyages:
            if date not in instance.departureFromIS or date not in instance.departureToIS:
                    for worker in workerList:
                        if pos == "Pilot":
                            if instance.mainPilot == worker.socialSecurityNumber:
                                availableList.append(worker)
                            elif instance.assistingPilot == worker.socialSecurityNumber:
                                availableList.append(worker)
                        elif pos == "Attendant":
                            if instance.mainFlightAttendant == worker.socialSecurityNumber:
                                availableList.append(worker)
                            elif worker.socialSecurityNumber in instance.getflightAttendants():
                                availableList.append(worker)
        return availableList"""




# +++++++++ Test Case ++++++++++
# workerLL = WorkerLL()
# workerLL.find_worker_by_ID("1")

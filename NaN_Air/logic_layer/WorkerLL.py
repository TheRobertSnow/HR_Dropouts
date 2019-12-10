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
                elif instance.position == "Copilot":
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

    def updateWorker(self, socialSecurityNumber, key, newValue): 
        #self.worker = IOAPI.request_workers()
        self.worker = WorkerLL.get_worker_list(self)
        for instance in self.worker:
            if instance.socialSecurityNumber == socialSecurityNumber:
                updatedWorker = self.IOAPI.updateWorker(instance, key, newValue)
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

    def listUnavailableWorkersbydate(self, date, pos):
        pass

    def listAvailableWorkersbydate(self, date, pos):
        pass

    def updateWorker(self, socialSecurityNumber, key, newValue):
        pass




# +++++++++ Test Case ++++++++++
# workerLL = WorkerLL()
# workerLL.find_worker_by_ID("1")

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
        notFoundString = "{} not found!".format(pos)
        return notFoundString

    def findWorkerByPOS(self, position):
        self.worker = self.IOAPI.request_workers()
        positionList = []
        if position == "Pilot":
            for instance in self.worker:
                if instance.position == "Captain" or "Copilot":
                    positionList.append(instance)
        elif position == "Attendant":
            for instance in self.worker:
                if instance.position == "Flight Service Manager" or "Flight Attendant":
                    positionList.append(instance)
        if len(positionList) == 0:
            positionList = "No {}'s found!.".format(position)
        return positionList

    """def updateWorker(socialSecurityNumber, key, newValue): #Verðum að gera function til þess að taka upp eitt instance!!!
        self.worker = self.IOAPI.request_workers()
        for instances in self.worker:
            if instance.socialSecurityNumber == socialSecurityNumber:
                workertoUpdate = instances
                #Svo vantar að uppfæra actually hlutinn"""


    def viewAllWorkers(self):
        self.worker = self.IOAPI.request_workers()
        return self.worker

    def createNewWorker(self, createWorkerList):
        createWorkerList.append("TRUE")
        createWorkerList.append("TRUE")
        worker = self.IOAPI.createNewWorker(createWorkerList)
        return worker
        





# +++++++++ Test Case ++++++++++
# workerLL = WorkerLL()
# workerLL.find_worker_by_ID("1")

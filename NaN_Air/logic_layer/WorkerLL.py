import IOAPI
from logic_layer import Worker
import collections

class WorkerLL():
    def __init__(self):
        """Calling me will create a object for every worker in the worker.csv file"""
        self.ioAPI = IOAPI.IOAPI()
        self.workerList = self.ioAPI.getWorkerList()
        self.instanceList = []
        for object in self.workerList:
            worker = Worker.CreateWorker(object)
            self.instanceList.append(worker)
        print(len(self.instanceList), "Worker objects in our system")

    def createNewWorker(self, workerList): #Verður að fá inn SSN til þess að búa til nýja starfsmanninn
        for worker in self.instanceList:
            workerssn = worker.socialSecurityNumber
            if workerList[0] == workerssn:
                return "Worker with that Social security number already exists, Worker creation failed"
            
        orderedDict = collections.OrderedDict()
        newID = self.ioAPI.getHigestFlightID()
        orderedDict["ID"] = newID
        orderedDict["Social security number"] = workerList[0]
        orderedDict["Name"] = workerList[1]
        orderedDict["Position"] = workerList[2]
        orderedDict["Plane license"] = workerList[3]
        orderedDict["Address"] = workerList[4]
        orderedDict["Phone"] = workerList[5]
        orderedDict["Cellphone"] = workerList[6]
        orderedDict["Email"] = workerList[7]
        orderedDict["Active"] = "True"
        orderedDict["Available"] = "True"
        workerList.insert(0, newID)
        workerList.insert(8, "True")
        workerList.insert(9, "True")
        newWorker = Worker.CreateWorker(orderedDict)
        self.instanceList.append(newWorker)
        print("Now there are", len(self.instanceList), "Worker objects in the system")
        returnString = self.ioAPI.createWorkerRequest(orderedDict, workerList)
        return returnString
        
    def viewWorkerByPosAndSSn(self, Captain, Copilot, MainFA, FA, ssn):
        for instance in self.instanceList:
            currentssn = instance.socialSecurityNumber
            position = instance.position
            if ssn != "":
                if currentssn == ssn:
                    if position == Captain or position == Copilot or position == MainFA or position == FA:
                        return instance
                    return "Worker found but he is not in this/these positions"
            else:
                if position == Captain or position == Copilot or position == MainFA or position == FA:
                    return instance
        return "Worker not found!"
    
    def update_data_in_file(self, aList):
            """Method takes in list of data, updates the dictionary list
            and writes the changes to file"""
            for index, dictionary in enumerate(self.__dictList ):
                for key, value in dictionary.items():
                    if key == 'Social security number':
                        if value == aList[0]:
                            self[index][aList[1]] = aList[2]
                            self.write____to_file()

    """def updateWorker(aList):
        Takes in a list with SSN of a worker, key and new value
        example list = ["2607962249", "position", "pilot"]
        Returns a string with a outcome

        indexValue = 0
        valueExists = False
        for count, dictionary in enumerate(self):
            for key, value in dictionary.items():
                if key == "social security number":
                    if value == aList[0]:
                        indexValue = count
                        valueExists = True
        if valueExists:
            self[indexValue][aList[1]] = aList[2]
            write____to_file(self)
            return "Worker updated"
        else:
            return "Worker does not exist."
"""
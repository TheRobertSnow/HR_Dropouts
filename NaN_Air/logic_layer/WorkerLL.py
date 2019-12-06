import IOAPI
from logic_layer import Worker
import collections

class WorkerLL():
    def __init__(self):
        """Calling me will create a object for every worker in the worker.csv file"""
        self.ioAPI = IOAPI.IOAPI()
        self.workerList = self.ioAPI.getWorkerList()
        self.instanceList = []
        for dicts in self.workerList:
            worker = Worker.CreateWorker(dicts)
            self.workerList.append(worker)
        print(len(self.instanceList), "objects in our system, this print command is found in WorkerLL")

    def createNewWorker(self, workerInfoList): #Verður að fá inn SSN til þess að búa til nýja starfsmanninn
        """ssn = workerInfoList[0]
        for worker in self.instanceList:
            workerssn = worker.socialSecurityNumber
            if ssn == workerssn:
                return "Worker with that Social Security Number already exists", "Worker creation failed"
        """
        orderedDict = collections.OrderedDict()
        orderedDict["Social Security Number"] = workerInfoList[0]
        orderedDict["Name"] = workerInfoList[1]
        orderedDict["Position"] = workerInfoList[2]
        orderedDict["Plane License"] = workerInfoList[3]
        orderedDict["Address"] = workerInfoList[4]
        orderedDict["Phone"] = workerInfoList[5]
        orderedDict["Cellphone"] = workerInfoList[6]
        orderedDict["Email"] = workerInfoList[7]
        orderedDict["Active"] = "True"
        orderedDict["Available"] = "True"
        workerInfoList.insert(8, "True")
        workerInfoList.insert(9, "True")
        newWorker = Worker.CreateWorker(orderedDict)
        self.instanceList.append(newWorker)
        print("Now there are", len(self.instanceList), "Worker objects in the system")
        returnString = self.ioAPI.createWorkerRequest(orderedDict, workerInfoList)
        return returnString
        

    def update_data_in_file(self, aList):
            """Method takes in list of data, updates the dictionary list
            and writes the changes to file"""
            for index, dictionary in enumerate(self.__dictList ):
                for key, value in dictionary.items():
                    if key == 'social security number':
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
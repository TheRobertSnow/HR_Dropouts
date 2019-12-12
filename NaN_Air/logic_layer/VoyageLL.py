import IOAPI

class VoyageLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()
        self.voyage = self.IOAPI.request_voyages()

    def get_voyage_list(self):
        return self.voyage

    def createNewVoyage(self, dataList):
        return self.IOAPI.createNewVoyage(dataList)

    def find_voyage_by_ID(self, id):
        for instance in self.voyage:
            if instance.voyageID == id:
                return instance

    def create_empty_voyage(self):
        """creates a empty voyage from 2 flights"""
        pass

    def requestPilots(self, voyageID):
        """returns pilots related to the voyage ID you send."""
        pass

    def viewallVoyagesWeek(self, week):
        pass

    def viewallVoyagesDay(self, day):
        pass

    def viewallVoyages(self):
        return self.voyage

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
        for worker in workerList:
            if worker.socialSecurityNumber == pilotToAddInput:
                doesntExist = False
                if worker.position != "Captain":
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
                if i.mainPilot == pilotToAddInput:  # check if already booked
                    return "Error! that pilot is booked for that day."
        # verify if he has the correct license(B Krafa geyma fyrir ef tími er)
        if type(instance) == str:
            return "Voyage was not found"
        # request to update the file and instance.
        return self.IOAPI.updateVoyage(instance, "Main pilot", pilotToAddInput)

    def addCopilotToVoyage(self, voyageID, pilotToAddInput):
        """adds a pilot to a voyage, required the ID of the voyage and the SSN of the worker to add"""
        # verifying the pilot exists and is actually a co pilot
        doesntExist = True
        workerList = self.IOAPI.request_workers()
        for worker in workerList:
            if worker.socialSecurityNumber == pilotToAddInput:
                doesntExist = False
                if worker.position != "Copilot":
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
                if i.assistingPilot == pilotToAddInput:  # check if already booked
                    return "Error! that pilot is booked for that day."
        # verify if he has the correct license(B Krafa geyma fyrir ef tími er)
        if type(instance) == str:
            return "Voyage was not found"
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
                    return "Error! that pilot is booked for that day."
        # verify if he has the correct license(B Krafa geyma fyrir ef tími er)
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
                    return "Error! that pilot is booked for that day."
        # verify if he has the correct license(B Krafa geyma fyrir ef tími er)
        if type(instance) == str:
            return "Voyage was not found"
        # request to update the file and instance.
        return self.IOAPI.updateVoyage(instance, "Flight attendants", pilotToAddInput)

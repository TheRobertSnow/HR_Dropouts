import IOAPI
from datetime import datetime
from logic_layer import FlightLL

class VoyageLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()
        self.voyage = self.IOAPI.request_voyages()
        self.flightLL = FlightLL.FlightLL()

    def get_voyage_list(self):
        return self.voyage

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

    def viewallVoyagesWeek(self, week):
        pass

    def viewallVoyagesDay(self, day):
        pass

    def viewallVoyages(self):
        pass

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
        pass

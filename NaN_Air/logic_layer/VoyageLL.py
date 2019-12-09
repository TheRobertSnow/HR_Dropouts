import IOAPI

class VoyageLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()
        self.voyage = self.IOAPI.request_voyages()

    def get_voyage_list(self):
        return self.voyage

    def find_voyage_by_ID(self, id):
        for instance in self.voyage:
            if instance.voyageID == id:
                return instance

    def create_empty_voyage(self):
        """creates a empty voyage from 2 flights"""
        pass



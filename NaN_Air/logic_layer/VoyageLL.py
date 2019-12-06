import sys
sys.path.append('..')
import IOAPI

class VoyageLL():
    def __init__(self):
        self.IOAPI = IOAPI.IOAPI()

    def get_voyage_list(self):
        self.voyage = self.IOAPI.request_voyages()
        return self.voyage

    def find_voyage_by_ID(self, id):
        for instance in self.voyage:
            if instance.voyageId == id:
                print(instance)

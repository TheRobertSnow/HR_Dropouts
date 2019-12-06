import sys
sys.path.append('..')
import IOAPI


class FlightRouteLL():
    def __init__(self):
        self.ioAPI = IOAPI.IOAPI()

    def get_flight_route_list(self):
        self.flightRoute = self.ioAPI.request_flight_routes()
        return self.flightRoute

    def find_flight_route_by_id(self, id):
        for instance in self.flight:
            if instance.flightID == id:
                print(instance)

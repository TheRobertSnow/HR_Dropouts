import IOAPI
from logic_layer import FlightRoute
import collections


class FlightRouteLL():
    def __init__(self):
        self.ioAPI = IOAPI.IOAPI()
        self.flightRouteDict = self.get


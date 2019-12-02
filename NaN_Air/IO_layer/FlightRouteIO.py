import csv
FILENAME = '../DataFiles/flightRoutes.csv'


class FlightRouteIO():

    def __init__(self):
        self.open_file()

    def read_from_file(self, csvFile):
        csvReader = csv.DictReader(csvFile, delimiter=",")
        next(csvReader, None)
        for line in csvReader:
            print(line)

    def open_file(self):
        with open(FILENAME, encoding="utf8") as csvFile:
            self.read_from_file(csvFile)


flightRoute = FlightRouteIO()

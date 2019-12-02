import csv
FILENAME = '../DataFiles/flightRoutes.csv'


class FlightRouteIO():

    def __init__(self):
        self.open_file()

    def read_from_file(self, csvFile):
        csvReader = csv.DictReader(csvFile, delimiter=",")
        returnList = []
        # next(csvReader, None)
        for line in csvReader:
            # print(line[Flight], line[RouteID], line[Country], line[Airport], line[FlightDistance])
            returnList.append(line)
        return returnList

    def open_file(self):
        with open(FILENAME, encoding="utf8") as csvFile:
            myList = self.read_from_file(csvFile)
            for i in myList:
                print(i)


flightRoute = FlightRouteIO()

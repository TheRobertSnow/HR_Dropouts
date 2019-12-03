import csv
FILENAME = 'DataFiles/flightRoutes.csv'


class FlightRouteIO():

    def __init__(self):
        self.get_instance()

    def get_instance(self):
        """Get a list of dictionaries"""
        self.open_file()
        return self.__dictList

    def find_in_file(self, argList):
        """Search file by specified value(s). Takes in a list of arguments"""
        pass

    def read_from_file(self, csvFile):
        """Function that reads from file opened in 'open_file'"""
        csvReader = csv.DictReader(csvFile, delimiter=",")
        returnList = []
        # next(csvReader, None)
        for line in csvReader:
            returnList.append(line)
        self.__dictList = returnList

    def open_file(self):
        """Function that opens a file"""
        with open(FILENAME, encoding="utf8") as csvFile:
            self.read_from_file(csvFile)

import csv
import collections

FILENAME = "DataFiles/worker.csv"
FIELDNAMES = ["Social Security Number", "Name", "Position", "Address", "Phone", "Cellphone",
              "Email", "Active", "Available", "Plane License"]  # for update row


# if more fieldnames are added, they also have to be added to the newAirplane method along with the FIELDNAMES constant.
def readFile():
    returnList = []
    with open(FILENAME, encoding="utf8") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=",")
        for line in csvReader:
            returnList.append(line)
    return returnList


def writeToFile(list):
    """takes in a list and creates a new row in the airplane.csv file"""
    print(list)
    with open(FILENAME, "a", encoding="utf8", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(list)


def updateRow(objectList):
    """Rewrites the whole csv file with the new and updated object list"""
    with open(FILENAME, "w", encoding="utf8", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(FIELDNAMES)
        for dictionary in objectList:
            writeList = []
            for value in dictionary.values():
                writeList.append(value)
            csvWriter.writerow(writeList)

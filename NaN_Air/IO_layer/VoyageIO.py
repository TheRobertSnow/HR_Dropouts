<<<<<<< HEAD
import csv
import collections

FILENAME = "../DataFiles/voyage.csv"
FIELDNAMES = ["voyage id", "Flight out ID", "Flight back ID", "Main Pilot", "Assisting Pilot", "Main Flight Attendant", "Flight Attendants",  
"Flight route ID", "departure from is", "departure to is"]  # for update row

# if more fieldnames are added, they also have to be added to the newAirplane method along with the FIELDNAMES constant.
def readFile():
    returnList = []
    with open(FILENAME, encoding="utf8") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=",")
        for line in csvReader:
            returnList.append(line)
    return returnList

def writeToFile(list):
    """takes in a list and creates a new row in the voyage.csv file"""
    print(list)
    with open(FILENAME, "a", encoding="utf8", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(list)

#Tester = list1 = ["5", "6", "7", "0101013321", "0101233641", "0101233449", ["1212346219", "1111435259"], "5", "23:00", "03:00"]



=======
import csv
import collections

FILENAME = "../DataFiles/voyage.csv"
FIELDNAMES = ["voyage id", "Flight out ID", "Flight back ID", "Main Pilot", "Assisting Pilot", "Main Flight Attendant", "Flight Attendants",  
"Flight route ID", "departure from is", "departure to is"]  # for update row

# if more fieldnames are added, they also have to be added to the newAirplane method along with the FIELDNAMES constant.
def readFile():
    returnList = []
    with open(FILENAME, encoding="utf8") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=",")
        for line in csvReader:
            returnList.append(line)
    return returnList

def writeToFile(list):
    """takes in a list and creates a new row in the voyage.csv file"""
    print(list)
    with open(FILENAME, "a", encoding="utf8", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(list)

#Tester = list1 = ["5", "6", "7", "0101013321", "0101233641", "0101233449", ["1212346219", "1111435259"], "5", "23:00", "03:00"]



>>>>>>> 6271cd5141a99f1bf0437a89f0b8c0b7e42d2b7b

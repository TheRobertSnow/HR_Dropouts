import IOAPI
from logic_layer import Airplane


class AirplaneLL:
    def __init__(self):
        if __name__ == '__main__':
            myObjects = IOAPI.getPlaneInstance()
            objectList = []
            for dictionary in myObjects:
                temp = Airplane.CreateAirplane(dictionary)
                objectList.append(temp)
            print(objectList)
            for i in objectList:
                print(i)


# main for testing
test = AirplaneLL()

class Router:

    # Private Attributes
    __hostname = "-"
    __brand = "-"
    __model = "-"

    def __init__(self, hostname, brand, model):
        self.__hostname = hostname
        self.__brand = brand
        self.__model = model
    
    def getHostname(self):
        return self.__hostname
    def setHostname(self, name):
        self.__hostname = str(name)

    def getBrand(self):
        return self.__brand
    def setBrand(self, brand):
        self.__brand = str(brand)
    
    def getModel(self):
        return self.__model
    def setModel(self, model):
        self.__model = str(model)


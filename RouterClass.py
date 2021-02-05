class Router:

    # Private Attributes
    __hostname = "-"
    __brand = "-"
    __model = "-"
    __interfaces = {}

    def __init__(self, hostname, brand, model):
        self.__hostname = hostname
        self.__brand = brand
        self.__model = model
    
    # Hostname
    def getHostname(self):
        return self.__hostname

    def setHostname(self, name):
        self.__hostname = str(name)

    # Brand
    def getBrand(self):
        return self.__brand

    def setBrand(self, brand):
        self.__brand = str(brand)
    
    # Model
    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = str(model)

    # Interfaces
    def add_interface(self, intname):
        if intname in self.__interfaces:
            return False
        else:
            self.__interfaces[intname] = {
                                            "name":intname,
                                            "connect_to":"-"
                                        }
            return True

    def get_interface(self, intname):
        if intname in self.__interfaces:
            return self.__interfaces[intname]
        else:
            return {}
    
    def show_interfaces(self, name="all"):
        if name == "all":
            print("\nShow {}'s all interfaces:".format(self.__hostname))
            keys = sorted(self.__interfaces.keys())
            for intf in keys:
                print("\n    Name:", self.__interfaces[intf]["name"])
                self.__printConnectedInterface(self.__interfaces[intf]["connect_to"])
            return True
        else:
            selected_interface = self.get_interface(name)
            if selected_interface == {}:
                print("\nNot found interface {} in {}. Try again!".format(name, self.__hostname))
                return False
            else:
                print("\nShow {}'s {} interface:".format(self.__hostname, name))
                print("\n    Name:", selected_interface["name"])
                self.__printConnectedInterface(selected_interface["connect_to"])
                return True

    def __printConnectedInterface(self, connect_to):
        if connect_to == "-":
            print("    Conect to: -")
        else:
            print("    Conect to: something")

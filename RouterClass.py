class Router:

    def __init__(self, hostname, brand, model):
        # Private Attributes
        self.__hostname = hostname
        self.__brand = brand
        self.__model = model
        self.__interfaces = {}
    
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
            print("    Conect to: {} interface {}".format(connect_to["hostname"], connect_to["interface"]))

    def connect_to(self, des_router, intf, withIntf):
        des_intf = des_router.get_interface(intf)
        src_intf = self.get_interface(withIntf)
        # Show error if interfaces not found or interface already taken
        des_intf_status = self.__checkInterfaceStatus(des_router.getHostname(), des_intf, intf)
        src_intf_status = self.__checkInterfaceStatus(self.getHostname(), src_intf, withIntf)
        if des_intf_status == False:
            return False
        if src_intf_status == False:
            return False
        # Connect 2 routers and show Success messege
        des_intf["connect_to"] = {"hostname": self.getHostname(), "router":self, "interface":withIntf}
        src_intf["connect_to"] = {"hostname": des_router.getHostname(), "router":des_router, "interface":intf}
        print("\n{}'s {} is connected to {}'s {}.".format(self.getHostname(), withIntf, des_router.getHostname(), intf))
        return True         
    
    def __checkInterfaceStatus(self, hostname, interface, interface_name):
        if interface == {}:
            print("\nNot found interface {} in {}".format(interface_name, hostname))
            return False
        elif not interface["connect_to"] == "-":
            print("\n{} interface {} is already connected to another router..".format(hostname, interface_name))
            return False
        return True

    def show_cdp_neighbor(self):
        print("\nShow {}'s CDP neighbor:".format(self.getHostname()))
        print("    Hostname\tDes_intf\tSrc_intf\t")
        keys = sorted(self.__interfaces.keys())
        for intf in keys:
            if not self.__interfaces[intf]["connect_to"] == "-":
                tmp = self.__interfaces[intf]["connect_to"]
                print("  > {}\t\t{}\t\t{}".format(tmp["hostname"], tmp["interface"], intf))

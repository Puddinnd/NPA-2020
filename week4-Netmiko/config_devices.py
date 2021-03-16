from Utils import *

def main():
    print("_______________________________________________")
    print("|                                              |")
    print("|  Select an options to configure:             |")
    print("|   [0]: all                                   |")
    print("|   [1]: IP addresses                          |")
    print("|   [2]: access-lists                          |")
    print("|   [3]: OSPF                                  |")
    print("|   [4]: enable CDP and LLDP                   |")
    print("|   [5]: description based on CDP              |")
    print("|   [6]: NAT and advertise default route (R5)  |")
    # print("|                                 |")
    # print("|  use comma to select multiple   |")
    # print("|  like: 1,2                      |")
    print("|______________________________________________|")
    print()
    option = input("Choose: ").strip()
    print()

    if option == 0:
        configInterfaces()
        configACL()
    elif option == "1":
        configInterfaces()
    elif option == "2":
        configACL()
    elif option == "3":
        configOSPF()
    elif option == "4":
        configCDPnLLDP()
    elif option == "5":
        configDescription()
    elif option == "6":
        NATnDefaultRoute2R5()
    else:
        print("Invalid option.")
        print()

main()

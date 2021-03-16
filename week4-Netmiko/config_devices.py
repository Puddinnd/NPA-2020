from Utils import *

def main():
    print("____________________________________")
    print("|                                  |")
    print("| Select an options to configure:  |")
    print("|   [0]: all                       |")
    print("|   [1]: IP addresses              |")
    print("|   [2]: access-lists              |")
    print("|   [3]: OSPF                      |")
    print("|   [4]: enable CDP and LLDP       |")
    print("|   [5]: description based on CDP  |")
    # print("|                                 |")
    # print("|  use comma to select multiple   |")
    # print("|  like: 1,2                      |")
    print("|__________________________________|")
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
    else:
        print("Invalid option.")
        print()

main()

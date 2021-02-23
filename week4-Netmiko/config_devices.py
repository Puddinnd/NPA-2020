from Utils import *

def main():
    print("___________________________________")
    print("|                                 |")
    print("| Select an options to configure: |")
    print("|   [0]: all                      |")
    print("|   [1]: IP addresses             |")
    print("|   [2]: access-lists             |")
    # print("|                                 |")
    # print("|  use comma to select multiple   |")
    # print("|  like: 1,2                      |")
    print("|_________________________________|")
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
    else:
        print("Invalid option.")
        print()

main()

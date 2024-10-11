from source.customer import *
from source.shop_owner import *

class Main():
    if UserValidation.valid_user:
        print("\nWelcome To Unique Products Store !\n")
        print("Choose One: ")
        print("1. Do you want to continue with your Location PIN.\n")
        print("2. Do you want to continue with Location ID.\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Location.display_loc_pin()
        elif choice == 2:
            Location.display_loc_id()
        else:
            print("Invalid choice. Please try again.")
            

Main()
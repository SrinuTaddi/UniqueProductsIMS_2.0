import json
from source.customer import *
from source.shop_owner import *

class Main:
    def main(self):
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        if UserValidation.valid_user(username, password):
            with open("database/user.json", "r") as data_file:
                data = json.load(data_file)
            with open("database/shops.json", "r") as shop_file:
                shop_data = json.load(shop_file)

            user_type = None
            if username in [usr['username'] for usr in data.get("customers", [])]:
                user_type = "customer"
            elif username in [usr['username'] for usr in data.get("shop_owners", [])]:
                user_type = "owner"

            if user_type:
                print("\nChoose One: ")
                print("1. Continue with Location PIN.")
                print("2. Continue with Location ID.\n")
                choice = int(input("Enter your choice: \n"))

                if choice == 1:
                    loc_id = Location.display_loc_pin()
                elif choice == 2:
                    loc_id = Location.display_loc_id()
                else:
                    print("Invalid choice. Please try again.")
                    
            shop_loc = []
            for shop in shop_data['shop_details']:
                if loc_id == shop['loc_id']:
                    shop_loc.append(loc_id)
                    break
                # print(f"Shop_Loc : {shop_loc}")

            # print(f"Loc : {shop_loc}")
            if user_type == "customer":
                Shop.shop_details(shop_loc)
                # print(f"Shop_ loc - {shop_loc}")
                choice = (input("\nDo you want to place an order? (yes/no): ").strip()).lower()
                if choice == "yes":
                    # shop_loc = input("Enter Loc-ID: ").strip()
                    PlaceOrder.place_order(shop_loc)
                else:
                    print("Thank you for visiting our shop!")

            elif user_type == "owner":
                shop_id = []
                for shop in data['shop_owners']:
                    if username == shop['username']:
                        shop_id = shop['shop_id']
                # Shop.shop_details(loc_id)
                # choice = (input("\nDo you want to add items to the shop? (yes/no): ").strip()).lower()
                # shop_id = [name for name in shop_data['shop_details'] if username == name['shop_owner'] name.append()]
                if shop_id:
                    print("\nChoose One: ")
                    print("1. Add Item to the Shop.")
                    print("2. Delete Item from the Shop.")
                    print("3. Update Item from the Shop.\n")
                    choice = int(input("Enter your choice: \n"))
                    if choice == 1:
                        # shop_in_loc = [shop for shop in shop_owner if shop['shop_id'] == shop_id]
                        AddItem.add_new_item(loc_id, shop_id)
                        
                    elif choice == 2:
                        # shop_id = input("Enter your Shop ID: ").strip()
                        DeleteItem.delete_item(loc_id, shop_id)
                    elif choice == 3:
                        # shop_id = input("Enter your Shop ID: ").strip()
                        UpdateItem.update_item(loc_id, shop_id)
                    else:
                        print("Invalid Choice !")
                else:
                    print("Shop not found !")

        else:
            print("Login failed. Please try again.")


if __name__ == "__main__":
    upims = Main()
    upims.main()
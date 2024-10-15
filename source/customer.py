import json
import sys 

class Shop:

    def shop_details(loc_id):
        with open("database/shops.json", "r") as shop_file:
            shop_data = json.load(shop_file)
        for shop in shop_data["shop_details"]:
            if loc_id == shop['loc_id']:
                print("\n----- Shop's Info -----\n")
                print(f"\nShop Name: {shop['shop_name']} \nShop Id: {shop['shop_id']}\nShop Owner: {shop['shop_owner']}\nShop Address: {shop['shop_address']}\n")
                print("Items: \n")
                for items in shop["shop_items"]:
                    print(f"Id: {items['item_id']}, Name: {items['item_name']}, Price: {items['item_price']}, Size: {items['item_size']}, Quantity: {items['item_quantity']}\n")
        return shop['shop_id'], loc_id

class Location:

    def display_loc_pin():
        with open("database/shops.json", "r") as loc_file:
            loc_data = json.load(loc_file)
        for pins in loc_data['locations']:
            print(f"{pins['loc_name']} - PIN : {pins['loc_pin']}")
        location_found = False
        loc_pin = input("\nEnter your location PIN to view Location details: ")
        for loc in loc_data['locations']:
            if str(loc['loc_pin']) == loc_pin:
                location_found = True
                loc_id = loc['loc_id']
                Shop.shop_details(loc_id)
        if not location_found:
            print("Invalid Location PIN !")
        return loc_id


    def display_loc_id():
        with open("database/shops.json", "r") as loc_file:
            loc_data = json.load(loc_file)
        for location in loc_data['locations']:
            print(f"{location['loc_name']} - Location ID : {location['loc_id']}")
        location_found = False
        location_id = input("\nEnter your location id to view Location details: ")
        for loc in loc_data['locations']:
            if loc['loc_id'] == location_id:
                location_found = True
                loc_id = loc['loc_id']
                Shop.shop_details(loc_id)
        if not location_found:
            print("Invalid Location ID !")
        return loc_id

class PlaceOrder:
    def place_order(loc_id):
        with open("database/shops.json", "r") as shop_file:
            shop_data = json.load(shop_file)
        shop_id = input("Enter shop id: ").strip()
        shop_found = False
        for shop in shop_data['shop_details']:
            if shop_id == shop['shop_id']:
                shop_found = True
                item_found = False
                item_id = input("Enter item id: ").strip()
                for item in shop['shop_items']:
                    if item['item_id'] == item_id:
                        item_found = True
                        print(f"Item name : {item['item_name']}, Order placed successfully!")
                if not item_found:
                    print("Invalid item id !")
        if not shop_found:
            print("invalid shop details!")
    


class UserValidation:

    def valid_user(username, password):
        with open("database/user.json", "r") as user_file:
            user_data = json.load(user_file)

        users_data = user_data.get("customers", []) + user_data.get("shop_owners", [])

        user_details = False
        for usr in users_data:
            if username == usr["username"] and password == usr["password"]:
                    user_details = True
                    print(f"\nWelcome To Unique Products, {username} !\n")
                    # print("\nWelcome To Unique Products Store !\n")
                    # print("Choose One: ")
                    # print("1. Do you want to continue with your Location PIN.\n")
                    # print("2. Do you want to continue with Location ID.\n")
                    # choice = int(input("Enter your choice: "))
                    # if choice == 1:
                    #     Location.display_loc()
                    # elif choice == 2:
                    #     Location.get_loc()
                    # else:
                    #     print("Invalid choice. Please try again.")
 
                    return True

        if not user_details:
            print("User not found!")
        return user_details
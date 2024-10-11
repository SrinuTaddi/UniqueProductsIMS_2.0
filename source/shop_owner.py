import json 
import sys

""" I'm commmenting the below class of the code, I'm already using the below class in my previous file(customer.py), so i can access it from my 'main.py' file. """

# class UserValidation:

#     def valid_user(username, password):
#         with open("database/user.json", "r") as user_file:
#             user_data = json.load(user_file)

#         users_data = user_data.get("customers", []) + user_data.get("shop_owners", [])

#         user_details = False
#         for usr in users_data:
#             if username == usr["username"] and password == usr["password"]:
#                     user_details = True
#                     print(f"Welcome {username} !\n")
#                     # print("\nWelcome To Unique Products Store !\n")
#                     # print("Choose One: ")
#                     # print("1. Do you want to continue with your Location PIN.\n")
#                     # print("2. Do you want to continue with Location ID.\n")
#                     # choice = int(input("Enter your choice: "))
#                     # if choice == 1:
#                     #     Location.display_loc_pin()
#                     # elif choice == 2:
#                     #     Location.display_loc_id()
#                     # else:
#                     #     print("Invalid choice. Please try again.")
#         if not user_details:
#             print("User not found!")
#         return user_details

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
            print("Invalid Location ID !")


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

class Shop:

    def shop_details(loc_id):
        with open("database/shops.json", "r") as shop_file:
            shop_data = json.load(shop_file)
        for shop in shop_data["shops"]:
            if loc_id == shop['loc_id']:
                print("\n----- Shop's Info -----\n")
                print(f"\nShop Name: {shop['shop_name']} \nShop Id: {shop['shop_id']}\nShop Owner: {shop['shop_owner']}\nShop Address: {shop['shop_address']}\n")
                print("Items: \n")
                for items in shop["shop_items"]:
                    print(f"Id: {items['item_id']}, Name: {items['item_name']}, Price: {items['item_price']}, Size: {items['item_size']}, Quantity: {items['item_quantity']}\n")
        return shop['shop_id']


class AddItem:
    def add_new_item(loc_id, shop_id):
        with open("database/shops.json", "r") as shop_file:
            shop_data = json.load(shop_file)
        shop_id = Shop.shop_details(loc_id)
        shop_found = False
        for shop in shop_data['shops']:
            if shop['loc_id'] == loc_id and shop["shop_id"] == shop_id:
                shop_found = True
                item_id = input("Enter item id: ")
                item_name = input("Enter item name: ")
                item_price = input("Enter item price: ")
                item_size = input("Enter item size: ")
                item_quantity = input("Enter item quantity: ")
                new_item = {
                    "item_id": item_id,
                    "item_name" : item_name,
                    "item_price" : item_price,
                    "item_size" : item_size,
                    "item_quantity" : item_quantity
                }
                shop["shop_items"].append(new_item)
                with open("database/shops.json", "w") as shop_f:
                    json.dump(shop_data, shop_f, indent=4)
                print(f"{item_name} is added to the {shop['shop_name']} shop.")
        if not shop_found:
            print("Shop not found. Please try again.")


class DeleteItem:
    def delete_item(loc_id, shop_id):
        with open("database/shops.json", "r") as shop_file:
            shop_data = json.load(shop_file)
        shop_id = Shop.shop_details(loc_id)
        shop_found = False
        for shop in shop_data["shops"]:
            if shop['loc_id'] == loc_id and shop["shop_id"] == shop_id:
                shop_found = True
                item_id = input("Enter item id: ").strip()
                item_found = False
                for item in shop["shop_items"]:
                    if str(item["item_id"]) == item_id:
                        item_found = True
                        shop["shop_items"].remove(item)
                        with open("database/shops.json", "w") as shop_file:
                            json.dump(shop_data, shop_file, indent=4)
                        print(f"Item id : {item['item_id']} is deleted from the items list.")
                if not item_found:
                    print("Item not found. Please try again.")
        if not shop_found:
            print("Shop not found. Please try again.")


class UpdateItem:
    def update_item(loc_id, shop_id):
        with open("database/shops.json") as shop_file:
            shop_data = json.load(shop_file)
        shop_id = Shop.shop_details(loc_id)
        shop_found = False
        for shop in shop_data['shops']:
            if shop['loc_id'] == loc_id and shop['shop_id'] == shop_id:
                shop_found = True
                item_id = input("Enter item id: ").strip()
                item_found = False
                for item in shop['shop_items']:
                    if str(item['item_id']) == item_id:
                        item_found = True
                        print(f"Item Details: {item}")
                        item['item_name'] = input("Enter Item Name: ").strip()
                        item['item_price'] = input("Enter Item Price: ").strip()
                        item['item_size'] = input("Enter item size: ").strip()
                        item['item_quantity'] = input("Enter item quantity: ").strip()
                        print("Item updated successfully !")
                        break
                if not item_found:
                    print("Item not found. Please try again.")
        if not shop_found:
            print("Shop not found. Please try again.")
        with open("database/shops.json", "w") as shop_file:
            json.dump(shop_data, shop_file, indent=4)


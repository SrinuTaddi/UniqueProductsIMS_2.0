# import json

# class PlaceOrder:
#     def place_order(loc_id):
#         with open("database/shops.json", "r") as shop_file:
#             shop_data = json.load(shop_file)
#         shop_found = False
#         shop_id = input("Enter shop id: ").strip()
#         for shop in shop_data['shop_details']:
#             if loc_id == shop['loc_id'] and shop_id == shop['shop_id']:
#                 shop_found = True
#                 item_found = False
#                 item_id = input("Enter item id: ").strip()
#                 for item in shop['shop_items']:
#                     if item['item_id'] == item_id:
#                         item_found = True
#                         print(f"Item name : {item['item_name']}, Order placed successfully!")
#                 if not item_found:
#                     print("Invalid item id !")
#         if not shop_found:
#             print("invalid shop details!")
# loc_id = input("Enter Location ID: ")
# PlaceOrder.place_order(loc_id)
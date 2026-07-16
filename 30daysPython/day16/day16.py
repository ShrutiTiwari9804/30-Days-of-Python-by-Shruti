import json 
import os

class InventoryManager:

    def __init__(self):
        self.filename = "inventory.json"
        self.inventory = []
        self.load_inventory()

    def load_inventory (self):
        if os.path.exists(self.filename):
            with open (self.filename, "r") as file:
                try:
                    self.inventory = json.load(file)
                except json.JSONDecodeError:
                    self.inventory = []

        else:
            self.save_inventory()

    def save_inventory(self):
        with open(self.filename, "w") as file:
            json.dump (self.inventory , file, indent = 4)
            
    def generate_id(self):
        if not self.inventory:
            return 1
        return max(item["id"] for item in self.inventory) + 1
    
    def add_product (self):
        name = input("Enter Product Name: ").strip()

        category = input ("Enter category : ").strip()

        quantity = int(input("Enter Quantity: "))

        price = float (input("Enter Price: "))

        product = {
            "id" : self.generate_id(),
            "name" : name,
            "category" : category,
            "quantity" : quantity,
            "price" : price

        }

        self.inventory.append(product)
        self.save_inventory()


        print("Product Added Successfully! ")

    def view_products(self):

        if not self.inventory:
            print("Inventory is empty. ")
            return
        
        print("\n------- INVENTORY -------")

        for item in self.inventory:
            print(f"""
ID       :  {item['id']}                
Name     :  {item['name']}       
Category :  {item['category']}      
Quantity :  {item['quantity']} 
Price    :  ₹{item['price']}            
-------------------------------------             
                  
""")
            
    def search_product(self):

        keyword =  input ("Enter Product: ").lower()

        found = False

        for item in self.inventory:

            if keyword in item["name"].lower():

                print(item)
                found = True

        if not found:
            print("Product Not Found.")

    def update_product(self):

        product_id = int(input("Enter Product ID: "))

        for item in self.inventory:

            if item ["id"] == product_id:

                item ["name"] = input("New Name: ")

                item ["category"] = input("New Categoey: ")

                item [" quantity"] = int(input("New Price: "))

                item ["price"] = float(input("New Price: " ))

                self.save_inventory()

                print("Product Updated Successfully!")

                return 
            
        print("Product Not Found. ")

    def delete_product(self):

        product_id = int(input("Enter Product ID: "))

        for item in self.inventory:

            if item["id"] == product_id:

                self.inventory.remove(item)

                self.save_inventory()

                print("Product Deleted Successfully!")

                return

        print("Product Not Found.")

    def low_stock(self):

        limit = int(input("Show products below quantity: "))

        found = False

        for item in self.inventory:

            if item["quantity"]  < limit:

                print(item)

                found = True

        if not found:
            print("No Low Stock Products: ")

    def total_inventory_value(self):

        total = 0

        for item in self.inventory:
            total += item["quantity"] * item["price"]

        print("f\nTotal Inventory Value = ₹{total:.2f}")

    def menu(self):
        
        while True:

            print("""
========== Inventory Management ======================
1. Add Product
2. View Products                  
3. Search Product                  
4. Update Product                  
5. Delete Product                  
6. Low Stock Report                 
7. Total Inventory Value                  
8. Exit                 
==================================================                 
""")
            
            choice = input ("Enter Choice: ")

            if choice == "1":
                self.add_product()

            elif choice == "2":
                self.view_products()

            elif choice == "3":
                self.search_product()

            elif choice == "4":
                self.update_product()

            elif choice == "5":
                self.delete_product()

            elif choice == "6":
                self.low_stock()

            elif choice == "7":
                self.low_stock()

            elif choice == "8":
                print("Thank you!")
                break

            else: 
                print("Invalid Choice")

manager = InventoryManager()
manager.menu()










                
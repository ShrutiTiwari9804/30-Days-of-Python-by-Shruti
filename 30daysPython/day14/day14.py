class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
class ShoppingCart:
    def __init__ (self):
        self.cart = []

    # CREATE
    def add_product(self):
        name = input("Enter product name: ")

        price = float(input("Enter price: "))

        quantity = int(input("Enter quantity: "))

        product = Product(name, price, quantity)

        self.cart.append(product)

        print("Product added successfully.")

    # READ
    def view_cart(self):

        if not self.cart:
            print ("\nCart is empty.")
            return
        
        print("\n======= SHOPPING CART ========")

        total = 0

        for i , product in enumerate(self.cart, start = 1):

            print (f"{i}. {product.name}")
            print (f"  Price   :₹{product.price}")
            print(f"   Quantity : {product.quantity}")
            print (f" Total : ₹{product.total_price()} ")

            total += product.total_price()

            print("-" * 35)

        print (f"Grand Total : ₹{total}")


    # UPDATE

    def update_quantity(self):

        if not self.cart:
            print("Cart is empty.")
            return
        
        self.view_cart()

        index = int(input("Enter product number to update: "))

        if 0 <= index < len(self.cart):
            qty = int(input("Enter new quantity: "))
            self.cart[index].quantity = qty
            print("Quality updated successfully.")

        else:
            print("Invalid product number.")

    # DELETE
    def remove_product(self):

        if not self.cart:
            print("Cart is empty.")
            return
        
        self.view_cart()

        index = int(input("Enter product number to remove: "))

        if 0 <= index < len(self.cart):
            removed = self.cart.pop(index)
            print(f"{removed.name} removed successfully.")
        else:
            print("Invalid product number.")


def main():

    cart = ShoppingCart()

    while True:

        print("\n ======= SHOPPING CART SYSTEM =======")
        print ("1. Add Product")
        print("2. View Cart")
        print("3. Update Quantity")
        print("4. Remove Product")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            cart.add_product()
        elif choice == "2":
            cart.update_quantity()
            
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            cart.remove_product()
        elif choice == "5":
            print("Thankyou for shoppping!")
            break
        else:
            print("Invalid choice.")



main()

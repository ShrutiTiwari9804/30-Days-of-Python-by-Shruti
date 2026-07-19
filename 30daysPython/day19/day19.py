class FoodItem:
    def __init__(self, food_id, name, price):
        self.food_id = food_id
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.food_id}. {self.name} - {self.price}")


class FoodOrderingSystem:
    def __init__(self):
        self.menu = []
        self.cart = []

    def add_food(self):
        food_id = len(self.menu) + 1
        name = input("Enter food name: ")
        price = float(input("Enter food price: "))

        food = FoodItem(food_id, name, price)
        self.menu.append(food)

        print("Food added successfully!\n")

    def display_menu(self):
        if not self.menu:
            print("Menu is empty.\n")
            return
        
        print("\n--------- MENU --------")
        for food in self.menu:
            food.display()
        print()


    def order_food(self):
        if not self.menu:
            print("No food Available.\n")
            return
        
        self.display_menu()
        food_id = int(input("Enter Food ID to order: "))

        for food in self.menu:
            if food.food_id == food_id:
                self.cart.append(food)
                print(f"{food.name} added to cart.\n")
                return
            

        print("Invalid Food ID.\n")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.\n")
            return
        
        total = 0

        print("\n --------- YOUR CART ---------")

        for food in self.cart:
            print(f"{food.name} - {food.price}")
            total += food.price

        print("-------------------------")
        print(f"Total Bill: {total}\n")

    def remove_from_cart(self):
        if not self.cart:
            print("Cart is empty.\n")
            return
        
        self.view_cart()

        name = input ("Enter food name to remove : ")

        for food in self.cart:
            if food.name.lower() == name.lower():
                self.cart.remove(food)
                print("Food removed.\n")
                return
            
        print("Food not found.\n")

def main():
    system = FoodOrderingSystem()

    while True:
        print("=========== FOOD ORDERING SYSTEM ==============")
        print("1. Add Food")
        print("2. Display Menu")
        print("3. Order Food")
        print("4. View CART")
        print("5. Remove From cart")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_food()

        elif choice == "2":
            system.display_menu()

        elif choice == "3":
            system.order_food()

        elif choice == "4":
            system.view_cart()

        elif choice == "5":
            system.remove_from_cart()

        elif choice == "6":
            print("Thnak You for Using Food Ordering System.")

        else:
            print("Invalid Choice!\n")

if __name__ == "__main__":
    main()
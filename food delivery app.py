class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = len(self.food_items) + 1
        self.food_items.append(food_item)
        print("Food item added successfully")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item updated successfully")
                return
        print("Food item not found")

    def view_food_items(self):
        print("List of all food items:")
        for food_item in self.food_items:
            print(f"{food_item.food_id}. {food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully")
                return
        print("Food item not found")

class User:
    def __init__(self):
        self.name = None
        self.phone_number = None
        self.email = None
        self.address = None
        self.password = None
        self.orders = []

    def register(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("User registered successfully")

    def login(self, email, password):
        if self.email == email and self.password == password:
            print("User logged in successfully")
            return True
        print("Invalid email or password")
        return False

    def place_new_order(self, food_items):
        order = []
        total_price = 0
        for food_item in food_items:
            if food_item <= len(admin.food_items):
                food_item = admin.food_items[food_item - 1]
                if food_item.stock > 0:
                    order.append(food_item)
                    total_price += food_item.price
                    food_item.stock -= 1
        if order:
            self.orders.append(order)
            print("Order placed successfully")
            print(f"Total price: INR {total_price}")
        else:
            print("No items selected or items out of stock")

    def order_history(self):
        print("List of all orders:")
        for i, order in enumerate(self.orders):
            print(f"{i+1}.")
            for food_item in order:
                print(f"{food_item.name} ({food_item.quantity}) [INR {food_item.price}]")
            print()

    def update_profile(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully")

admin = Admin()
user = User()

# Admin 
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 100)
admin.add_food_item("Vegan Burger", "1 piece", 320, 10, 50)
admin.add_food_item("Truffle Cake", "500gm", 900, 5, 20)
admin.add_food_item("Truffle Cake", "500gm", 900, 5, 20)
admin.view_food_items()
admin.edit_food_item(2, "Vegan Burger", "2 pieces", 400, 10, 50)
admin.remove_food_item(3)
admin.view_food_items()

# User 
user.register("John Doe", "+91 9876543210", "johndoe@example.com", "123 Main St, Anytown", "password")
user.login("johndoe@example.com", "password")
user.place_new_order([2, 3])
user.order_history()
user.update_profile("John Doe", "+91 9876543210", "johndoe@example.com", "456 Main St, Anytown", "newpassword")

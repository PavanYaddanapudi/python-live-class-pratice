items = {
    "Bread": 40,
    "Cookies": 80,
    "Butter": 120,
    "Cheese": 180,
    "Yoghurt": 60
}
cart = []

def view_items():
    print("Items Available:")
    for item, price in items.items():
        print(f"Name: {item} Price: {price}")

def add_to_cart():
    item_name = input("Enter the item name: ").capitalize()
    if item_name in items:
        try:
            quantity = int(input("Enter the quantity: "))
            cart.append([item_name, quantity, items[item_name], quantity * items[item_name]])
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Item not found.")

def update_cart():
    item_name = input("Which item to be updated: ").capitalize()
    for i, cart_item in enumerate(cart):
        if cart_item[0] == item_name:
            try:
                new_quantity = int(input("Enter the quantity to be updated: "))
                cart[i][1] = new_quantity
                cart[i][3] = new_quantity * cart[i][2]
                return
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
    print("Item not found in cart.")

def delete_from_cart():
    item_name = input("Which item to be removed: ").capitalize()
    for i, cart_item in enumerate(cart):
        if cart_item[0] == item_name:
            cart.pop(i)
            return
    print("Item not found in cart.")

def print_bill():
    print("Name, Quantity, Price, Total")
    total_amount = 0
    for item_name, quantity, price, total in cart:
        print(f"{item_name}, {quantity}, {price}, {total}")
        total_amount += total
    print(f"Total Amount of Bill: {total_amount}")

while True:
    print("\nWhat do you want to do?")
    print("1. View items")
    print("2. Add items to cart")
    print("3. Update items in cart")
    print("4. Delete items from cart")
    print("5. Print bill")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_items()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            update_cart()
        elif choice == 4:
            delete_from_cart()
        elif choice == 5:
            print_bill()
        elif choice == 6:
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

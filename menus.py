from orders import sandwich_menu
from orders import on_going_orders
from orders import finished_sandwiches
from orders import menu_list
# Function to display the sandwich menu
def display_menu(menu):
    print("** Sandwich Menu **")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def order_sandwich(menu):
    while True:
        user_input = input("Please enter the name of the sandwich you want to order: \n")
        if user_input in menu:
            confirm = input(f"Are you sure you want to add \033[1;32m{user_input}\033[0m to the order list? (Yes/No) ")
            if confirm.lower() == "yes":
                menu_list.remove(user_input)
                on_going_orders.append(user_input)
                print("Sandwich ordered.")
                break
            elif confirm.lower() == "no":
                break
            else:
                print("Invalid input. Please try again.")

def view_orders():
    print("Ongoing Orders:")
    for order in on_going_orders:
        print(order)
    print("Finished Orders:")
    for order in finished_sandwiches:
        print(order)

def remove_order():
    while True:
        user_input = input("Please enter the name of the sandwich you want to remove: \n")
        if user_input in on_going_orders:
            confirm = input(f"Are you sure you want to remove \033[1;32m{user_input}\033[0m to the list? (Yes/No) ")
            if confirm.lower() == "yes":
                on_going_orders.remove(user_input)
                print("Sandwich removed.")
                break
            else:
                print("Removed canceled.")
        else:
            print("Invalid input. Please try again.")


def main_menu():
    while True:
        user_input = input("Please select an option: \n1. View Menu,\n2. Order a Sandwich,\n3. View Orders,\n4. Remove an order,\n5. Exit: \n")
        if user_input == "1":
            display_menu(sandwich_menu)
        elif user_input == "2":
            order_sandwich(sandwich_menu)
        elif user_input == "3":
            view_orders()
        elif user_input == "4":
            remove_order()    
        elif user_input == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_menu()

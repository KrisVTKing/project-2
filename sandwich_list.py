from orders import on_going_orders
from add_sandwich_oder import add_sandwich_order
from orders import finished_sandwiches
from finished_oder import order_finished
from remove_order import remove_order
from orders import list
from orders import menu_list

def find_missing_items(full_menu, menu_with_orders):
    missing_items = []
    for item in menu_with_orders:
        if item not in full_menu and item not in missing_items:
            missing_items.append(item)
    return missing_items

missing_items = find_missing_items(list, menu_list + on_going_orders)
print("Missing Items:")
for item in missing_items:
    print(item)


def main_menu():
    while True:
        user_input = input("Please select an option: \n1. View On Going Orders,\n2. View Finished Orders,\n3. Add an order,\n4. Confirm that an order is complete,\n5. Remove,\n6. Exit: \n")
        if user_input == "1":
            print(on_going_orders)
        elif user_input == "2":
            print(finished_sandwiches)
        elif user_input == "3":
            add_sandwich_order()
        elif user_input == "4":
            order_finished()  
        elif user_input == "5":
            remove_order()
        elif user_input == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")
if __name__ == "__main__":
    main_menu()
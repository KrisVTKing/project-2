from orders import on_going_orders
from orders import finished_sandwiches

print("ongoing orders: \n", on_going_orders)
print("finished orders: \n", finished_sandwiches)
def remove_order():
    while True:
        print("Ongoing Orders: \n", on_going_orders)
        print("Finished Orders: \n", finished_sandwiches)
        remove = input("What order do you want to remove?\n")
        if remove in on_going_orders:
            confirm = input("Are you sure you want to remove \033[1;32m" + remove + "\033[0m from the order list? (Yes/No)\n")
            if confirm.lower() == "yes":
                on_going_orders.remove(remove)
                print("Order removed.")
                break
            elif confirm.lower() == "no":
                break
            else:
                print("Invalid input.")
                continue
        elif remove in finished_sandwiches:
            confirm = input("Are you sure you want to remove \033[1;32m" + remove + "\033[0m from the finished list? (Yes/No)\n")
            if confirm.lower() == "yes":
                finished_sandwiches.remove(remove)
                print("Order removed.")
                break
            elif confirm.lower() == "no":
                break
            else:
                print("Invalid input.")
                break
    
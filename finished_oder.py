from orders import on_going_orders
from orders import finished_sandwiches

def order_finished():
    while True:
        print (on_going_orders)
        order_confirm = input("Please confirm if the order is completed by typing the name of the order.\n")
        if order_confirm in on_going_orders:
            confirm = input("Are you sure you want to confirm the \033[1;32m" + order_confirm + "\033[0m from the order list? (Yes/No)\n")
            if confirm.lower() == "yes":
                on_going_orders.remove(order_confirm)
                finished_sandwiches.append(order_confirm)
                print("Order confirmed.")
                break
            elif confirm.lower() == "no":
                break
            else:
                print("Invalid input.")
                continue
        else:
            print("Invalid input.")
            break
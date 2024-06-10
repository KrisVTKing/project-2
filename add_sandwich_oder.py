from orders import on_going_orders

def add_sandwich_order():
    while True:
        sandwich = input("What sandwich do you want to order?\n").title()
        confirm = input("Are you sure you want to add \033[1;32m" + sandwich + "\033[0m to the order list? (Yes/No)\n")
        if confirm.lower() == "yes":
            on_going_orders.append(sandwich)
            print("Sandwich ordered.")
            break
        elif confirm.lower() == "no":
            break
        else:
            print("Invalid input.")
            continue

if __name__ == "__main__":
    add_sandwich_order()

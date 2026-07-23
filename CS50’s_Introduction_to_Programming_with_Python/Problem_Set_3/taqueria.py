# Menu that enables a user to place an order, prompting and adding them up, one per line, until the user inputs control-d.

def main():
    compra = 0
    while True:
        try:
            item = input("Item: ")
            item = item.title().strip()
            preco = show_menu(item)

            if preco == "":
                continue

            else:
                compra += preco
                print(f"${compra:.2f}")

        except EOFError:
            print(end="\n")
            break

def show_menu(i):

    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    if i in menu:
        price = menu[i]

        return price

    else:
        return ""


main()

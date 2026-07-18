def main():
    due = 50

    while True:
        cents = int(input("Insert Coin: "))

        if (cents == 25) or (cents == 10) or (cents == 5):

            due = amount_due(due,cents)

            if due == 0:
                print("Change Owed:", due)
                break

            elif due < 0:
                print("Change Owed:", -due)
                break

            print("Amount Due:", due)

        else:
            print("Amount Due:", due)


def amount_due(d, c):
    due = d - c

    return due

main()

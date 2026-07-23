# Making a list of items that the user needs from the grocery store.

def main():

    # Create dictionary.
    items = {}
    while True:
        try:
            # Prompts  the user for items.
            i = input("").upper()
            result = dict_grocery(items, i)

        except EOFError:
            break

    for i in sorted(items):
        print(items[i], i)

# Make the list of items in a dictionary.
def dict_grocery(items, i):

    if i in items:
        items[i] += 1

    else:
        items[i] = 1

main()

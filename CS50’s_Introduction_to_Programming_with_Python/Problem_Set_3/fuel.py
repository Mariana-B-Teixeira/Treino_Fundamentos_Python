def main():
    # Prompts the user for a fraction that indicates how much fuel is in a tank.
    fraction = get_fraction()

    # Outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank
    percentage_output(fraction)

def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")

            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x < 0 or y <= 0:
                raise ValueError

            # Converts to float.
            fraction = x / y

            if fraction > 1:
                pass

            else:
                return fraction

        except (ValueError, ZeroDivisionError):
            pass

def percentage_output(f):
    percentage = f*100

    percentage = round(percentage)

    # If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
    if percentage <= 1:
        return print("E")

    # And if 99% or more remains, output F instead to indicate that the tank is essentially full.
    elif percentage >= 99:
        return print("F")

    else:
        return print(percentage, "%", sep="")

main()

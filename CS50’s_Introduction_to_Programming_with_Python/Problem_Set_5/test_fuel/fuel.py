def main():
    # Prompts the user for a fraction that indicates how much fuel is in a tank.
    f = input()
    percentage = convert(f)

    # Outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank
    print(gauge(percentage))

def convert(fraction):

    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    elif x < 0 or y < 0 or x > y:
        raise ValueError

    else:
        return round((x / y) * 100)

def gauge(percentage):
  # If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
    if percentage <= 1:
        return "E"

    # And if 99% or more remains, output F instead to indicate that the tank is essentially full.
    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

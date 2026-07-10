def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    out  = d.strip('$')
    return float(out)

def percent_to_float(p):
    out = p.strip('%')
    return float(out)/100.00


main()

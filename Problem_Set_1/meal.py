def main():
    t = input("What time is it?")

    if 7.0 <= convert(t) <= 8.0:
        print("breakfast time")

    elif 12.0 <= convert(t) <= 13.0:
        print("lunch time")

    elif 18.0 <= convert(t) <= 19.0:
        print("dinner time")

    else:
        print("")

def convert(time):
    h, m = time.split(":")
    horas = float(h)
    minutos = float(m)

    convTime = horas + minutos/60
    return convTime

if __name__ == "__main__":
    main()

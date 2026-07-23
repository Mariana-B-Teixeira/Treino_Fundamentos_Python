def main():
    while True:
        try:
            # Propts date.
            x = input("Date: ") # MM/DD/YYYY or Mouth DD, YYYY

            # Format date to standardize it.
            if "/" in x:
                mes, dia, ano = x.split("/")
                mes = int(mes)
                dia = int(dia)
                ano = int(ano)

                if mes <= 12 and dia <= 31:
                    print(f"{ano}-{mes:02}-{dia:02}", end = "")
                    break

                else:
                    raise ValueError

            elif "," in x and x.split(" ")[1].endswith(","):
                mes, dia, ano = x.split(" ")
                mes = getting_month(mes)
                mes = int(mes)
                ano = int(ano)
                dia = dia.replace(",", "")
                dia = int(dia)

                if mes <= 12 and dia <= 31:
                    print(f"{ano}-{mes:02}-{dia:02}", end = "")
                    break

                else:
                    raise ValueError

            else:
                raise ValueError

        # Handles invalid date formats.
        except ValueError:
            continue

# Format month.
def getting_month(x):
    list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    for i, mes in enumerate(list, start=1):
            if mes == x:
                return i

    return 0

main()

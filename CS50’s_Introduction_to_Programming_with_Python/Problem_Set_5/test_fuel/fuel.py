def main():
    # Solicita ao usuário uma fração que indica quanto combustível há no tanque.
    f = input()
    percentage = convert(f)

    # Exibe, como uma porcentagem arredondada para o inteiro mais próximo, quanto combustível há no tanque
    print(gauge(percentage))

def convert(fraction):

    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    # Erros de cálculo.
    if y == 0:
        raise ZeroDivisionError

    elif x < 0 or y < 0 or x > y:
        raise ValueError

    else:
        # Arredonda e passa o valor para uma porcentagem (%)
        return round((x / y) * 100)

def gauge(percentage):
  # Se, no entanto, restar 1% ou menos, exibe E para indicar que o tanque está vazio.
    if percentage <= 1:
        return "E"

    # E se restar 99% ou mais, exibe F para indicar que o tanque está cheio.
    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

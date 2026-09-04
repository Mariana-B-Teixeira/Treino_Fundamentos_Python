def main():
    # Solicita ao usuário uma placa de veículo.
    plate = input("Plate: ")
    
    # Verifica se a placa é válida e exibe o resultado.
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_part = ""
    second_part = ""
    bool = True
    c = 0

    # Conta o número total de caracteres na placa.
    for x in s:
        c = c + 1

    # Valida se a placa tem entre 2 e 6 caracteres.
    if c < 2 or c > 6:
        bool = False

    # Verifica se a placa começa com dígitos (deve começar com letras).
    if s[0:1].isdigit():
        bool = False

    # Analisa a partir do terceiro caractere para separar as letras dos números.
    for y in s[2:]:
        if y.isdigit():
            # O primeiro número não pode ser zero ('0').
            if y == "0":
                bool = False

            else:
                # Divide a placa onde começa a sequência numérica.
                index = s.index(y)
                first_part, second_part = s[:index], s[index:]
                break

    # Garante que após o início dos números não existam novas letras.
    for y in second_part:
        if y.isdigit():
            continue
        else:
            bool = False

    # Retorna o status final de validação.
    return bool

# Garante que a função main só seja executada quando o arquivo for rodado diretamente.
if __name__ == "__main__":
    main()

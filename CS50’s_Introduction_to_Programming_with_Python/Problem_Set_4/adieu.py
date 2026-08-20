# Teste da biblioteca inflect

import inflect

# Motor de inflexão que automatiza regras gramaticais da língua inglesa
p = inflect.engine()

def main():

    # Cria lista
    people = []
    while True:
        try:

            # Acrescenta nomes na lista
            name = input("Name: ")
            people.append(name)

        # Para a entrada de nomes aao pressionar Ctrl + D
        except EOFError:
            print(end="\n")
            break

    # Cita nomes da entrada, nessa frase
    print(f"Adieu, adieu, to {p.join(people)}")

main()

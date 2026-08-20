# Módulo Python que lê diretamente do terminal
import sys

# Biblioteca Python
import random

# Teste da biblioteca pyfiglet, com a classe Figlet, para obter fontes de letras
from pyfiglet import Figlet

# Cria objeto da classe Figlet (instância)
figlet = Figlet()

def main():

    # Lista de fontes válidas
    font_list = figlet.getFonts()

    while True:

        # Nome desse script + comando para obter fonte desejada
        if len(sys.argv) == 3:

            first = sys.argv[1]
            second = sys.argv[2]

            if first != "-f" and first != "--font":
                sys.exit("Wrong argument")

            else:
                if second in font_list:

                    # Texto para ser convertido para a fonte desejada
                    text = input("Input: ")

                    figlet.setFont(font=second)

                    # Output do texto na fonte desejada
                    print("Output: ", figlet.renderText(text), sep="", end="")
                    break

                else:

                    # Limita fonte desejada para alguma que seja válida
                    sys.exit("Invalid font")


        # Se a fonte não for escolhida, é colocada uma aleatória no texto
        elif len(sys.argv) == 1:

            # Escolhe fonte aleatória
            second = random.choice(font_list)
            figlet.setFont(font=second)
            text = input("Input: ")

            # Output com fonte aleatória e válida
            print("Output: ", figlet.renderText(text), sep="", end="")
            break

        else:

            # Se a entrada for indesejada, output é Invalid
            sys.exit("Invalid")

# Chamada da função de entrada main()
main()

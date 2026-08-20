# Teste da biblioteca emoji

import emoji
def main():
    # Entrada do código do emoji
    text = input("Input: ")

    #Saída com o código transformado em emoji
    print(emoji.emojize(text, language="alias"))

main()

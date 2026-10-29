frutas = []
valores = []

opcao = 1

while opcao != 0:
    opcao = int(input("\nMEU PROGRAMA: \n1 - Cadastrar frutas\n2 - Exibir frutas\n0 - Sair\n\nDigite a opção desejada: "))

    if opcao == 0:
        print("Saindo...")
        break
    elif opcao == 1:
        novaFruta = input("Digite o nome da fruta: ")
        frutas.append(novaFruta)

        valorFruta = float(input(f"Digite o valor para {novaFruta}: "))
        valores.append(valorFruta)
    elif opcao == 2:
        if len(frutas) == 0:
            print("\n >> Nenhum registro encontrado \n")
        else:
            print("\nFrutas cadastradas: ")

            for f,v in zip(frutas, valores):
                print(f'{f} - R${v}')

            input("Fim da lista, pressione [ENTER] para voltar ao menu.")
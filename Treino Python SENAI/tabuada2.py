#Criação de uma tabuada com laço de repetição

while True:

    numero = int(input("Digite o numero da tabuada: "))

    ##Exemplo de laço de repetição for em python
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

    sair = input("Digite 's' para sair e qualquer tecla para continuar:")
    if(sair.lower() == "s"):
        print("Obrigado por usar meu software! :)")
        break
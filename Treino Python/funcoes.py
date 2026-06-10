#exemplo de funções no python

def idade (anoAtual, anoNasc):
    idade = anoAtual - anoNasc
    return idade

nome = input("Digite seu nome: ")

ano = int(input("Digite o ano em que você nasceu: "))

atual = int(input("Digite o ano atual: "))

print(f"{nome}, você tem {idade(atual, ano)} anos de idade!")
#criar uma função que calcula o imc de uma pessoa
#tabela imc
#imc < 18.5 -> Magro
#imc entre 18.5 e 24.9 -> Normal
#imc entre 25 e 29.9 -> Sobrepeso
#imc entre 30 e 39.9 -> Obesidade
#imc maior ou igual a 40 -> Obesidade Grave

def imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

nome = input("Digite o seu nome: ")

peso = float(input("Digite o seu peso: "))

altura = float(input("Digite a sua altura: "))

valorImc = imc(peso,altura)

print(valorImc)


if valorImc < 18.5:
    print(f"Magro - Imc: {valorImc}")
elif valorImc > 18.5 and valorImc < 24.9:
    print(f"Normal - Imc: {valorImc}")
elif valorImc > 25 and valorImc < 29.9:
    print(f"Sobrepeso - Imc: {valorImc}")
elif valorImc > 30 and valorImc < 39.9:
    print(f"Obesidade - Imc: {valorImc}")
elif valorImc >= 40:
    print(f"Obesidade grave - Imc: {valorImc}")
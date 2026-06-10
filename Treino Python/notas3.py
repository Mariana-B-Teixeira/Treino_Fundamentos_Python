#Crie um programa que receba o nome de um aluno e 3 notas (prova, trabalho, pesquisa), calcule a média dessas notas
#se a méda for maior ou igual a 6, o aluno será aprovado, se a média for maior ou igual a 4, o aluno estará em recuperação
#e caso seja menor que 4, o aluno deve ser reprovado

nome = input("Digite o nome do aluno: ")
prova = float(input("Digite a nota da sua prova: "))
trabalho = float(input("Digite a nota do seu trabalho: "))
pesquisa = float(input("Digite a nota da sua pesquisa: "))

media = (prova + trabalho + pesquisa) / 3

if media >= 6:
    print(f"O aluno {nome} foi aprovado com média {media}")
elif media >=4:
    print(f"O aluno {nome} foi reprovado com nota {media}")
else:
    print(f"O aluno {nome} está de recuperação com nota {media}")
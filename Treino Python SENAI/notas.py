#Crie um programa que receba a nota de um aluno
#e exiba: Aprovado (>=6), Recuperação (entre 4 e 6) ou Reprovado (<4)

nota = float(input("Digite a nota: "))

if nota >= 6:
    print("Aprovado")
elif nota >= 4:
    print("Recuperação")
else:
    print("Reprovado")
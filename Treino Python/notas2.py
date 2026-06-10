#Problema: Nota de trabalho - maior ou igual a 6
#E
#Nota de prova - maior ou igual a 7
#para ser aprovado

nome = input("Digite seu nome.")
trabalho = float(input("Digite sua nota de trabalho."))
prova = float(input("Digite sua nota de prova."))

if (trabalho >= 6) and (prova >= 7):
    print(f"O aluno {nome} foi aprovado, com nota de trabalho {trabalho} e com nota de prova {prova}")
else:
    print(f"O aluno {nome} foi reprovado, com nota de trabalho {trabalho} e com nota de prova {prova}")

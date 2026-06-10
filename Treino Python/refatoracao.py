nome1 = input("Nome do aluno 1: ")

for i in range(3):
    print("Nota:")
nota1_1 = float(input("Nota 1: "))
nota1_2 = float(input("Nota 2: "))
nota1_3 = float(input("Nota 3: "))
media1 = (nota1_1 + nota1_2 + nota1_3) / 3
print(f"\nAluno: {nome1}")
print(f"Média: {media1:.2f}")
if media1 >= 7:
    print("Situação: Aprovado")
if media1 >= 5 and media1 < 7:
    print("Situação: Recuperação")
if media1 < 5:
    print("Situação: Reprovado")

nome2 = input("\nNome do aluno 2: ")
nota2_1 = float(input("Nota 1: "))
nota2_2 = float(input("Nota 2: "))
nota2_3 = float(input("Nota 3: "))
media2 = (nota2_1 + nota2_2 + nota2_3) / 3
print(f"\nAluno: {nome2}")
print(f"Média: {media2:.2f}")
if media2 >= 7:
    print("Situação: Aprovado")
if media2 >= 5 and media2 < 7:
    print("Situação: Recuperação")
if media2 < 5:
    print("Situação: Reprovado")

nome3 = input("\nNome do aluno 3: ")
nota3_1 = float(input("Nota 1: "))
nota3_2 = float(input("Nota 2: "))
nota3_3 = float(input("Nota 3: "))
media3 = (nota3_1 + nota3_2 + nota3_3) / 3
print(f"\nAluno: {nome3}")
print(f"Média: {media3:.2f}")
if media3 >= 7:
    print("Situação: Aprovado")
if media3 >= 5 and media3 < 7:
    print("Situação: Recuperação")
if media3 < 5:
    print("Situação: Reprovado")
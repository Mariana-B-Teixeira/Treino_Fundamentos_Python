def calcular_media(notas):
    soma = 0

    for nota in notas:
        soma = soma + nota

    media = soma / len(notas)
    return media


def verificar_situacao(media):
    if media >= 7:
        print("Aprovado!")
    elif media >= 5 and media < 7:
        print("Recuperação!")
    else:
        print("Reprovado!")


def main():
    nome = input("Digite o nome do aluno: ")
    quantidade = int(input("Quantas notas deseja inserir? "))

    notas = []

    for i in range(quantidade):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

    media = calcular_media(notas)

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")

    verificar_situacao(media)


main()
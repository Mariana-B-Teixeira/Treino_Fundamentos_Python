#Verificando se pode dirigir
idade = int(input("Digite sua idade: "));

if idade >= 18:
    print("Pode dirigir")
elif idade == 17:
    print("Quase lá, mais um ano!")
else:
    print("Não pode dirigir ainda.")
#Listas são estruturas que permitem colecionar (armazenar) itens mutáveis

Frutas = ['Abacaxi', 'Banana', 'Mamão']
#índices      0          1        2

print(f'Tamanho da lista de Frutas: {len(Frutas)}')

print("\n----------------\n")

print("-\nLista 1:\n-")
print(f'1º item: {Frutas[0]}')
print(f'2º item: {Frutas[1]}')
print(f'3º item: {Frutas[2]}')

nova = 'Limão'

print("\n----------------\n")

print("-\nLista 2:\n-")
#adicionamos o novo item à lista:
Frutas.append(nova)

while True: 

    for i in range(len(Frutas)):
        print(f"{i+1}º item: {Frutas[i]}")
    break;
print("\n----------------\n")
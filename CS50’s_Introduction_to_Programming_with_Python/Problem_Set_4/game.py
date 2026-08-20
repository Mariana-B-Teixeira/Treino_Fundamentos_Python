# Testa biblioteca random

import random

while True:
    try:
        # Entrada de nível de dificuldade, ou seja, tamanho do intervalo de números considerados.
        n = int(input("Level: "))

        # Restringe a números positivos, se a entrada for 0 ou negativa, pergunta de novo
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        continue

    except Exception as e:
        continue

# Gera número aleatório dentro do intervalo escolhido
answer = int(random.randint(1,n))

while True:
    try:
        # Usuário tenta adivinhar número
        guess = int(input("Guess: "))

        # Restringe a números positivos, se a entrada for 0 ou negativa, pergunta novamente
        if guess <=0:
            raise ValueError

    except ValueError:
        continue
    except Exception as e:
        continue

    # Corrige resposta do usuário, caso seja válida
    if guess > 0:

        # Output para respostas com valor abaixo do esperado
        if guess < answer:
            print("Too small!")

        # Output para respostas com valor acima do esperado
        elif guess > answer:
            print("Too large!")

        # Output para respostas corretas
        elif guess == answer:
            print("Just right!")
            break

    # Para outras respostas indesejadas, pergunta novamente
    else:
        continue
